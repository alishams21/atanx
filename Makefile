.PHONY: all backend frontend provisioner install-next stop stop-backend stop-frontend stop-provisioner

# Default target that shows available commands
help:
	@echo "Available commands:"
	@echo "  make start-backend     - Run backend and gateway services"
	@echo "  make start-frontend    - Run frontend application"
	@echo "  make start-provisioner - Run provisioner service"
	@echo "  make start-all         - Run everything in the correct order"
	@echo "  make stop-all          - Stop all services"
	@echo "  make stop-backend      - Stop backend services"
	@echo "  make stop-frontend     - Stop frontend service"
	@echo "  make stop-provisioner  - Stop provisioner service"

# Setup Python virtual environment and install requirements
setup-provisioner:
	python -m venv venv
	. venv/bin/activate && \
	pip install -r provisioner/requirements.txt

# Run backend and gateway
start-backend:
	docker-compose up --build

# Install Next.js if not present and run frontend
start-frontend:
	cd frontend && \
	yarn install && \
	if ! yarn list --pattern next | grep -q "next@"; then \
		yarn add next; \
	fi && \
	yarn dev

# Run provisioner
start-provisioner:
	@if [ ! -d "venv" ]; then \
		make setup-provisioner; \
	fi
	. venv/bin/activate && \
	python provisioner/watch_services.py

# Run everything in parallel
start-all:
	make start-backend & \
	make start-frontend & \
	make start-provisioner & \
	wait; \
	echo "All services started"

# Stop backend services
stop-backend:
	docker-compose down

# Stop frontend service (finds and kills the Next.js process)
stop-frontend:
	@pkill -f "next dev" || true

# Stop provisioner service
stop-provisioner:
	@pkill -f "watch_services.py" || true

# Stop all services
stop-all: 
	make stop-backend & \
	make stop-frontend & \
	make stop-provisioner & \
	wait; \
	echo "All services stopped" 
