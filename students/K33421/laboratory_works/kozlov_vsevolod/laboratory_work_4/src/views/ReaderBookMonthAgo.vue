<template>
  <h2>Список пользователей, которые взяли книгу больше месяца назад</h2>
  <ReaderListGet :url="url"/>
</template>

<script setup>
import ReaderListGet from "@/components/ReaderListGet"
const url = "http://127.0.0.1:8000/lab3/reader/book_month_ago"
</script>

<style scoped>

</style>