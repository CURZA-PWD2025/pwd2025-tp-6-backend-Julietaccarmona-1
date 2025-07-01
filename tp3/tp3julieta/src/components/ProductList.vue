<script setup lang="ts">
import type { Zapatilla } from "../interfaces/Zapatilla";
import { zapatillas } from "../data/zapatillas.ts";
import ItemList from "./ItemList.vue";
import { ref } from "vue";

const productos = ref<Zapatilla[]>(zapatillas);
</script>

<template>
  <div class="product-list">
    <ItemList
      v-for="zapatilla in productos"
      :key="zapatilla.id"
      :pzapatilla="zapatilla"
    />
  </div>
</template>

<style scoped>
.product-list {
  font-size: 20px;
  font-family: sans-serif;
  width: 1280px;
  height: 100%;
  margin: 0 auto;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  padding: 80px;
  border: 2px dashed rgb(179, 184, 184);
  border-radius: 10px;
  background-color: #f5f5f5;
}
</style>
