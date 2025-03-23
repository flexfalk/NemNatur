<script setup>
</script>

<template>
  <div>
    <header class="header">
      <div class="logo">
        <img src="/logo.jpg" alt="NemNatur Logo" />
      </div>
      <nav>
        <ul>
          <li><router-link to="/">Startside</router-link></li>
          <li><router-link to="/products">Aktiviteter</router-link></li>
          <li><router-link to="/about">Hvem er vi</router-link></li>
          <li><router-link to="/contact">Kontakt</router-link></li>
        </ul>
      </nav>
    </header>

    <main>
      <router-view></router-view>
    </main>
  </div>
</template>

<style scoped>
/* Global Styles */
body {
  font-family: 'Poppins', sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f5f5f5;
  color: #333;
}

/* Header Styles */
.header {
  background-color: #2c3e50;
  padding: 40px 0; /* Increased the padding to make the header taller */
  display: flex;
  justify-content: center; /* Center the content */
  align-items: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 1000;
  position: relative;
  border: none; /* Remove any borders around the header */
}

.header .logo {
  position: absolute;
  left: 10%; /* Push the logo slightly to the right */
}

.header .logo img {
  width: 120px;
  height: auto;
  border-radius: 8px;
  transition: transform 0.3s ease;
}

.header .logo img:hover {
  transform: scale(1.1);
}

nav ul {
  list-style: none;
  padding: 0;
  display: flex;
  justify-content: center;
  margin-top: 0;
}

nav ul li {
  margin: 0 25px;
}

nav ul li a {
  color: white;
  text-decoration: none;
  font-size: 18px;
  font-weight: 600;
  text-transform: uppercase;
  transition: color 0.3s ease;
}

nav ul li a:hover {
  color: #ffeb3b;
}

/* Main Content */
main {
  padding: 30px;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  margin-top: 20px;
}

h1, h2 {
  font-weight: 600;
}

/* Buttons */
button {
  background-color: #2c3e50;
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #34495e;
}
</style>
