<template>
  <form @submit.prevent class="container">
    <FormInputs :fields-arr="formDict"/>
    <ListErrorMsgs :error-msgs="formErrorMsgs"/>
    <button @click="postLogin" class="btn btn-primary">Войти</button>
    <div v-if="formSuccess">
      Вы успешно авторизировались
    </div>
  </form>
</template>

<script setup>
import {ref} from "vue";
import FormInputs from "@/components/FormInputs"
import axios from "axios";
import {formDictToData, userSendErrorCatch, removerErrorMsgs} from "@/tools";
import ListErrorMsgs from "@/components/ListErrorMsgs"

const formDict = ref({
  username: {value: '', error_msg: '', type: 'text', label: 'Username'},
  password: {value: '', error_msg: '', type: 'password', label: 'Пароль'}
})
const formErrorMsgs = ref(null)
const formSuccess = ref(false)

function postLogin(){
  formErrorMsgs.value = null
  formSuccess.value = false

  let data = formDictToData(formDict)

  axios.post(
      'http://127.0.0.1:8000/auth/token/login/',
      data
  ).catch(
      userSendErrorCatch(formDict, formErrorMsgs)
  ).then((response) =>{
    if (response){
      formSuccess.value = true
      removerErrorMsgs(formDict)
      axios.defaults.headers.common['Authorization'] = `Token ${response.data['auth_token']}`
    }
  })
}



</script>

<style scoped>
</style>