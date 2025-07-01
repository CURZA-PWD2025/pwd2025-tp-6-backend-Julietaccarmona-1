<script lang="ts">
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

<style scoped>
/* Estilos para la barra de navegación */
.navbar {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f5f5f5;
  padding: 1rem 2rem;
  border-radius: 20px;
  margin: 2rem auto;
  max-width: 800px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  gap: 2rem;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
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
  background-color: #dbeafe; /* azul suave */
  color: #1d4ed8;
}

.navbar a.router-link-exact-active {
  background-color: #1d4ed8;
  color: white;
  font-weight: bold;
}

/* Adaptable para pantallas grandes */
@media (min-width: 1024px) {
  header {
    display: flex;
    justify-content: center;
  }
}
</style>
