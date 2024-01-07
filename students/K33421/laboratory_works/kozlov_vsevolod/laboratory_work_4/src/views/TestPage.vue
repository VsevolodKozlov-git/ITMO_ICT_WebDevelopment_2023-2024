<template>

</template>

<script setup>
import axios from "axios";
import {onMounted} from "vue";
async function f1(){
  // try{
  //   await axios.get('http://127.0.0.1:8000/lab3/book_instance/remove')
  // }
  // catch (e) {
  //   console.log(`code ${e.code}`)
  //   console.log(`status ${e.status}`)
  // }

  // axios.get(
  //     'http://127.0.0.1:8000/lab3/book_instance/remove'
  // ).catch((e) => {
  //   if (e.response){ // Ошибка в ответе сервера
  //     console.log(e.response.status) // Какая ошибка
  //     console.log(e.response.data) // Что ответил сервер
  //   }
  //   else if (e.request){ // Сделали запрос, но не получили ответ
  //     console.log(e.request)
  //   }
  //   else{ // todo
  //     // Выводит полную информацию об ошибке
  //     console.log(e.config)
  //   }
  // })


  // Код падает с 404
  // await axios.get(
  //     'http://127.0.0.1:8000/lab3/book_instance/remove'
  // )

  // Код не падает, потому что validateStatus прошел
  // await axios.get(
  //     'http://127.0.0.1:8000/lab3/book_instance/remove',
  //     {validateStatus: (status) => (status === 404)}
  // )


  // Упадет и ничего не выведет
  // axios.get(
  //     'http://127.0.0.1:8000/lab3/book_instance/remove'
  // ).then((response) => {
  //   console.log(response.data)
  //   console.log(response.status)
  //   console.log(response.statusText)
  // })

  // Упадет на response.data
  // axios.get(
  //     'http://127.0.0.1:8000/lab3/book_instance/remove'
  // ).catch((e)=>{
  //   if (e.response){
  //     console.log(e.response.status)
  //   }
  // }).then((response) => {
  //   console.log(response.data)
  //   console.log(response.status)
  //   console.log(response.statusText)
  // })


  // Тоже упадет на response.data
  // const response = await axios.get(
  //     'http://127.0.0.1:8000/lab3/book_instance/remove'
  // ).catch((e) => {
  //   console.log(e.response.status)
  // })
  //
  // console.log(response.data)

  // Вывод: Надо выкидывать ошибку, если не удалось обработать в catch
  // const response = await axios.get(
  //     'http://127.0.0.1:8000/lab3/book_instance/remove'
  // ).catch((e) => {
  //   console.log(e.response.status)
  //   // Можем дописать данные о файле в ошибку
  //   e['filename'] = 'TestPage'
  //   throw e
  // })

  // const value = axios.get(
  //     'http://127.0.0.1:8000/lab3/book_instance/remove'
  // ).catch((e) => {
  //   console.log(e.response.status)
  //   // Можем дописать данные о файле в ошибку
  //   e['filename'] = 'TestPage'
  //   return true
  // })
}


function f2(){
  // Ошибку ловить надо внутри async, а не за его пределами
  // Да, мы тут получаем тот же error
  // var result = 1;
  // (async () => {
  //   try{
  //     result = await axios.get(
  //         'http://127.0.0.1:8000/lab3/book_instance/10')
  //   }
  //   catch (e) {
  //     console.log(e.response.status)
  //   }
  // })()
  // console.log(result)
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/lab3/book_instance/10'
  }).then((response) =>{
    console.log(response)
  })



  // let response
  // axios.get(
  //     'http://127.0.0.1:8000/lab3/book_instance/10'
  // ).catch((error) => {
  //   console.log(error.toJSON())
  // }).then((thenResponse) =>{
  //   response = thenResponse
  // })
  // console.log(`response: ${response}`)
}
// onMounted(async ()=>{
//   await f1()
// })

onMounted(f2)
</script>

<style scoped>

</style>