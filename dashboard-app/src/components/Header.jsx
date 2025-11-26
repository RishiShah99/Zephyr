import { motion } from 'framer-motion'
import { Minus, Square, X } from 'lucide-react'

// Use window.electron API exposed by preload
export default function Header() {
  const handleMinimize = () => {
    if (window.electron) {
      window.electron.minimize();
    }
  };

  const handleMaximize = () => {
    if (window.electron) {
      window.electron.maximize();
    }
  };

  const handleClose = () => {
    if (window.electron) {
      window.electron.close();
    }
  };

  return (
    <header className="glass h-16 flex items-center justify-between px-6 relative z-10 border-b border-white/5" style={{ WebkitAppRegion: 'drag' }}>
      {/* Title - minimalist and clean */}
      <div className="flex items-center gap-3">
        <div className="relative">
          {/* Simplified wind icon */}
          <div className="relative w-8 h-8 flex items-center justify-center">
            <svg className="w-6 h-6 text-zephyr-silver" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M9.59 4.59A2 2 0 1 1 11 8H2m10.59 11.41A2 2 0 1 0 14 16H2m15.73-8.27A2.5 2.5 0 1 1 19.5 12H2" />
            </svg>
          </div>
        </div>
        <div>
          <h1 className="text-lg font-bold text-zephyr-silver tracking-wider">
            ZEPHYR
          </h1>
          <p className="text-[9px] text-zephyr-silver/40 -mt-0.5 tracking-widest">AI ENGINE</p>
        </div>
      </div>

      {/* Window controls */}
      <div className="flex gap-1" style={{ WebkitAppRegion: 'no-drag' }}>
        <button 
          onClick={handleMinimize}
          className="p-2 hover:bg-white/5 rounded-md transition-colors group"
        >
          <Minus className="w-4 h-4 text-white/50 group-hover:text-white/80" />
        </button>
        <button 
          onClick={handleMaximize}
          className="p-2 hover:bg-white/5 rounded-md transition-colors group"
        >
          <Square className="w-3.5 h-3.5 text-white/50 group-hover:text-white/80" />
        </button>
        <button 
          onClick={handleClose}
          className="p-2 hover:bg-red-500/10 rounded-md transition-colors group"
        >
          <X className="w-4 h-4 text-white/50 group-hover:text-red-400" />
        </button>
      </div>
    </header>
  )
}
