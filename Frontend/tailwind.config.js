// tailwind.config.js (or .mjs)
import daisyui from 'daisyui'; // <-- ES Module import at the top

/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./test.html",
    "./learn_more.html",
    "./dashboard.html",
    "./src/**/*.{js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    daisyui, // <-- Reference the imported variable
  ],
  daisyui: {
    themes: ["light", "dark", "cupcake"],
  },
}
