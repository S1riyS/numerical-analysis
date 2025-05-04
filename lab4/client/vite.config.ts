import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path';

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@common': resolve(__dirname, './src/modules/common'),
      '@approximation': resolve(__dirname, './src/modules/approximation'),
      '@interpolation': resolve(__dirname, './src/modules/interpolation'),
      '/src': resolve(__dirname, './src')
    },
  },
})
