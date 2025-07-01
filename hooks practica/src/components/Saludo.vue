<template>
  <div>
    <h2>👋 ¡Hola Julieta!</h2>
  </div>
</template>

<script setup>
import { onMounted, onUnmounted } from "vue";

onMounted(() => {
  console.log("✅ El componente Saludo fue montado.");
});

onUnmounted(() => {
  console.log("❌ El componente Saludo fue desmontado.");
});
</script>
