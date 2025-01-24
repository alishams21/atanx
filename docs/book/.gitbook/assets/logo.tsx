'use client'

import { Zap, Atom, Cpu, Wifi, Network, Server, Database, Cloud, Layers, GitBranch, Hexagon } from 'lucide-react'

export default function AtanxHeader() {
  return (
    <div className="relative w-full overflow-hidden bg-gradient-to-br from-gray-100 to-gray-200 p-8 shadow-inner">
      <div className="container relative mx-auto flex flex-col items-center gap-6 text-center">
        <div className="flex items-center gap-3">
          <div className="flex h-16 w-20 items-center justify-center rounded-md bg-gradient-to-br from-purple-600 to-indigo-600 p-2 text-white shadow-lg">
            <svg className="h-full w-full" viewBox="0 0 40 32" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M4 4H36M4 16H36M4 28H36" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/>
              <path d="M12 4V28M28 4V28" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/>
              <circle cx="12" cy="10" r="2" fill="currentColor"/>
              <circle cx="28" cy="22" r="2" fill="currentColor"/>
              <path d="M20 4V12M20 20V28" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/>
            </svg>
          </div>
          <span className="text-4xl font-semibold tracking-tight text-gray-800">
            Atanx
          </span>
        </div>
        <h1 className="max-w-2xl text-2xl font-medium text-gray-700 lg:text-3xl">
          AI powered data professionals
        </h1>
      </div>
      <Zap className="absolute -left-2 top-1/4 h-8 w-8 rotate-12 text-green-400 opacity-30" />
      <Atom className="absolute bottom-1/4 right-4 h-10 w-10 -rotate-12 text-green-500 opacity-20" />
      <Cpu className="absolute left-1/4 top-4 h-6 w-6 text-green-400 opacity-25" />
      <Wifi className="absolute bottom-6 right-1/3 h-8 w-8 text-green-500 opacity-20" />
      <Network className="absolute left-1/3 top-1/3 h-12 w-12 text-green-300 opacity-15" />
      <Server className="absolute right-1/4 bottom-1/4 h-8 w-8 text-green-400 opacity-20" />
      <Database className="absolute left-10 top-1/4 h-6 w-6 text-green-500 opacity-25" />
      <Cloud className="absolute right-10 top-1/6 h-10 w-10 text-green-300 opacity-15" />
      <Layers className="absolute left-1/5 bottom-1/6 h-8 w-8 text-green-400 opacity-20" />
      <GitBranch className="absolute right-1/6 top-1/3 h-7 w-7 text-green-500 opacity-25" />
      <Hexagon className="absolute left-2/3 top-1/4 h-9 w-9 text-green-300 opacity-15" />
      <div className="absolute -bottom-2 left-1/3 h-4 w-4 rounded-full bg-green-300 opacity-25"></div>
      <div className="absolute right-1/4 top-2 h-3 w-3 rounded-full bg-green-400 opacity-20"></div>
      <div className="absolute left-1/2 top-1/2 h-5 w-5 rounded-full bg-green-200 opacity-15"></div>
      <div className="absolute bottom-1/3 left-10 h-6 w-6 rounded-full border border-green-400 opacity-20"></div>
      <div className="absolute right-8 top-1/3 h-4 w-4 rotate-45 rounded-sm bg-green-300 opacity-15"></div>
      <div className="absolute left-1/4 top-3/4 h-8 w-8 rounded-md border-2 border-green-500 opacity-10"></div>
      <div className="absolute right-1/5 top-2/3 h-6 w-6 rounded-full border-2 border-green-300 opacity-15"></div>
      <div className="absolute left-2/3 bottom-1/4 h-5 w-5 rotate-45 rounded-sm bg-green-400 opacity-20"></div>
      <div className="absolute left-1/6 top-1/5 h-7 w-7 rounded-full border-4 border-green-300 opacity-10"></div>
      <div className="absolute right-1/3 bottom-1/5 h-6 w-6 rotate-12 rounded-md bg-green-400 opacity-15"></div>
      <svg className="absolute left-0 top-0 h-full w-full" xmlns="http://www.w3.org/2000/svg">
        <line x1="0" y1="0" x2="100%" y2="100%" stroke="rgba(52, 211, 153, 0.1)" strokeWidth="1" />
        <line x1="100%" y1="0" x2="0" y2="100%" stroke="rgba(52, 211, 153, 0.1)" strokeWidth="1" />
        <line x1="50%" y1="0" x2="50%" y2="100%" stroke="rgba(52, 211, 153, 0.1)" strokeWidth="1" strokeDasharray="4 4" />
        <line x1="0" y1="50%" x2="100%" y2="50%" stroke="rgba(52, 211, 153, 0.1)" strokeWidth="1" strokeDasharray="4 4" />
        <circle cx="20%" cy="30%" r="5" fill="rgba(52, 211, 153, 0.1)" />
        <circle cx="80%" cy="70%" r="7" fill="rgba(52, 211, 153, 0.1)" />
        <rect x="70%" y="20%" width="10" height="10" fill="rgba(52, 211, 153, 0.1)" />
        <polygon points="30,40 40,20 50,40" fill="rgba(52, 211, 153, 0.1)" />
        <path d="M60,80 Q70,70 80,80 T100,80" stroke="rgba(52, 211, 153, 0.1)" fill="none" />
        <ellipse cx="25%" cy="75%" rx="15" ry="10" fill="rgba(52, 211, 153, 0.1)" />
      </svg>
    </div>
  )
}

