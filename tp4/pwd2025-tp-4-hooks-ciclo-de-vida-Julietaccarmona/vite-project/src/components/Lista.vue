<script setup>
import { ref, onMounted } from "vue";
import profesionesData from "../resources/profesiones";

const profesiones = ref([]);

onMounted(() => {
  setTimeout(() => {
    profesiones.value = profesionesData;
  }, 3000);
});
</script>

<template>
  <div>
    <h2>Lista de profesiones</h2>
    <ul>
      <li v-for="item in profesiones" :key="item.id">
        <strong>{{ item.nombre }}</strong
        >: {{ item.descripcion }}
      </li>
    </ul>
  </div>
</template>

<style scoped>
h2 {
  color: #555454;
}

ul {
  list-style-type: none;
  text-align: justify;
  line-height: 2;
}

li {
  margin: 5px 0;
  border-style: solid;
  padding: 10px 20px;
  background: linear-gradient(to right, rgb(189, 189, 189), transparent);
}
</style>
