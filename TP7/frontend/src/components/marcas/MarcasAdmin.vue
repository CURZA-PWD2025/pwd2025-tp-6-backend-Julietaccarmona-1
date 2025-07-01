<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useMarcasStore } from "@/stores/marcasStore";

const store = useMarcasStore();
const descripcion = ref("");

onMounted(store.fetchAll);
const crear = async () => {
  if (descripcion.value.trim()) {
    await store.create({ descripcion: descripcion.value });
    descripcion.value = "";
  }
};
</script>

<template>
  <h2 class="text-xl font-semibold mb-4">Marcas</h2>

  <div class="mb-4">
    <input v-model="descripcion" placeholder="Nueva marca" class="border p-2 mr-2" />
    <button @click="crear" class="px-3 py-2 bg-blue-600 text-white rounded">Agregar</button>
  </div>

  <table class="w-full border">
    <thead><tr><th>ID</th><th>Descripción</th></tr></thead>
    <tbody>
      <tr v-for="m in store.lista" :key="m.id">
        <td class="border p-1">{{ m.id }}</td>
        <td class="border p-1">{{ m.descripcion }}</td>
      </tr>
    </tbody>
  </table>
</template>
<style scoped></style>