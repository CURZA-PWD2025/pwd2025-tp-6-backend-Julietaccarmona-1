<script lang="ts" setup>
import { RouterView, RouterLink } from "vue-router";
</script>

<template>
  <div>
    <header>
      <nav class="navbar">
        <RouterLink to="/">Sobre nosotros</RouterLink>
        <RouterLink to="/contacto">Contacto</RouterLink>
        <RouterLink to="/producto">Productos</RouterLink>
      </nav>
    </header>

    <main>
      <RouterView />
    </main>
  </div>
</template>

<style>
html,
body,
#app {
  height: 100%;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
</style>

<style scoped>
header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  background-color: #f5f5f5;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

main {
  margin-top: 80px; 
  padding: 2rem;
}

.navbar {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  gap: 2rem;
}

.navbar a {
  text-decoration: none;
  color: #333;
  font-weight: 500;
  font-size: 1.1rem;
  padding: 0.5rem 1rem;
  border-radius: 12px;
  transition: background-color 0.3s, color 0.3s;
}

.navbar a:hover {
  background-color: #dbeafe; 
  color: #1d4ed8;
}

.navbar a.router-link-exact-active {
  background-color: #3bdbce;
  color: white;
  font-weight: bold;
}
</style>
