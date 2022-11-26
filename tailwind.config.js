/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html", "./templates/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        "green-dark" : "#61892F", 
        "green-light" : "#86C232", 
        "gray-light" : "#6B6E70",
        "green-light" : "##34D399",
        "cream-red" : "#FF7D7D",
        "better-gray" : "#2E2E32"
      },
      fontFamily : {
        "primary" : "Rubik, sans-serif",
      }
    },
  },
  plugins: [],
}
