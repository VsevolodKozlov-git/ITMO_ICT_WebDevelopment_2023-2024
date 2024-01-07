<template>
  <form @submit.prevent>
    <FormInputs :fields-arr="formDict"/>
    <ListErrorMsgs :error-msgs="formErrorMsgs"/>
    <button @click="post">Войти</button>
    <div v-if="formSuccess">
      Вы успешно зарегистрировались
    </div>
  </form>
</template>

<script>
export default {
  name: "UserForm"
}
</script>

<style scoped>

</style>