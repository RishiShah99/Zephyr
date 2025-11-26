import { motion } from 'framer-motion'
import { Lightbulb, FolderOpen, Calendar, Plus, Trash2 } from 'lucide-react'
import { useState, useEffect } from 'react'

export default function Projects() {
  const [projects, setProjects] = useState([])
  const [loading, setLoading] = useState(true)
  const [showAddForm, setShowAddForm] = useState(false)
  const [newName, setNewName] = useState('')
  const [newDescription, setNewDescription] = useState('')

  // Fetch projects on mount
  useEffect(() => {
    fetchProjects()
  }, [])

  const fetchProjects = async () => {
    try {
      setLoading(true)
      console.log('Fetching projects from API...')
      const data = await window.zephyrAPI.getProjects()
      console.log('Projects API response:', data)
      if (data.success) {
        console.log('Setting projects:', data.projects)
        setProjects(data.projects)
      } else {
        console.error('API returned error:', data.error)
      }
    } catch (error) {
      console.error('Failed to fetch projects:', error)
    } finally {
      setLoading(false)
    }
  }

  const addProject = async () => {
    if (!newName) return
    
    try {
      const response = await fetch('http://localhost:5000/projects', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: newName, description: newDescription })
      })
      
      const data = await response.json()
      if (data.success) {
        setNewName('')
        setNewDescription('')
        setShowAddForm(false)
        fetchProjects() // Refresh the list
      }
    } catch (error) {
      console.error('Failed to add project:', error)
    }
  }

  const deleteProject = async (project) => {
    if (!confirm(`Delete project "${project.name}"?`)) return
    
    try {
      const response = await fetch('http://localhost:5000/projects', {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: project.name })
      })
      
      const data = await response.json()
      if (data.success) {
        fetchProjects() // Refresh the list
      }
    } catch (error) {
      console.error('Failed to delete project:', error)
    }
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-white/60">Loading projects...</div>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-3xl font-bold text-white mb-2">Project Ideas</h2>
          <p className="text-white/60">Your structured project templates</p>
        </div>
        <motion.button
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          onClick={() => setShowAddForm(!showAddForm)}
          className="px-6 py-3 rounded-xl bg-gradient-to-r from-purple-500 to-blue-500 text-white font-semibold shadow-lg hover:shadow-2xl transition-shadow flex items-center gap-2"
        >
          <Plus className="w-5 h-5" />
          New Idea
        </motion.button>
      </div>

      {/* Add Form */}
      {showAddForm && (
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className="glass rounded-2xl p-6 border border-white/10"
        >
          <input
            type="text"
            placeholder="Project Name"
            value={newName}
            onChange={(e) => setNewName(e.target.value)}
            className="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white placeholder-white/40 focus:outline-none focus:border-purple-500 mb-4"
          />
          <textarea
            placeholder="Project Description"
            value={newDescription}
            onChange={(e) => setNewDescription(e.target.value)}
            rows={3}
            className="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white placeholder-white/40 focus:outline-none focus:border-purple-500 mb-4 resize-none"
          />
          <div className="flex gap-3">
            <button
              onClick={addProject}
              className="px-6 py-2 rounded-lg bg-purple-500 text-white font-semibold hover:bg-purple-600 transition-colors"
            >
              Create Project
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

      {/* Projects grid */}
      <div className="grid grid-cols-1 gap-6">
        {projects.map((project, index) => (
          <motion.div
            key={project.name}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.1 }}
            whileHover={{ scale: 1.02 }}
            className="glass rounded-2xl p-6 border border-white/10 group cursor-pointer relative overflow-hidden"
          >
            {/* Status badge and delete button */}
            <div className="absolute top-6 right-6 flex items-center gap-2">
              <div className={`px-3 py-1 rounded-full text-xs font-semibold ${
                project.status === 'Active' 
                  ? 'bg-green-500/20 text-green-400' 
                  : 'bg-blue-500/20 text-blue-400'
              }`}>
                {project.status}
              </div>
              <motion.button
                whileHover={{ scale: 1.1 }}
                whileTap={{ scale: 0.9 }}
                onClick={(e) => { e.stopPropagation(); deleteProject(project); }}
                className="opacity-0 group-hover:opacity-100 transition-opacity p-2 rounded-lg bg-red-500/20 hover:bg-red-500/30 text-red-400"
              >
                <Trash2 className="w-4 h-4" />
              </motion.button>
            </div>

            <div className="flex gap-4">
              {/* Icon */}
              <div className="w-14 h-14 rounded-xl bg-gradient-to-br from-yellow-500 to-orange-500 flex items-center justify-center shrink-0 shadow-lg">
                <Lightbulb className="w-7 h-7 text-white" />
              </div>

              {/* Content */}
              <div className="flex-1">
                <h3 className="text-2xl font-bold text-white mb-2">{project.name}</h3>
                <p className="text-white/60 mb-4">{project.description || 'No description'}</p>

                {/* Tech stack */}
                {project.tech_stack && project.tech_stack.length > 0 && (
                  <div className="flex flex-wrap gap-2 mb-4">
                    {project.tech_stack.map((tech) => (
                      <span
                        key={tech}
                        className="px-3 py-1 rounded-lg bg-white/5 text-white/70 text-sm font-mono"
                      >
                        {tech}
                      </span>
                    ))}
                  </div>
                )}

                {/* Footer */}
                <div className="flex items-center gap-4 text-white/40 text-sm">
                  <div className="flex items-center gap-2">
                    <Calendar className="w-4 h-4" />
                    <span>Created {project.created}</span>
                  </div>
                </div>
              </div>
            </div>

            {/* Hover glow */}
            <div className="absolute inset-0 bg-gradient-to-r from-yellow-500/0 to-orange-500/0 group-hover:from-yellow-500/5 group-hover:to-orange-500/5 rounded-2xl transition-all" />
          </motion.div>
        ))}
      </div>

      {/* Empty state */}
      {projects.length === 0 && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="glass rounded-2xl p-12 border border-white/10 text-center"
        >
          <Lightbulb className="w-16 h-16 text-white/20 mx-auto mb-4" />
          <h3 className="text-xl font-bold text-white/60 mb-2">No project ideas yet</h3>
          <p className="text-white/40">Try saying: "idea for a weather app"</p>
        </motion.div>
      )}
    </div>
  )
}
