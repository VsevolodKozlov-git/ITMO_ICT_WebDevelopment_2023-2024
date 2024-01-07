<template>
  <ul v-if="errorMsgs" class="error">
    Ошибка:
    <li v-for="errorMsg in errorMsgs">
      {{errorMsg}}
    </li>
  </ul>
</template>

<script setup>
defineProps({
  errorMsgs:{
    required: true,
    type: Array
  }
})
</script>

<style scoped>

</style>