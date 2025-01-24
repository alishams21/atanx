import React from 'react'

const AtanxLogo: React.FC<{ className?: string }> = ({ className = '' }) => {
  return (
    <div className={`flex h-16 w-20 items-center justify-center rounded-md bg-gradient-to-br from-purple-600 to-indigo-600 p-2 text-white shadow-lg ${className}`}>
      <svg 
        className="h-full w-full text-white"
        viewBox="0 0 40 32" 
        fill="none" 
        xmlns="http://www.w3.org/2000/svg"
      >
        <path 
          d="M4 4H36M4 16H36M4 28H36" 
          stroke="white"
          strokeWidth="2" 
          strokeLinecap="round"
        />
        <path 
          d="M12 4V28M28 4V28" 
          stroke="white"
          strokeWidth="2" 
          strokeLinecap="round"
        />
        <circle 
          cx="12" 
          cy="10" 
          r="2" 
          fill="white"
        />
        <circle 
          cx="28" 
          cy="22" 
          r="2" 
          fill="white"
        />
        <path 
          d="M20 4V12M20 20V28" 
          stroke="white"
          strokeWidth="2" 
          strokeLinecap="round"
        />
      </svg>
    </div>
  )
}

export default AtanxLogo 
