import { motion } from 'framer-motion'

export default function FeatureCard({ feature, index }) {
  const Icon = feature.icon

  return (
    <motion.div
      initial={{ opacity: 0, x: -50 }}
      animate={{ opacity: 1, x: 0 }}
      transition={{ delay: index * 0.05, type: 'spring', stiffness: 200 }}
      whileHover={{ 
        scale: 1.02,
        borderColor: 'rgba(184, 184, 255, 0.3)',
        transition: { type: 'spring', stiffness: 300, damping: 20 }
      }}
      className="glass rounded-2xl p-6 border border-white/10 cursor-pointer group relative overflow-hidden"
    >
      {/* Subtle flow on hover */}
      <motion.div 
        className="absolute inset-0 opacity-0 group-hover:opacity-100"
        style={{
          background: 'linear-gradient(90deg, transparent 0%, rgba(184, 184, 255, 0.05) 50%, transparent 100%)',
          backgroundSize: '200% 100%',
        }}
        animate={{
          backgroundPosition: ['0% 0%', '200% 0%'],
        }}
        transition={{ duration: 2, repeat: Infinity, ease: 'linear' }}
      />

      {/* Icon with minimal styling */}
      <div className="w-14 h-14 rounded-xl bg-zephyr-gray border border-white/10 flex items-center justify-center mb-4 shadow-lg group-hover:border-zephyr-accent/30 transition-all relative z-10">
        <Icon className="w-7 h-7 text-zephyr-silver" />
      </div>

      {/* Content */}
      <h3 className="text-lg font-bold text-white mb-2 relative z-10 group-hover:text-zephyr-accent transition-colors">{feature.title}</h3>
      <p className="text-white/50 text-sm mb-4 relative z-10">{feature.description}</p>

      {/* Examples - clean and simple */}
      <div className="space-y-2 relative z-10">
        {feature.examples.map((example, i) => (
          <motion.div 
            key={i} 
            className="text-xs text-zephyr-silver/60 font-mono bg-zephyr-gray/50 border border-white/5 px-3 py-1.5 rounded-lg group-hover:border-zephyr-accent/20 transition-colors"
            whileHover={{ x: 3 }}
          >
            <span className="text-zephyr-accent">→</span> {example}
          </motion.div>
        ))}
      </div>

      {/* Corner accent - minimal */}
      <div className="absolute bottom-0 right-0 w-12 h-12 opacity-0 group-hover:opacity-100 transition-opacity">
        <div className="absolute bottom-0 right-0 w-full h-px bg-gradient-to-l from-zephyr-accent to-transparent" />
        <div className="absolute bottom-0 right-0 w-px h-full bg-gradient-to-t from-zephyr-accent to-transparent" />
      </div>
    </motion.div>
  )
}
