<script setup>
import Lista from "./components/Lista.vue";
import Tareas from "./components/Tareas.vue";
import DimensionComponente from "./components/DimensionComponente.vue";

import { ref } from "vue";

const currentComponent = ref("Lista");

const componentes = {
  Lista: Lista,
  Tareas: Tareas,
  Dimensiones: DimensionComponente,
};
</script>

<template>
  <div>
    <h1>TP4 Hooks</h1>
    <button @click="currentComponent = 'Lista'">Ver Lista</button>
    <button @click="currentComponent = 'Tareas'">Ver Tareas</button>
    <button @click="currentComponent = 'Dimensiones'">Ver Dimensiones</button>

    <component :is="componentes[currentComponent]" />
  </div>
</template>

<style>
h1 {
  color: #ffffff;
  text-shadow: black 2px 2px 4px;
  border: 2px dashed #5c5c5c;
  border-radius: 20px;
  padding: 10px;
  text-align: center;
  background-color: #d3d3d3;
  font-family: "Courier New", Courier, monospace;
  padding: 10px 20px;
  margin: 20px auto;
  width: fit-content;
}
</style>
