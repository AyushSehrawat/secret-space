/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html", "./templates/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        "green-dark" : "#61892F",
        "green-light" : "#86C232",
        "gray-light" : "#6B6E70"
      },
      fontFamily : {
        "primary" : "Rubik, sans-serif",
      }
    },
  },
  plugins: [],
}
