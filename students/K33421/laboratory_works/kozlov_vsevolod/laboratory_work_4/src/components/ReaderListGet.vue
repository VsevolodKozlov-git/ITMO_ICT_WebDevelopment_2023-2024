<template>
  <div class="container align-items-center">
    <div class="card" v-for="(reader, id) in readers">
      <div class="card-header">
        <button class="btn btn-light" data-bs-toggle="collapse" :data-bs-target="`#collapseUser${id}`">
          {{`${reader.first_name} ${reader.last_name}`}}
        </button>
      </div>
      <div :id="`collapseUser${id}`" class="collapse" data-bs-parent="#accordionExample">
        <div class="card-body">
          <table class="table table-responsive">
            <thead>
            <tr>
              <th scope="col">Поле</th>
              <th scope="col">Значение</th>
            </tr>
            </thead>
            <tbody>
            <tr>
              <td>Читательский номер</td>
              <td>{{reader.reader_number}}</td>
            </tr>
            <tr>
              <td>Дата регистрации</td>
              <td>{{reader.registration_date}}</td>
            </tr>
            <tr>
              <td>Активен</td>
              <td>{{reader.active}}</td>
            </tr>
            <tr>
              <td>Пасспорт</td>
              <td>{{reader.passport_number}}</td>
            </tr>

            <tr>
              <td>Дата рождения</td>
              <td>{{reader.birth_date}}</td>
            </tr>
            <tr>
              <td>Адрес</td>
              <td>{{reader.address}}</td>
            </tr>
            <tr>
              <td>Номер телефона</td>
              <td>{{reader.mobile_number}}</td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
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