<template>
  <div class="mb-3"  v-for="field in fieldsArr">
    <div class="form-label">{{field.label}}</div>

    <input
        v-model="field.value"
        :class="getFormClass(field.type)"
        :type="field.type">
    <div v-if="field.error_msg" class="error">
      {{field.error_msg}}
    </div>
  </div>
</template>

<script setup>
  defineProps({
    fieldsArr: {
      required: true,
      type: Object
    }
  })

  function getFormClass(fieldType){
    if (fieldType === 'checkbox'){
      return 'form-check'
    }
    return 'form-control'
  }
</script>

<style scoped>

</style>