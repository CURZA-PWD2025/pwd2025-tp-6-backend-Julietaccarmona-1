<template>
  <div>
    <button @click="mostrar = !mostrar">
      {{ mostrar ? "Ocultar componente" : "Mostrar componente" }}
    </button>

    <Saludo v-if="mostrar" />

    <Info mensaje="Mostrá este mensajito por mí, por fa 🙏" />
    <Info mensaje="¡Hola Julieta! Esto también viene del componente padre 👩‍💻" />
  </div>
</template>

<script setup>
import { ref } from "vue";
import Saludo from "./components/Saludo.vue";
import Info from "./components/Info.vue";

const mostrar = ref(true);
</script>

<style>
body {
  margin: 0;
  padding: 0;
  font-family: sans-serif;
  background: linear-gradient(transparent, #aa0c9d);
}

.pagina {
  max-width: 600px;
  margin: 2rem auto;
  padding: 1rem;
}
</style>
