<template>
  <div class="p-4 max-w-xl mx-auto">
    <MarcaForm />
    <hr class="my-4" />
    <MarcasList />
  </div>
</template>

<script setup lang="ts">
import MarcaForm   from "@/components/marcas/MarcaForm.vue";
import MarcasList  from "@/components/marcas/MarcasList.vue";
</script>
