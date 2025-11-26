import { motion } from 'framer-motion'
import FeatureCard from './FeatureCard'
import { Brain, Music, Search, Calendar, Newspaper, Sparkles, Eye, Zap } from 'lucide-react'

const features = [
  {
    icon: Brain,
    title: 'Memory System',
    description: 'Store and recall facts instantly',
    gradient: 'from-purple-500 to-pink-500',
    examples: ['remember my favorite color', 'what do you know about me'],
  },
  {
    icon: Music,
    title: 'Spotify Control',
    description: 'Voice-controlled music playback',
    gradient: 'from-green-500 to-emerald-500',
    examples: ['play some lofi', 'pause music', "what's playing"],
  },
  {
    icon: Search,
    title: 'File Search',
    description: 'Find anything on your computer',
    gradient: 'from-blue-500 to-cyan-500',
    examples: ['find files named zephyr', 'search python files'],
  },
  {
    icon: Sparkles,
    title: 'Project Ideas',
    description: 'Auto-generate project structures',
    gradient: 'from-yellow-500 to-orange-500',
    examples: ['idea for a todo app', 'list my projects'],
  },
  {
    icon: Calendar,
    title: 'Daily Briefings',
    description: 'Morning and evening summaries',
    gradient: 'from-indigo-500 to-purple-500',
    examples: ['show briefing', 'morning summary'],
  },
  {
    icon: Newspaper,
    title: 'Latest News',
    description: 'Stay updated with current events',
    gradient: 'from-red-500 to-rose-500',
    examples: ['latest news', 'tech news today'],
  },
  {
    icon: Zap,
    title: 'Smart NLP',
    description: 'Understands natural language',
    gradient: 'from-cyan-500 to-blue-500',
    examples: ['Automatically detects your intent'],
  },
  {
    icon: Eye,
    title: 'Screen Invisible',
    description: 'Hidden from screen shares',
    gradient: 'from-gray-500 to-slate-500',
    examples: ['Perfect for interviews & demos'],
  },
]

export default function Dashboard() {
  return (
    <div className="space-y-8">
      {/* Welcome section */}
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="glass rounded-2xl p-8 border border-white/10"
      >
        <h2 className="text-4xl font-bold text-white mb-2">
          Welcome to <span className="text-zephyr-accent">Zephyr</span>
        </h2>
        <p className="text-white/60 text-lg">
          Your intelligent OS-integrated AI assistant. Fast, powerful, and invisible when needed.
        </p>
      </motion.div>

      {/* Feature grid */}
      <div>
        <h3 className="text-2xl font-bold text-white mb-6">All Features</h3>
        <div className="grid grid-cols-2 gap-6">
          {features.map((feature, index) => (
            <FeatureCard key={feature.title} feature={feature} index={index} />
          ))}
        </div>
      </div>

      {/* Quick stats */}
      <div className="grid grid-cols-3 gap-6">
        <motion.div
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.2 }}
          className="glass rounded-2xl p-6 border border-white/10"
        >
          <div className="text-white/60 text-sm mb-2">Commands Today</div>
          <div className="text-4xl font-bold text-white">24</div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.3 }}
          className="glass rounded-2xl p-6 border border-white/10"
        >
          <div className="text-white/60 text-sm mb-2">Facts Stored</div>
          <div className="text-4xl font-bold text-white">12</div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.4 }}
          className="glass rounded-2xl p-6 border border-white/10"
        >
          <div className="text-white/60 text-sm mb-2">Projects Created</div>
          <div className="text-4xl font-bold text-white">4</div>
        </motion.div>
      </div>
    </div>
  )
}
