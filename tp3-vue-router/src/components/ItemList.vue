<template>
  <div class="zapatilla">
    <h2>{{ pzapatilla.descripcion }}</h2>
    <p>Precio: ${{ pzapatilla.precio }}</p>
    <img
      :src="'/imgs/' + pzapatilla.foto"
      :alt="pzapatilla.descripcion"
      width="200"
    />
  </div>
</template>

<script setup lang="ts">
import type { Zapatilla } from "../interfaces/Zapatilla";

const props = defineProps<{ pzapatilla: Zapatilla }>();
</script>
