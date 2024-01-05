<template>
  <div v-for="reader in readers" :key="reader.id">
    <h2>{{`${reader.first_name} ${reader.last_name}`}}</h2>
    <ul>
      <li>{{`reader number: ${reader.reader_number}`}}</li>
      <li>{{`registration date: ${reader.registration_date}`}}</li>
      <li>{{`active : ${reader.active}`}}</li>
      <li>{{`passport number: ${reader.passport_number}`}}</li>
      <li>{{`birth date : ${reader.birth_date}`}}</li>
      <li>{{`address : ${reader.address}`}}</li>
      <li>{{`mobile number: ${reader.mobile_number}`}}</li>
    </ul>
  </div>
</template>

<script setup>
import {onMounted, ref} from "vue";
import axios from "axios";

const props = defineProps({
  url:{ type:String, required: true}
})

const readers = ref(null);
async function fetchReaderRareBooks(){
  try {
    const response = await axios.get(props.url)
    readers.value = response.data
  } catch (e){
    alert(`Ошибка при общращении к api: ${props.url}`)
  }
}
onMounted(()=>{
  fetchReaderRareBooks()
})

</script>

<style scoped>

</style>