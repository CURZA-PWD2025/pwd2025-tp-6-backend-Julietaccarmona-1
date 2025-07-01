<script setup lang="ts">
import type { Zapatilla } from "../interfaces/Zapatilla";

const props = defineProps<{ pzapatilla: Zapatilla }>();
</script>

<template>
  <div class="zapatilla">
    <h2>{{ props.pzapatilla.descripcion }}</h2>
    <p>Precio: ${{ props.pzapatilla.precio }}</p>
    <img
      :src="'/imgs/' + props.pzapatilla.foto"
      :alt="props.pzapatilla.descripcion"
      width="200"
    />
  </div>
</template>
