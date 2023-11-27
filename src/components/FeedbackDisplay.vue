<template>
    <v-card>
      <v-card-title>Translation Feedback</v-card-title>
      <v-card-text v-if="feedback">
        <div><strong>Original Text:</strong> {{ feedback.originalText }}</div>
        <div><strong>Translated Text:</strong> {{ feedback.translatedText }}</div>
        <div><strong>Comments:</strong> {{ feedback.comments }}</div>
      </v-card-text>
      <v-card-text v-else>
        No feedback available.
      </v-card-text>
    </v-card>
  </template>
  
  <script>
  export default {
    name: 'FeedbackDisplay',
    props: {
      feedback: {
        type: Object,
        required: true
      }
    }
  };
  </script>
  
  <style>
  /* Estilos personalizados para FeedbackDisplay */
  </style>
  