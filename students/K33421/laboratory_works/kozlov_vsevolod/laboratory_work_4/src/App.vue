<template>
  <router-link to="/reader/rare_books">Rare books</router-link>
  <br>
  <router-link to="/reader/outdated">Outdated</router-link>
  <br>
  <router-link to="/reader/book_month_ago">BookMonthAgo</router-link>
  <br>
  <router-view></router-view>
</template>

<script setup>

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
