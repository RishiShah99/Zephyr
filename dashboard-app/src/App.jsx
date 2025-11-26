import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import Sidebar from './components/Sidebar'
import Header from './components/Header'
import Dashboard from './components/Dashboard'
import Memory from './components/Memory'
import Projects from './components/Projects'
import TestZone from './components/TestZone'

function App() {
  const [currentPage, setCurrentPage] = useState('dashboard')

  const renderPage = () => {
    switch (currentPage) {
      case 'dashboard':
        return <Dashboard />
      case 'memory':
        return <Memory />
      case 'projects':
        return <Projects />
      case 'test':
        return <TestZone />
      default:
        return <Dashboard />
    }
  }

  return (
    <div className="h-screen w-screen bg-zephyr-gradient overflow-hidden relative">
      {/* Subtle flowing lines - representing invisible wind/air */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none opacity-20">
        {/* Horizontal flow lines */}
        {[...Array(6)].map((_, i) => (
          <motion.div
            key={`flow-${i}`}
            className="absolute h-px bg-gradient-to-r from-transparent via-zephyr-silver to-transparent"
            style={{
              top: `${15 + i * 15}%`,
              width: '100%',
              left: '-100%',
            }}
            animate={{
              left: ['0%', '100%'],
            }}
            transition={{
              duration: 4 + i * 0.5,
              repeat: Infinity,
              ease: 'linear',
              delay: i * 0.5,
            }}
          />
        ))}

        {/* Diagonal wind streaks - minimal and elegant */}
        {[...Array(8)].map((_, i) => (
          <motion.div
            key={`streak-${i}`}
            className="absolute w-24 h-px bg-gradient-to-r from-transparent via-zephyr-accent-dim to-transparent"
            style={{
              top: `${Math.random() * 100}%`,
              left: '-10%',
              transform: 'rotate(-12deg)',
            }}
            animate={{
              left: ['0%', '110%'],
              opacity: [0, 0.4, 0],
            }}
            transition={{
              duration: 3 + Math.random() * 2,
              repeat: Infinity,
              ease: 'easeOut',
              delay: i * 0.3,
            }}
          />
        ))}

        {/* Floating particles - subtle air movement */}
        {[...Array(12)].map((_, i) => {
          const startX = Math.random() * 100;
          const startY = Math.random() * 100;
          const endX = startX + 15;
          const endY = startY - 8;
          
          return (
            <motion.div
              key={`particle-${i}`}
              className="absolute w-1 h-1 bg-zephyr-silver rounded-full"
              style={{
                left: `${startX}%`,
                top: `${startY}%`,
              }}
              animate={{
                left: [`${startX}%`, `${endX}%`],
                top: [`${startY}%`, `${endY}%`],
                opacity: [0, 0.5, 0],
                scale: [0.5, 1.2, 0.5],
              }}
              transition={{
                duration: 5 + Math.random() * 3,
                repeat: Infinity,
                delay: i * 0.2,
                ease: 'easeInOut',
              }}
            />
          );
        })}

        {/* Corner accent lines - minimal tech aesthetic */}
        <div className="absolute top-0 left-0 w-24 h-24">
          <div className="absolute top-0 left-0 w-full h-px bg-gradient-to-r from-zephyr-accent-dim to-transparent opacity-40" />
          <div className="absolute top-0 left-0 w-px h-full bg-gradient-to-b from-zephyr-accent-dim to-transparent opacity-40" />
        </div>
        <div className="absolute top-0 right-0 w-24 h-24">
          <div className="absolute top-0 right-0 w-full h-px bg-gradient-to-l from-zephyr-accent-dim to-transparent opacity-40" />
          <div className="absolute top-0 right-0 w-px h-full bg-gradient-to-b from-zephyr-accent-dim to-transparent opacity-40" />
        </div>
        <div className="absolute bottom-0 left-0 w-24 h-24">
          <div className="absolute bottom-0 left-0 w-full h-px bg-gradient-to-r from-zephyr-accent-dim to-transparent opacity-40" />
          <div className="absolute bottom-0 left-0 w-px h-full bg-gradient-to-t from-zephyr-accent-dim to-transparent opacity-40" />
        </div>
        <div className="absolute bottom-0 right-0 w-24 h-24">
          <div className="absolute bottom-0 right-0 w-full h-px bg-gradient-to-l from-zephyr-accent-dim to-transparent opacity-40" />
          <div className="absolute bottom-0 right-0 w-px h-full bg-gradient-to-t from-zephyr-accent-dim to-transparent opacity-40" />
        </div>
      </div>

      {/* Main container */}
      <div className="relative h-full flex">
        {/* Sidebar */}
        <Sidebar currentPage={currentPage} setCurrentPage={setCurrentPage} />

        {/* Main content */}
        <div className="flex-1 flex flex-col">
          {/* Header */}
          <Header />

          {/* Page content with transitions */}
          <AnimatePresence mode="wait">
            <motion.div
              key={currentPage}
              initial={{ opacity: 0, x: 100 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -100 }}
              transition={{ duration: 0.2, ease: 'easeOut' }}
              className="flex-1 overflow-auto p-8"
            >
              {renderPage()}
            </motion.div>
          </AnimatePresence>
        </div>
      </div>
    </div>
  )
}

export default App
