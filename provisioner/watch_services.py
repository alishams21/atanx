import os
import json
import time
import yaml
import subprocess
import asyncio
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class RegistryWatcher(FileSystemEventHandler):
    def __init__(self):
        self.debounce_timer = None
        # Get the project root directory (parent of provisioner)
        self.project_root = Path(__file__).resolve().parent.parent
        # Define paths relative to project root
        self.registry_path = self.project_root / 'frontend' / 'src' / 'app' / 'analyzers' / 'registry.json'
        self.compose_path = self.project_root / 'docker-compose.yml'
        self.analytics_code_path = self.project_root / 'frontend' / 'src' / 'app' / 'analyticscode'
        
        # Add these debug lines
        print(f"Project root: {self.project_root}")
        print(f"Registry path: {self.registry_path} (exists: {self.registry_path.exists()})")
        print(f"Compose path: {self.compose_path} (exists: {self.compose_path.exists()})")
        print(f"Analytics path: {self.analytics_code_path} (exists: {self.analytics_code_path.exists()})")
        
        # Process initial state
        self.process_registry()

    def add_service_to_compose(self, analyzer, compose):
        """Add service configuration to docker-compose."""
        compose['services'][analyzer] = {
            'build': {
                'context': f'./frontend/src/app/analyticscode/{analyzer}',
                'dockerfile': 'Dockerfile'
            },
            'networks': ['analyzer-network'],
            'volumes': [
                f'./frontend/src/app/analyticscode/{analyzer}:/app:ro'
            ],
            'environment': [
                f'SERVICE_NAME={analyzer}',
                'SERVICE_PORT=8000',
                'PYTHONPATH=/app'
            ],
            'user': '${DOCKER_UID}:${DOCKER_GID}',
            'restart': 'unless-stopped',
            'healthcheck': {
                'test': ['CMD', 'curl', '-f', 'http://localhost:8000/health'],
                'interval': '30s',
                'timeout': '10s',
                'retries': 3,
                'start_period': '20s'
            }
        }
        return compose

    async def verify_analyzer_files(self, analyzer_path, timeout=30):
        """Verify required analyzer files exist."""
        required_files = ['Dockerfile', 'main.py', 'requirements.txt']
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            all_files_exist = True
            for file in required_files:
                file_path = analyzer_path / file
                if not file_path.exists():
                    print(f"Waiting for {file} in {analyzer_path}... ({round(timeout - (time.time() - start_time))}s remaining)")
                    all_files_exist = False
                    break

            if all_files_exist:
                print(f"All required files found for {analyzer_path.name}")
                
                try:
                    with open(self.compose_path, 'r') as f:
                        compose = yaml.safe_load(f)
                    
                    compose = self.add_service_to_compose(analyzer_path.name, compose)
                    
                    with open(self.compose_path, 'w') as f:
                        yaml.dump(compose, f, sort_keys=False)
                    
                    print(f"Added {analyzer_path.name} to docker-compose.yml")
                    return True
                except Exception as e:
                    print(f"Error updating docker-compose.yml: {e}")
                    return False

            await asyncio.sleep(1)

        print(f"Timeout waiting for files in {analyzer_path}")
        return False

    def start_service(self, service_name):
        """Start a specific service using docker-compose."""
        print(f"Starting service: {service_name}")
        try:
            # Change to the parent directory where docker-compose.yml is located
            os.chdir(self.compose_path.parent)
            
            # First check if the service exists in docker-compose.yml
            result = subprocess.run(
                ['docker-compose', 'config', '--services'],
                capture_output=True,
                text=True,
                check=True
            )
            available_services = result.stdout.strip().split('\n')
            
            if service_name not in available_services:
                print(f"Error: Service '{service_name}' not found in docker-compose.yml")
                print(f"Available services: {available_services}")
                return False

            # Try to build first
            build_result = subprocess.run(
                ['docker-compose', 'build', service_name],
                capture_output=True,
                text=True
            )
            if build_result.stderr:
                print(f"Build stderr: {build_result.stderr}")
            if build_result.stdout:
                print(f"Build output: {build_result.stdout}")

            # Then try to start the service
            result = subprocess.run(
                ['docker-compose', 'up', '-d', service_name],
                capture_output=True,
                text=True
            )
            
            if result.stderr:
                print(f"Start stderr: {result.stderr}")
            if result.stdout:
                print(f"Start output: {result.stdout}")
            
            if result.returncode != 0:
                print(f"Failed to start service {service_name}")
                return False
            
            print(f"Service {service_name} started successfully")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"Error starting {service_name}:")
            print(f"Command: {e.cmd}")
            print(f"Return code: {e.returncode}")
            print(f"Output: {e.output}")
            print(f"Stderr: {e.stderr}")
            return False
        except Exception as e:
            print(f"Unexpected error starting {service_name}: {str(e)}")
            return False
        finally:
            # Change back to the original directory
            os.chdir(str(Path.cwd()))

    def sync_docker_compose_with_registry(self, registry, compose):
        """Sync docker-compose services with registry."""
        CORE_SERVICES = ['gateway', 'backend']
        registered_analyzers = list(registry.keys())
        current_services = [s for s in compose['services'].keys() if s not in CORE_SERVICES]
        
        services_to_remove = [s for s in current_services if s not in registered_analyzers]
        services_to_add = [a for a in registered_analyzers if a not in current_services]

        print('Registered analyzers:', registered_analyzers)
        print('Current services (excluding core):', current_services)
        print('Services to remove:', services_to_remove)
        print('Services to add:', services_to_add)

        return services_to_remove, services_to_add

    def stop_and_remove_service(self, service_name):
        """Stop and remove a service."""
        print(f"Stopping and removing service: {service_name}")
        commands = [
            f"docker-compose stop {service_name}",
            f"docker-compose rm -f {service_name}",
            f"docker ps -q -f name={service_name} | xargs -r docker rm -f",
            f"docker images -q *{service_name}* | xargs -r docker rmi -f"
        ]
        
        try:
            for cmd in commands:
                subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
            print(f"Service {service_name} stopped and removed")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error stopping {service_name}: {e}")
            return False

    async def process_registry(self):
        """Process the current state of the registry."""
        print("Processing current registry state...")
        try:
            with open(self.registry_path, 'r') as f:
                registry = json.load(f)
            
            with open(self.compose_path, 'r') as f:
                compose = yaml.safe_load(f)
                if compose is None:
                    print("Error: docker-compose.yml is empty or invalid")
                    return
                if 'services' not in compose:
                    print("Error: No 'services' section found in docker-compose.yml")
                    return

            print(f"Current registry contents: {json.dumps(registry, indent=2)}")
            print(f"Current compose services: {list(compose['services'].keys())}")

            services_to_remove, services_to_add = self.sync_docker_compose_with_registry(registry, compose)

            # Remove services
            for service in services_to_remove:
                if service in compose['services']:
                    if self.stop_and_remove_service(service):
                        del compose['services'][service]
                        print(f"Removed service {service} from docker-compose.yml")
                        with open(self.compose_path, 'w') as f:
                            yaml.dump(compose, f, sort_keys=False)

            # Add new services
            for analyzer in services_to_add:
                analyzer_path = self.analytics_code_path / analyzer
                print(f"Checking files for {analyzer} at {analyzer_path}")
                
                if analyzer_path.exists():
                    print(f"Waiting for all required files for {analyzer}...")
                    await self.verify_analyzer_files(analyzer_path)

            # Start new services
            for service in services_to_add:
                self.start_service(service)

        except Exception as e:
            print(f"Error processing registry: {e}")

    def on_modified(self, event):
        """Handle registry file modification events."""
        if event.src_path == str(self.registry_path):
            print("Registry changed. Checking analyzers...")
            asyncio.run(self.process_registry())

def main():
    watcher = RegistryWatcher()
    observer = Observer()
    
    # Get the registry directory path using absolute path resolution
    registry_dir = Path(__file__).resolve().parent.parent / 'frontend' / 'src' / 'app' / 'analyzers'
    registry_dir.mkdir(parents=True, exist_ok=True)  # Create directory if it doesn't exist
    
    print(f"Watching directory: {registry_dir}")
    
    observer.schedule(watcher, path=str(registry_dir), recursive=False)
    observer.start()

    print("Watching for analyzer registry changes...")
    
    # Run initial processing
    asyncio.run(watcher.process_registry())
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()

if __name__ == "__main__":
    main() 