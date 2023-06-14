import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import './assets/main.css'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')

setInterval(async function() {
    const response = await fetch(import.meta.env.VITE_BACKEND_URL + '/api/v1/test')
    switch(response.status) {
        case 200:
            console.log(await response.json())
            break;
        case 204:
            console.log('No new data found')
            break;
        default:
            break;
    }
}, 5000)
