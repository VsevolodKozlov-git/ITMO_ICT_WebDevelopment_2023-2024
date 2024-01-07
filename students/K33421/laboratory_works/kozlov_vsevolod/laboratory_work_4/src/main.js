import { createApp } from 'vue';
import App from '@/App.vue';
import router from "@/router";
import 'bootstrap/dist/css/bootstrap.css';
import BootstrapVue3 from 'bootstrap-vue-3';

// Import BootstrapVue3 styles
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css';
import '@/styles/styles.css'
const app = createApp(App);

// Use the BootstrapVue3 plugin with the app
app.use(BootstrapVue3);
app.use(router);

app.mount('#app');