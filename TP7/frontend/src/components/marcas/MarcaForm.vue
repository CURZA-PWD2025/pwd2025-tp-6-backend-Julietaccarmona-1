<script setup lang="ts">
import { ref, watch, computed } from "vue";
import { useMarcasStore } from "@/stores/marcasStore";

const store = useMarcasStore();

const desc = ref("");
watch(
  () => store.actual,
  (val) => { desc.value = val ? val.descripcion : ""; }
);

const modoEdicion = computed(() => !!store.actual);

const guardar = async () => {
  if (!desc.value.trim()) return;

  if (modoEdicion.value) {
    await store.update(store.actual!.id, { descripcion: desc.value });
    store.actual = null;        // salir de edición
  } else {
    await store.create({ descripcion: desc.value });
  }
  desc.value = "";
};

const cancelar = () => {
  store.actual = null;
  desc.value = "";
};
</script>

<template>
  <h2 class="text-xl font-semibold mb-2">
    {{ modoEdicion ? "Editar Marca" : "Nueva Marca" }}
  </h2>

  <div class="mb-4">
    <input v-model="desc" class="border p-2 mr-2" placeholder="Descripción" />
    <button @click="guardar" class="bg-green-600 text-white px-3 py-2 rounded">
      {{ modoEdicion ? "Actualizar" : "Agregar" }}
    </button>
    <button v-if="modoEdicion" @click="cancelar" class="ml-2 px-3 py-2 border rounded">
      Cancelar
    </button>
  </div>
</template>
