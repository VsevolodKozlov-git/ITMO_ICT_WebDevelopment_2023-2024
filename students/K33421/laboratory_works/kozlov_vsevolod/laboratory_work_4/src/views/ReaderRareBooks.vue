<template>
  <h2>Список пользователей, которые имеют книги с кольчеством экземпляров не больше 2-х</h2>
  <ReaderListGet :url="url"/>
</template>

<script setup>
import ReaderListGet from "@/components/ReaderListGet"
const url = 'http://127.0.0.1:8000/lab3/reader/rare_books'
</script>

<style scoped>

</style>