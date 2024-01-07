<template>
  <div v-if="authorizationError">
    Авторизируйтесь прежде чем изменять данные пользователя
  </div>
  <div v-else>
    <form @submit.prevent class="container">
      <FormInputs :fields-arr="formDict"/>
      <button class="btn btn-primary" @click="updateUserData">Обновить данные</button>
      <ListErrorMsgs :error-msgs="formErrorMsgs"/>
      <div v-if="formSuccess">
        Данные обновлены
      </div>
    </form>
  </div>
</template>

<script setup>
import {onMounted, ref} from "vue";
import axios from "axios";
import FormInputs from '@/components/FormInputs'
import {formDictToData, userSendErrorCatch, removerErrorMsgs} from "@/tools";
import ListErrorMsgs from "@/components/ListErrorMsgs"

const formDict = ref({
  first_name: {value: '', error_msg: '', type: 'text', label: 'Имя'},
  last_name: {value: '', error_msg: '', type: 'text', label: 'Фамилия'},
  email: {value: '', error_msg: '', type: 'email', label: 'email'}
})

const authorizationError = ref(false)
const formErrorMsgs = ref(false)
const formSuccess = ref(false)

function writeDataToDict(){
  axios.get(
      'http://127.0.0.1:8000/auth/users/me/'
  ).catch((e)=>{
    let errorResolved = false

    if (e.response){
      if (e.response.status === 401) {
        authorizationError.value = true
        errorResolved = true
      }
    }

    if (!errorResolved){
      throw e
    }
  }).then((response)=>{
    if (response){
      const data  = response.data
      formDict.value.first_name.value = data.first_name
      formDict.value.last_name.value = data.last_name
      formDict.value.email.value = data.email
    }
  })
}

function updateUserData(){
  formErrorMsgs.value = null
  formSuccess.value = false
  let data = formDictToData(formDict)
  axios.patch(
      'http://127.0.0.1:8000/auth/users/me/',
      data
  ).catch(
      userSendErrorCatch(formDict, formErrorMsgs)
  ).then( (response) => {
    if(response){
      formSuccess.value = true
      removerErrorMsgs(formDict)
    }
  })

}

onMounted(
    async ()=>{
      await writeDataToDict()
})


</script>

<style scoped>

</style>