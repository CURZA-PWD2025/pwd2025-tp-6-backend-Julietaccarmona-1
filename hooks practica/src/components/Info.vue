<template>
    <div class="info-box">
      <p>{{ mensaje }}</p>
    </div>
  </template>
  
  <script setup>
  defineProps({
    mensaje: String
  });
  </script>
  
  <style scoped>
  .info-box {
    margin: 1rem 0;
    padding: 1rem;
    background-color: #fff;
    border-radius: 8px;
    color: #333;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  }
  </style>
  