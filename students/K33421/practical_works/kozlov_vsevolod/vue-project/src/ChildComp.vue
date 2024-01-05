<script setup>
const emit = defineEmits(['hello'])

emit('hello', 'hello from child')
</script>

<template>
  <h2>Child component</h2>
</template>