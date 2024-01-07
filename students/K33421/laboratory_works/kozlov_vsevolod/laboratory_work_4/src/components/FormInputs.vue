<template>
  <div v-for="field in fieldsArr">
    <div class="label">{{field.label}}</div>
    <input
        v-model="field.value"
        class="input"
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
</script>

<style scoped>

</style>