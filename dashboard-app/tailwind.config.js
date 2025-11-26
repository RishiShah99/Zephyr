/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'zephyr-black': '#0a0a0f',
        'zephyr-dark': '#121218',
        'zephyr-gray': '#1a1a24',
        'zephyr-silver': '#e0e0e8',
        'zephyr-accent': '#b8b8ff', // Soft purple - for actions
        'zephyr-accent-dim': '#6b6b9f',
      },
      backgroundImage: {
        'zephyr-gradient': 'linear-gradient(135deg, #0a0a0f 0%, #121218 50%, #0a0a0f 100%)',
      },
      animation: {
        'flow': 'flow 3s ease-in-out infinite',
        'gust': 'gust 2s ease-in-out infinite',
      },
      keyframes: {
        'flow': {
          '0%, 100%': { transform: 'translateX(0) translateY(0)' },
          '50%': { transform: 'translateX(20px) translateY(-10px)' },
        },
        'gust': {
          '0%, 100%': { opacity: 0 },
          '50%': { opacity: 0.3 },
        },
      },
    },
  },
  plugins: [],
}
