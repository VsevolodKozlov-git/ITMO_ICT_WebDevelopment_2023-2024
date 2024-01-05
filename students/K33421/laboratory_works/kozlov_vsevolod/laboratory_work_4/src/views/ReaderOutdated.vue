<template>
  <h1>Список пользователей, которые не прошли перерегистрацию</h1>
  <ReaderListGet :url="url"/>
</template>

<script setup>
import ReaderListGet from "@/components/ReaderListGet"
const url = "http://127.0.0.1:8000/lab3/reader/outdated"
</script>

<style scoped>

</style>