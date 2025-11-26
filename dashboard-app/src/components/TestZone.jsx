import { useState } from 'react'
import { motion } from 'framer-motion'
import { Send, Terminal, Trash2 } from 'lucide-react'

const quickTests = [
  'tell me a joke',
  'list my project ideas',
  'recall',
  'find files named test',
  'play some lofi',
  'what\'s the weather',
]

export default function TestZone() {
  const [command, setCommand] = useState('')
  const [output, setOutput] = useState([])
  const [isLoading, setIsLoading] = useState(false)

  const runCommand = async () => {
    if (!command.trim()) return

    // Add command to output
    setOutput(prev => [...prev, { type: 'command', text: command }])
    setIsLoading(true)
    
    try {
      // Call the actual API
      const data = await window.zephyrAPI.sendCommand(command)
      
      setOutput(prev => [...prev, { 
        type: 'response', 
        text: data.response || 'Command executed successfully'
      }])
    } catch (error) {
      setOutput(prev => [...prev, { 
        type: 'error', 
        text: `Error: ${error.message || 'Failed to execute command'}`
      }])
    } finally {
      setIsLoading(false)
    }

    setCommand('')
  }

  const clearOutput = () => {
    setOutput([])
  }

  return (
    <div className="space-y-6 flex flex-col h-full max-h-[calc(100vh-200px)]">
      {/* Header */}
      <div className="flex-shrink-0 flex items-center justify-between">
        <div>
          <h2 className="text-3xl font-bold text-white mb-2">Test Zone</h2>
          <p className="text-white/60">Try out Zephyr commands in real-time</p>
        </div>
        {output.length > 0 && (
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={clearOutput}
            className="px-4 py-2 rounded-lg bg-red-500/20 border border-red-500/30 text-red-400 hover:bg-red-500/30 transition-all flex items-center gap-2"
          >
            <Trash2 className="w-4 h-4" />
            Clear
          </motion.button>
        )}
      </div>

      {/* Quick test buttons */}
      <div className="flex flex-wrap gap-2 flex-shrink-0">
        {quickTests.map((test) => (
          <motion.button
            key={test}
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={() => setCommand(test)}
            className="px-4 py-2 rounded-lg glass border border-white/10 text-white/70 hover:text-white hover:border-purple-500/50 text-sm font-mono transition-all"
          >
            {test}
          </motion.button>
        ))}
      </div>

      {/* Output terminal - FIXED OVERFLOW */}
      <div className="flex-1 glass rounded-2xl border border-white/10 p-6 overflow-y-auto overflow-x-hidden font-mono text-sm min-h-0">
        {output.length === 0 ? (
          <div className="flex items-center justify-center h-full text-white/30">
            <div className="text-center">
              <Terminal className="w-12 h-12 mx-auto mb-4 opacity-50" />
              <p>No commands run yet. Try typing a command below!</p>
            </div>
          </div>
        ) : (
          <div className="space-y-4 max-w-full">
            {output.map((item, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                className={
                  item.type === 'command' 
                    ? 'text-zephyr-accent break-all overflow-hidden' 
                    : item.type === 'error'
                    ? 'text-red-400 break-all overflow-hidden'
                    : 'text-white/70 break-all overflow-hidden whitespace-pre-wrap max-w-full'
                }
                style={{ wordBreak: 'break-all', overflowWrap: 'anywhere' }}
              >
                {item.type === 'command' && <span className="text-zephyr-silver">→ </span>}
                {item.type === 'error' && <span className="text-red-500">✗ </span>}
                <span className="inline-block max-w-full">{item.text}</span>
              </motion.div>
            ))}
            {isLoading && (
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="text-zephyr-accent/60"
              >
                <span className="animate-pulse">⟳ Processing...</span>
              </motion.div>
            )}
          </div>
        )}
      </div>

      {/* Input area - FIXED: Always visible */}
      <div className="flex-shrink-0 glass rounded-2xl border border-white/10 p-4 flex gap-3">
        <input
          type="text"
          value={command}
          onChange={(e) => setCommand(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && runCommand()}
          placeholder="Type a command..."
          className="flex-1 bg-transparent text-white placeholder-white/40 outline-none font-mono"
        />
        <motion.button
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          onClick={runCommand}
          disabled={isLoading || !command.trim()}
          className="px-6 py-2 rounded-lg bg-gradient-to-r from-zephyr-accent to-zephyr-accent-dim text-white font-semibold shadow-lg hover:shadow-2xl transition-shadow flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          <Send className="w-4 h-4" />
          {isLoading ? 'Running...' : 'Run'}
        </motion.button>
      </div>
    </div>
  )
}
