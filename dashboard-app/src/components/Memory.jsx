import { motion } from 'framer-motion'
import { Brain, Calendar, Plus, Trash2 } from 'lucide-react'
import { useState, useEffect } from 'react'

export default function Memory() {
  const [facts, setFacts] = useState([])
  const [loading, setLoading] = useState(true)
  const [newKey, setNewKey] = useState('')
  const [newValue, setNewValue] = useState('')
  const [showAddForm, setShowAddForm] = useState(false)

  // Fetch memory on mount
  useEffect(() => {
    fetchMemory()
  }, [])

  const fetchMemory = async () => {
    try {
      setLoading(true)
      console.log('Fetching memory from API...')
      const data = await window.zephyrAPI.getMemory()
      console.log('Memory API response:', data)
      if (data.success) {
        console.log('Setting facts:', data.memory)
        setFacts(data.memory)
      } else {
        console.error('API returned error:', data.error)
      }
    } catch (error) {
      console.error('Failed to fetch memory:', error)
    } finally {
      setLoading(false)
    }
  }

  const addMemory = async () => {
    if (!newKey || !newValue) return
    
    try {
      const response = await fetch('http://localhost:5000/memory', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ key: newKey, value: newValue })
      })
      
      const data = await response.json()
      if (data.success) {
        setNewKey('')
        setNewValue('')
        setShowAddForm(false)
        fetchMemory() // Refresh the list
      }
    } catch (error) {
      console.error('Failed to add memory:', error)
    }
  }

  const deleteMemory = async (fact) => {
    if (!confirm(`Delete "${fact.key}"?`)) return
    
    try {
      const response = await fetch('http://localhost:5000/memory', {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          type: fact.type,
          category: fact.category,
          key: fact.key,
          id: fact.id
        })
      })
      
      const data = await response.json()
      if (data.success) {
        fetchMemory() // Refresh the list
      }
    } catch (error) {
      console.error('Failed to delete memory:', error)
    }
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-white/60">Loading memory...</div>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-3xl font-bold text-white mb-2">Memory Bank</h2>
          <p className="text-white/60">Everything Zephyr knows about you</p>
        </div>
        <div className="flex gap-4 items-center">
          <div className="glass rounded-xl px-6 py-3 border border-white/10">
            <div className="text-white/60 text-sm">Total Facts</div>
            <div className="text-3xl font-bold text-white">{facts.length}</div>
          </div>
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={() => setShowAddForm(!showAddForm)}
            className="px-6 py-3 rounded-xl bg-gradient-to-r from-purple-500 to-blue-500 text-white font-semibold shadow-lg hover:shadow-2xl transition-shadow flex items-center gap-2"
          >
            <Plus className="w-5 h-5" />
            Add Memory
          </motion.button>
        </div>
      </div>

      {/* Add Form */}
      {showAddForm && (
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className="glass rounded-2xl p-6 border border-white/10"
        >
          <div className="grid grid-cols-2 gap-4 mb-4">
            <input
              type="text"
              placeholder="Key (e.g., favorite_color)"
              value={newKey}
              onChange={(e) => setNewKey(e.target.value)}
              className="px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white placeholder-white/40 focus:outline-none focus:border-purple-500"
            />
            <input
              type="text"
              placeholder="Value (e.g., blue)"
              value={newValue}
              onChange={(e) => setNewValue(e.target.value)}
              className="px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white placeholder-white/40 focus:outline-none focus:border-purple-500"
            />
          </div>
          <div className="flex gap-3">
            <button
              onClick={addMemory}
              className="px-6 py-2 rounded-lg bg-purple-500 text-white font-semibold hover:bg-purple-600 transition-colors"
            >
              Save Memory
            </button>
            <button
              onClick={() => setShowAddForm(false)}
              className="px-6 py-2 rounded-lg bg-white/5 text-white font-semibold hover:bg-white/10 transition-colors"
            >
              Cancel
            </button>
          </div>
        </motion.div>
      )}

      {/* Facts list */}
      <div className="space-y-4">
        {facts.map((fact, index) => (
          <motion.div
            key={fact.key}
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: index * 0.1 }}
            whileHover={{ scale: 1.02 }}
            className="glass rounded-2xl p-6 border border-white/10 group cursor-pointer"
          >
            <div className="flex items-start justify-between">
              <div className="flex gap-4 flex-1">
                {/* Icon */}
                <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-purple-500 to-blue-500 flex items-center justify-center shrink-0">
                  <Brain className="w-6 h-6 text-white" />
                </div>

                {/* Content */}
                <div className="flex-1">
                  <h3 className="text-lg font-semibold text-white mb-1 capitalize">
                    {fact.key.replace(/_/g, ' ')}
                  </h3>
                  <p className="text-2xl font-bold bg-gradient-to-r from-purple-400 to-blue-400 bg-clip-text text-transparent mb-3">
                    {fact.value}
                  </p>
                  <div className="flex items-center gap-2 text-white/40 text-sm">
                    <Calendar className="w-4 h-4" />
                    <span>Stored on {fact.timestamp}</span>
                  </div>
                </div>
              </div>

              {/* Delete button */}
              <motion.button
                whileHover={{ scale: 1.1 }}
                whileTap={{ scale: 0.9 }}
                onClick={(e) => { e.stopPropagation(); deleteMemory(fact); }}
                className="opacity-0 group-hover:opacity-100 transition-opacity p-2 rounded-lg bg-red-500/20 hover:bg-red-500/30 text-red-400"
              >
                <Trash2 className="w-4 h-4" />
              </motion.button>

              {/* Hover glow */}
              <div className="absolute inset-0 bg-gradient-to-r from-purple-500/0 to-blue-500/0 group-hover:from-purple-500/5 group-hover:to-blue-500/5 rounded-2xl transition-all" />
            </div>
          </motion.div>
        ))}
      </div>

      {/* Empty state if no facts */}
      {facts.length === 0 && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="glass rounded-2xl p-12 border border-white/10 text-center"
        >
          <Brain className="w-16 h-16 text-white/20 mx-auto mb-4" />
          <h3 className="text-xl font-bold text-white/60 mb-2">No facts stored yet</h3>
          <p className="text-white/40">Try saying: "remember my favorite color is blue"</p>
        </motion.div>
      )}
    </div>
  )
}
