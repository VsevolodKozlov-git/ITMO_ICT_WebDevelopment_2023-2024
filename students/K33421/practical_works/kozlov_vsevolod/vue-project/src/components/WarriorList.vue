<template>
  <div class="warrior" v-for="warrior in warriors"> <!-- v-for - директива для отображения списка элементов на основе массива. -->
    <div><strong>Имя:</strong> {{ warrior.name }}</div>
    <div><strong>Расса:</strong> {{ warrior.race }}</div>
  </div>
</template>

<script setup>
defineProps({warriors: {
    type: Array,
    required: true
  }})
</script>

<style scoped>

</style>