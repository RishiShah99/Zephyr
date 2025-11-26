import { motion } from 'framer-motion'
import { LayoutDashboard, Brain, Lightbulb, FlaskConical, Sparkles } from 'lucide-react'

const navItems = [
  { id: 'dashboard', label: 'Dashboard', icon: LayoutDashboard },
  { id: 'memory', label: 'Memory', icon: Brain },
  { id: 'projects', label: 'Projects', icon: Lightbulb },
  { id: 'test', label: 'Test Zone', icon: FlaskConical },
]

export default function Sidebar({ currentPage, setCurrentPage }) {
  return (
    <aside className="w-64 glass border-r border-white/10 flex flex-col">
      {/* Logo section */}
      <div className="p-6 border-b border-white/5">
        <div className="flex items-center gap-3">
          <div className="relative">
            {/* Simple wind icon */}
            <div className="w-10 h-10 bg-zephyr-gray border border-white/10 rounded-lg flex items-center justify-center">
              <svg className="w-6 h-6 text-zephyr-silver" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M9.59 4.59A2 2 0 1 1 11 8H2m10.59 11.41A2 2 0 1 0 14 16H2m15.73-8.27A2.5 2.5 0 1 1 19.5 12H2" />
              </svg>
            </div>
          </div>
          <div>
            <h2 className="text-zephyr-silver font-bold text-base tracking-wider">ZEPHYR</h2>
            <p className="text-zephyr-silver/40 text-[9px] tracking-widest">AI ENGINE</p>
          </div>
        </div>
      </div>

      {/* Navigation */}
      <nav className="flex-1 p-4 space-y-2">
        {navItems.map((item) => {
          const Icon = item.icon
          const isActive = currentPage === item.id

          return (
            <motion.button
              key={item.id}
              onClick={() => setCurrentPage(item.id)}
              className={`
                w-full flex items-center gap-3 px-4 py-3 rounded-xl
                transition-all duration-150 relative overflow-hidden
                ${isActive ? 'text-zephyr-accent' : 'text-white/60 hover:text-white hover:bg-white/5'}
              `}
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
            >
              {/* Active indicator - clean and minimal */}
              {isActive && (
                <motion.div
                  layoutId="activeTab"
                  className="absolute inset-0 bg-zephyr-accent/10 rounded-xl border border-zephyr-accent/30"
                  transition={{ type: 'spring', stiffness: 300, damping: 30 }}
                />
              )}

              {/* Icon and label */}
              <Icon className={`w-5 h-5 relative z-10 ${isActive ? 'text-zephyr-accent' : ''}`} />
              <span className="relative z-10 font-medium">{item.label}</span>
            </motion.button>
          )
        })}
      </nav>

      {/* Footer */}
      <div className="p-4 border-t border-white/5">
        <div className="text-zephyr-silver/30 text-[9px] text-center tracking-wider">
          <p className="text-zephyr-silver/50 font-semibold">ZEPHYR v3.0</p>
          <p className="mt-1">OS-INTEGRATED AI</p>
        </div>
      </div>
    </aside>
  )
}
