import { createApp } from 'vue'
import App from '@/App.vue'
// Автоматически resolve index.js
import router from "@/router";

const app = createApp(App);
// install plugin in vue
app.use(router);
// rootContainer is css selector where app will be mounted
// if 'body' it will be mounted inside body
app.mount('#app');