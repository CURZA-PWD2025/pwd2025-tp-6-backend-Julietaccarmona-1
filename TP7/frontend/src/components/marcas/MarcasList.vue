<script setup lang="ts">
import { onMounted } from "vue";
import { useMarcasStore } from "@/stores/marcasStore";

const store = useMarcasStore();
onMounted(store.fetchAll);

const editar = (marcaId: number) => {
  // Lanzás evento al padre
  store.fetchOne(marcaId);
};
const borrar = async (marcaId: number) => {
  if (confirm("¿Eliminar la marca?")) await store.remove(marcaId);
};
</script>

<template>
  <h2 class="text-xl font-semibold mb-4">Listado de Marcas</h2>

  <table class="border w-full">
    <thead class="bg-gray-100">
      <tr><th>ID</th><th>Descripción</th><th>Acciones</th></tr>
    </thead>
    <tbody>
      <tr v-for="m in store.lista" :key="m.id" class="hover:bg-gray-50">
        <td class="border p-1 text-center">{{ m.id }}</td>
        <td class="border p-1">{{ m.descripcion }}</td>
        <td class="border p-1 text-center">
          <button @click="editar(m.id)"  class="px-2 text-blue-600">✏️</button>
          <button @click="borrar(m.id)"  class="px-2 text-red-600">🗑️</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>
