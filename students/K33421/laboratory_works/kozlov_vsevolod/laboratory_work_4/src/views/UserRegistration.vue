<template>
  <form @submit.prevent class="container">
    <FormInputs :fields-arr="formDict"/>
    <ListErrorMsgs :error-msgs="formErrorMsgs"/>
    <button class="btn btn-primary"  @click="post">Войти</button>
    <div v-if="formSuccess">
      Вы успешно зарегистрировались
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
  password: {value: '', error_msg: '', type: 'password', label: 'Пароль'},
  first_name: {value: '', error_msg: '', type: 'text', label: 'Имя'},
  last_name: {value: '', error_msg: '', type: 'text', label: 'Фамилия'},
  email: {value: '', error_msg: '', type: 'email', label: 'Почта'}
})
const formErrorMsgs = ref(null)
const formSuccess = ref(false)

function post(){
  formErrorMsgs.value = null
  formSuccess.value = false

  let data = formDictToData(formDict)

  axios.post(
      'http://127.0.0.1:8000/auth/users/',
      data
  ).catch(
      userSendErrorCatch(formDict, formErrorMsgs)
  ).then((response) =>{
    if (response){
      formSuccess.value = true
      removerErrorMsgs(formDict)
    }
  })
}
</script>

<style scoped>

</style>