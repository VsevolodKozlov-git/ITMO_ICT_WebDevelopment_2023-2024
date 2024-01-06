<template>
  <h1>Добавление читателя</h1>
  <form @submit.prevent>
    <div v-for="field in reader">
      <div class="label">{{field.label}}</div>
      <input
          v-model="field.value"
          class="input"
          :type="field.type">
      <div v-if="field.error_msg" class="error">
        {{field.error_msg}}
      </div>
    </div>
    <button class="btn" @click="createReader">Cоздать</button>
  </form>
  <div v-if="userAdded">
    Пользователь успешно добавлен
  </div>
</template>

<script setup>
import {ref} from "vue";
import {postData} from "@/tools";

const filename = 'ReaderCreate'

// const reader = ref({
//   reader_number: {value: '', error_msg: '', type: 'text', label: 'Читательский номер'},
//   registration_date: {value: '', error_msg: '', type: 'date', label: 'Дата регистрации'},
//   active: {value: '', error_msg: '', type: 'checkbox', label: 'Активен'},
//   first_name : {value: '', error_msg: '', type: 'text', label: 'Имя'},
//   last_name: {value: '', error_msg: '', type: 'text', label: 'Фамилия'},
//   passport_number: {value: '', error_msg: '', type: 'text', label: 'Номер паспорта'},
//   birth_date: {value: '', error_msg: '', type: 'date', label: 'Дата рождения'},
//   address: {value: '', error_msg: '', type: 'text', label: 'Адрес'},
//   mobile_number: {value: '', error_msg: '', type: 'text', label: 'Мобильный номер без +7'}
// })

const reader = ref({
  reader_number: {value: '0716990', error_msg: '', type: 'text', label: 'Читательский номер'},
  registration_date: {value: '2024-01-06', error_msg: '', type: 'date', label: 'Дата регистрации'},
  active: {value: true, error_msg: '', type: 'checkbox', label: 'Активен'},
  first_name : {value: 'Имя', error_msg: '', type: 'text', label: 'Имя'},
  last_name: {value: 'Фамилия', error_msg: '', type: 'text', label: 'Фамилия'},
  passport_number: {value: '0711000333', error_msg: '', type: 'text', label: 'Номер паспорта'},
  birth_date: {value: '2002-11-23', error_msg: '', type: 'date', label: 'Дата рождения'},
  address: {value: 'Доваторцев, 23', error_msg: '', type: 'text', label: 'Адрес'},
  mobile_number: {value: '8005553535', error_msg: '', type: 'text', label: 'Мобильный номер без +7'}
})

const userAdded = ref(false);

function createReader(){
  userAdded.value = false;
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

  let field = reader.value.reader_number
  let is_error = field.value.length > 10
  let error_msg = 'reader number should be <= 10 chars'
  validateField(field, is_error, error_msg)

  field = reader.value.first_name
  is_error = field.value.length > 100
  error_msg = 'first name should be <= 100 chars'
  validateField(field, is_error, error_msg)

  field = reader.value.last_name
  is_error = field.value.length > 100
  error_msg = 'last name should be <= 100 chars'
  validateField(field, is_error, error_msg)

  field = reader.value.passport_number
  is_error = field.value.length !== 10
  error_msg = 'passport number should be == 10 chars'
  validateField(field, is_error, error_msg)

  field = reader.value.address
  is_error = field.value.length > 200
  error_msg = 'address should be <= 200 chars'
  validateField(field, is_error, error_msg)

  field = reader.value.mobile_number
  is_error = !validatePhoneNumber(field.value)
  error_msg = 'typed incorrect mobile number'
  validateField(field, is_error, error_msg)


  if (errorFlag){
    return;
  }

  let data = {}
  for (let key in reader.value){
    data[key] = reader.value[key].value
  }

  (async() =>{
    await postData(
        'http://127.0.0.1:8000/lab3/reader/create',
        filename,
        data)
  })()

  for (let key in reader.value){
    reader.value[key].value = ''
    reader.value[key].error_msg = ''
  }
  userAdded.value = true;
}

function validatePhoneNumber(str) {
  const regex = /^[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$/;
  return regex.test(str);
}



</script>

<style scoped>
.error{
  font-size: small;
  color: red;
}
</style>