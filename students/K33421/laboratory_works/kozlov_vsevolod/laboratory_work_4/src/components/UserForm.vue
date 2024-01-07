<template>
  <form @submit.prevent>
    <FormInputs :fields-arr="formDict"/>
    <ListErrorMsgs :error-msgs="formErrorMsgs"/>
    <button @click="formSendFunction">{{formSendText}}</button>
    <div v-if="formSuccess">
      {{formSuccess}}
    </div>
  </form>
</template>

<script setup>
import FormInputs from "@/components/FormInputs"
import ListErrorMsgs from "@/components/ListErrorMsgs"


defineProps({
  formDict: {required:true, type:Object},
  formErrorMsgs: {required:true, type:Array || null},
  formSendFunction: {required:true, type: Function},
  formSendText: {required:true, type: String},
  formSuccess: {required:true, type:String || null},
})
</script>

<style scoped>

</style>