<template>

</template>

<script setup>
const arr = ['arr1', 'arr2', 'arr3']
const dict = {key1: 'val1', key2: 'val2', key3: 'val3'}


// in = по индексам
for (const index in arr){
  console.log(index) // 0 1 2
}
// of = по значениям
for (const value of arr){
  console.log(value) // arr1 arr2 arr3
}


// in - перебор по ключю
for (const key in dict){
  console.log(key) // key1 key2 key3
}
// of - error. Нельзя использовать со словарями
for (const value of dict){
  console.log(value) // error
}
// Чтобы перебрать ключи используем Object.values(dict), который возвращает arr значений
for (const value of Object.values(dict)){
  console.log(value) // val1 val2 val3
}


// for (const value in Object.values(dict)){
//   console.log(value)
// }
//
// for (const value in arr){
//   console.log(value)
// }
</script>

<style scoped>

</style>