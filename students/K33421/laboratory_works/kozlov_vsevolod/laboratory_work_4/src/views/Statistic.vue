<template>
  <h1>Стастистика</h1>

  <h2>Возраст посетителей</h2>
  <div v-if="ageStat">
    <ul>
      <li>До 20 лет: {{ ageStat.under_20 }}</li>
      <li>После 20 лет: {{ageStat.after_20}}</li>
    </ul>
  </div>

  <h2>Образование посетителей</h2>
  <div v-if="educationStat">
    <ul>
      <li>Начальное: {{educationStat.beginner}}</li>
      <li>Среднее: {{educationStat.middle}}</li>
      <li>Высшее: {{educationStat.higher}}</li>
      <li>Ученая степень: {{educationStat.degree}}</li>
    </ul>
  </div>

  <div>
    Начальная дата
    <input type="date" v-model="dateAfter" :max="getCurrentDate" :min="'2000-01-01'">
  </div>
  <div>
    Конечная дата
    <input type="date" v-model="dateBefore" :max="getCurrentDate" :min="'2000-01-01'">
  </div>

  <h2>Статистика библиотеки</h2>
  <div v-if="libStat">
    <ul>
      <li>Книг взято: {{libStat.books_taken}}</li>
      <li>Новых читателей: {{libStat.new_readers}}</li>
    </ul>
  </div>

  <h2>Статистика по читательским залам</h2>
  <div v-if="roomStat">
    <div v-for="room in roomStat">
      <h3>{{room.name}}</h3>
      <ul>
        <li>Книг взято: {{room.books_taken}}</li>
        <li>Новых читателей: {{room.new_readers}}</li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import {ref, onMounted, computed, watch} from "vue"
import {fetchData} from "@/tools"


const ageStat = ref(null)
const educationStat = ref(null)
const dateAfter = ref('2000-01-01');
const libStat = ref(null)
const roomStat = ref(null)

const filename = 'Statistics'


const dateBefore = ref(new Date().toISOString().split('T')[0]);
const getCurrentDate = computed(() => {
  return new Date().toISOString().split('T')[0];
})

async function fetchConstData(){
  ageStat.value = await fetchData(
      'http://127.0.0.1:8000/lab3/statistics/age',
      filename
  )

  educationStat.value = await fetchData(
      'http://127.0.0.1:8000/lab3/statistics/education',
      filename
  )
  console.log(educationStat.value)
}

async function fetchVarData(){
  let config = {
    params:
        {date_before: dateBefore.value,
          date_after:dateAfter.value}
  }
  libStat.value = await fetchData(
      'http://127.0.0.1:8000/lab3/statistics/library',
      filename,
      config
  )
  roomStat.value = await fetchData(
      'http://127.0.0.1:8000/lab3/statistics/room/list',
      filename,
      config
  )
}

watch([dateAfter, dateBefore], async() => await fetchVarData())

onMounted(() =>{
  fetchConstData().then()
  fetchVarData().then()
})

</script>

<style scoped>

</style>