<template>
  <h1>Экземлпяры книг</h1>

  <div>
    Нажмите на книгу, экземпляры которой вы хотите просмотреть
  </div>

  <div v-if="bookDict">
    <div v-for="book in bookDict" :key="book">
      <h3 class="book_title" @click="book.visible = !book.visible">
        {{`"${book.title}" ${book.authors} ${book.year}`}}
      </h3>
<!--      <button @click="book.visible = !book.visible">Экземпляры</button>-->
      <ul v-if="book.visible">
        <li v-for="instance in book.instances">
          {{`код: ${instance.code}; качество:${instance.quality}; зал:${instance.room}`}}
          <button @click="deleteInstance(instance.id)">Удалить</button>
        </li>
      </ul>
    </div>
  </div>

</template>

<script setup>
import {onMounted, ref} from "vue";
import {fetchData, deleteData} from "@/tools";

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

// todo put method

onMounted(async()=>{
  await getBookInstances()
})
</script>

<style scoped>
.book_title:hover {
  color: red;
}
</style>