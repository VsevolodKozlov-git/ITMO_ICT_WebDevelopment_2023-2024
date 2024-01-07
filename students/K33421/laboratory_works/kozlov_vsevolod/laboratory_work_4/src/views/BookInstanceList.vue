<template>
  <div class="container">

    <div class="card" v-for="(book, key, id) in bookDict">
      <div class="card-header">
        <button class="btn btn-light" data-bs-toggle="collapse" :data-bs-target="`#collapseUser${id}`">
          {{`"${book.title}" ${book.authors} ${book.year}`}}
        </button>
      </div>
      <div :id="`collapseUser${id}`" class="collapse" data-bs-parent="#accordionExample">
        <div class="card-body">
          <table class="table table-responsive">
            <thead>
            <tr>
              <th scope="col">Код</th>
              <th scope="col">Качество</th>
              <th scope="col">Зал</th>
              <th scope="col"></th>
              <th scope="col"></th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="instance in book.instances">
              <td>{{instance.code}}</td>
              <td>{{instance.quality}}</td>
              <td>{{instance.room}}</td>
              <td>
                <button class="btn btn-light" @click="goToUpdatePage(instance.id)">Изменить</button>
              </td>
              <td>
                <button class="btn btn-light" @click="deleteInstance(instance.id)">Удалить</button>
              </td>

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
import {fetchData, deleteData} from "@/tools";
import router from "@/router";

const fileName = 'BookInstancesList.vue'
const bookDict = ref({})

async function getBookInstances(){
  const instancesList= await fetchData(
      'http://127.0.0.1:8000/lab3/book_instance/list',
      fileName)
  writeInBookDict(instancesList)
}

function writeInBookDict(instancesList){
  for (const instance of instancesList){
    const book = instance.book
    if (!(book.id in bookDict.value)) {
      bookDict.value[book.id] = {
        title: book.title,
        publisher: book.publisher,
        authors: authorsToStr(book.authors),
        year: book.year,
        instances: [],
        visible: false
      }
    }
   bookDict.value[book.id].instances.push({
     'code': instance.code,
     'quality': instance.quality,
     'room': instance.room,
     'id': instance.id
   })
  }

  function authorsToStr(authorsArr){
    let authorsStr = ''
    for (const author of authorsArr){
      authorsStr += `${author.first_name} ${author.last_name}, `
    }
    // Убираем запятую и пробел в конце
    if (authorsStr){
      authorsStr = authorsStr.slice(0, -2)
    }
    return authorsStr
  }
}

function deleteInstance(instanceId){
  // delete from db
  deleteData(
      `http://127.0.0.1:8000/lab3/book_instance/remove/${instanceId}`,
      fileName
  )
  // delete from dict
  for (const book of Object.values(bookDict.value)){
    book.instances = book.instances.filter((instance) => instance.id !== instanceId)
  }
}

function goToUpdatePage(instanceId){
  router.push(`/book_instance/update/${instanceId}`)
}

onMounted(async()=>{
  await getBookInstances()
})
</script>

<style scoped>
.book_title:hover {
  color: red;
}
</style>