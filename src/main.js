import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import axios from 'axios';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';

// Configuração do Axios para chamadas de API
axios.defaults.baseURL = 'http://localhost:3000'; // Altere para a URL do seu backend

// Uso do Vuetify para estilos de UI
Vue.use(Vuetify);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify: new Vuetify(),
  render: h => h(App),
}).$mount('#app');
