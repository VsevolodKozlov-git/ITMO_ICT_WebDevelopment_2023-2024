<template>
  <div v-if="authorizationError">
    Авторизируйтесь прежде чем изменять данные пользователя
  </div>
  <div v-else>
    <FormInputs :fields-arr="userForm"/>
    <button @click="updateUserData">Обновить данные</button>
    <ListErrorMsgs :error-msgs="formErrorMsgs"/>
<!--    <ul v-if="formErrorMsgs" class="error">-->
<!--      Ошибка:-->
<!--      <li v-for="errorMsg in formErrorMsgs">-->
<!--        {{errorMsg}}-->
<!--      </li>-->
<!--    </ul>-->
    <div v-if="formSuccess">
      Данные обновлены
    </div>
  </div>
</template>

<script setup>
import {onMounted, ref} from "vue";
import axios from "axios";
import FormInputs from '@/components/FormInputs'
import {formDictToData, userSendErrorCatch} from "@/tools";
import ListErrorMsgs from "@/components/ListErrorMsgs"

const userForm = ref({
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
      userForm.value.first_name.value = data.first_name
      userForm.value.last_name.value = data.last_name
      userForm.value.email.value = data.email
    }
  })
}

function updateUserData(){
  formErrorMsgs.value = null
  formSuccess.value = false
  let data = formDictToData(userForm)
  axios.patch(
      'http://127.0.0.1:8000/auth/users/me/',
      data
  ).catch(
      userSendErrorCatch(userForm, formErrorMsgs)
  ).then( (response) => {
    if(response){
      formSuccess.value = true
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