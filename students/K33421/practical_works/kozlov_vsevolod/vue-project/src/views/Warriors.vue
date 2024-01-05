<template>
  <div class="app">
    <h1>Портал информации о войнах в онлайн РПГ</h1>
    <button @click="fetchWarriors">Получить список войнов</button> <!-- Кнопка вызывает функцию получения списка данных (функция fetchWarriors объявлена в блоке "methods") -->
    <warrior-form/> <!-- Встраивание компонента формы -->
    <warrior-list
        :warriors="warriors"
    /> <!-- Встраивание компонента вызывающего список объектов. v-bind - директива служит для так называемой data binding -- привязки данных (данные объявляются в блоке данных data() (см. код ниже)). -->
  </div>
</template>

<script setup>
import WarriorForm from "@/components/WarriorForm.vue";
import WarriorList from "@/components/WarriorList.vue";
import {ref, onMounted} from "vue"
import axios from "axios";


const warriors = ref(null);

async function fetchWarriors () { // асинхронная функция для получения данных
  try {
    // throw new Error('error');
    const response = await axios.get('http://127.0.0.1:8000/lab3/warriors/list') // Выполнение GET-запроса Backend-серверу. Запрос вернет JSON.
    warriors.value = response.data // Массив данных warriors из блока(функции) data() получает значением результат только-что выполненного запроса
  } catch (e) {
    alert('Ошибка')
    warriors.value = [
        {name: 'Сева', race: 'Кавказец'},
        {name: 'Коля', race: 'Русский'}
    ]
  }
}

onMounted(() => fetchWarriors())
</script>

