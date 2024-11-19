/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors:{
        sendColor:'#86efac',
        receivedColor:'#fff',
        selected:'#515050'
      }
    },
  },
  plugins: [],
}