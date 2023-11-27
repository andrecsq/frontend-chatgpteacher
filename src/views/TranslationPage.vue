<template>
    <v-container>
      <translation-form @submit="handleTranslation" />
      <feedback-display v-if="feedback" :feedback="feedback" />
    </v-container>
  </template>
  
  <script>
  import TranslationForm from '@/components/TranslationForm.vue';
  import FeedbackDisplay from '@/components/FeedbackDisplay.vue';
  
  export default {
    name: 'TranslationPage',
    components: {
      TranslationForm,
      FeedbackDisplay
    },
    data() {
      return {
        feedback: null
      };
    },
    methods: {
      handleTranslation(translationData) {
        // Aqui você pode adicionar a lógica para enviar a tradução para o backend
        // e receber o feedback. O feedback recebido pode ser armazenado em 'this.feedback'.
      }
    }
  };
  </script>
  
  <style>
  /* Seu CSS personalizado vai aqui */
  </style>
  