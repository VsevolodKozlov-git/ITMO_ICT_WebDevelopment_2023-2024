<template>
  <h1>Изменение экземпляра книги</h1>
  <form @submit.prevent>
    <FormInputs :fields-arr="instanceForm"></FormInputs>
    <button @click="updateBookInstance">Изменить</button>
    <div v-if="instanceUpdated">
      Экземпляр обновлен
    </div>
  </form>
</template>

<script setup>
import {ref, onMounted} from "vue"
import {fetchData, patchData} from "@/tools";
import FormInputs from "@/components/FormInputs"
import {useRoute} from "vue-router";

const route = useRoute();


const instanceForm = ref({
  code: {value: '', error_msg: '', type: 'text', label: 'Код'},
  quality: {value: '', error_msg: '', type: 'text', label: 'Качество'},
  room: {value: '', error_msg: '', type: 'number', label: 'Зал'},
})
const filename='BookInstanceUpdate'
const instanceId = route.params.pk
const instanceUpdated = ref(false);

async function writeValueInInstanceForm(){
  const data =  await fetchData(
      `http://127.0.0.1:8000/lab3/book_instance/${instanceId}`,
      filename
  )
  instanceForm.value.code.value = data.code
  instanceForm.value.quality.value = data.quality
  instanceForm.value.room.value = data.room
}

function updateBookInstance(){
  instanceUpdated.value = false;
  let errorFlag = false;

  function validateField(field, is_error, error_msg){
    if (is_error){
      field.error_msg = error_msg
      errorFlag = true
    }
    else{
      field.error_msg = ''
    }
  }

  let field = instanceForm.value.code
  let is_error = field.value.length > 10
  let error_msg = 'code number should be <= 10 chars'
  validateField(field, is_error, error_msg)

  field = instanceForm.value.quality
  is_error = !(['b', 'g', 'n'].includes(field.value))
  error_msg = 'quality should be one of ["b", "g", "n"]'
  validateField(field, is_error, error_msg)

  field = instanceForm.value.room
  is_error = !([1, 2].includes(field.value))
  error_msg = 'room should be either 1 or 2'
  validateField(field, is_error, error_msg)
  if (errorFlag){
    return;
  }

  let data = {};
  for (let key in instanceForm.value){
    data[key] = instanceForm.value[key].value
  }

  (async() =>{
    await patchData(
        `http://127.0.0.1:8000/lab3/book_instance/update/${instanceId}`,
        filename,
        data)
  })()
  instanceUpdated.value = true;
}

onMounted(
    async()=>{
      await writeValueInInstanceForm()
    }
)



</script>

<style scoped>

</style>