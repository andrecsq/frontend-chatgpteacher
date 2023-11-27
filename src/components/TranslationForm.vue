<template>
    <v-form @submit.prevent="submitTranslation">
      <v-text-field
        v-model="textToTranslate"
        label="Enter text to translate"
        required
      ></v-text-field>
  
      <v-btn type="submit" color="primary">Translate</v-btn>
    </v-form>
  </template>
  
  <script>
  export default {
    name: 'TranslationForm',
    data() {
      return {
        textToTranslate: ''
      };
    },
    methods: {
      submitTranslation() {
        this.$emit('submit', this.textToTranslate);
        this.textToTranslate = ''; // Limpar o campo após a submissão
      }
    }
  };
  </script>
  
  <style>
  /* Estilos personalizados para TranslationForm */
  </style>
  