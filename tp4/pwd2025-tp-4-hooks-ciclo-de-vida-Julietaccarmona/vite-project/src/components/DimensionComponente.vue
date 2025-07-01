<script setup>
import { ref, onMounted, onUnmounted } from "vue";

const width = ref(window.innerWidth);
const height = ref(window.innerHeight);

const actualizarDimensiones = () => {
  width.value = window.innerWidth;
  height.value = window.innerHeight;
};

onMounted(() => {
  window.addEventListener("resize", actualizarDimensiones);
});

onUnmounted(() => {
  window.removeEventListener("resize", actualizarDimensiones);
});
</script>

<template>
  <div>
    <h2>Dimensiones del componente</h2>
    <p>Ancho: {{ width }} px</p>
    <p>Alto: {{ height }} px</p>
  </div>
</template>

<style scoped>
h2 {
  color: #555454;
}

p {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}
</style>
