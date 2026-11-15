/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,ts}",
  ],
  theme: {
    extend: {
      colors: {
        tila: {
          dark: '#0B0B14',
          surface: '#131326',
          card: 'rgba(23, 23, 46, 0.7)',
          accent: '#7C3AED',
          lightViolet: '#A855F7',
          glow: '#6366F1',
          cyanGlow: '#38BDF8',
          textMuted: '#94A3B8'
        }
      },
      backgroundImage: {
        'hero-gradient': 'radial-gradient(ellipse at 50% -20%, rgba(124, 58, 237, 0.35), rgba(11, 11, 20, 0.95))',
        'glow-radial': 'radial-gradient(circle, rgba(168, 85, 247, 0.25) 0%, rgba(11, 11, 20, 0) 70%)',
        'card-gradient': 'linear-gradient(135deg, rgba(255, 255, 255, 0.07) 0%, rgba(255, 255, 255, 0.02) 100%)',
        'badge-gradient': 'linear-gradient(90deg, rgba(124, 58, 237, 0.4), rgba(56, 189, 248, 0.4))',
        'button-gradient': 'linear-gradient(90deg, #7C3AED 0%, #A855F7 100%)',
      },
      boxShadow: {
        'glow-violet': '0 0 40px -10px rgba(124, 58, 237, 0.5)',
        'glow-cyan': '0 0 40px -10px rgba(56, 189, 248, 0.5)',
        'glass-edge': 'inset 0 1px 1px 0 rgba(255, 255, 255, 0.15)',
      },
      animation: {
        'pulse-slow': 'pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'float': 'float 6s ease-in-out infinite',
        'glow-spin': 'glowSpin 10s linear infinite',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-12px)' },
        },
        glowSpin: {
          '0%': { transform: 'rotate(0deg)' },
          '100%': { transform: 'rotate(360deg)' },
        }
      }
    },
  },
  plugins: [],
}
