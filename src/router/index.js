import Vue from 'vue';
import VueRouter from 'vue-router';
import TranslationPage from '../views/TranslationPage.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Translation',
    component: TranslationPage
  },
  // Você pode adicionar mais rotas aqui conforme necessário
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;
