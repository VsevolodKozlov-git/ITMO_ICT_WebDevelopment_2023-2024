<template>
  <form @submit.prevent> <!-- @submit.prevent позволяет остановить перезагрузку страницы после нажатия кнопки -->
    <h1>Создание война</h1>
    <input
        v-model="warrior.name"
        class="input"
        type="text"
        placeholder="Имя"> <!-- Вызывает форму, при нажатии кнопки "Создать", "warrior.name" получит значение из формы -->
    <input
        v-model="warrior.race"
        class="input"
        type="text"
        placeholder="Расса">
    <button class="btn" @click="createWarrior">Cоздать</button> <!-- Нажатие кнопки "Создать" вызывает метод "createWarrior" и записывает данные в объект "warrior" -->
  </form>
</template>

<script setup>
import {ref} from "vue";
import axios from "axios";

const warrior = ref({name: '', race: ''})

function createWarrior() {
  axios.post('http://62.109.28.95:8890/warrior/create1', {
    race: warrior.value.race,
    name: this.warrior.value.name,
  })
  warrior.value.name = ''
  warrior.value.race = ''
}

</script>

<style scoped>

</style>