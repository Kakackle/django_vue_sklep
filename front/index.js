import {createApp} from 'vue'
import {createPinia} from 'pinia'

import App from './App.vue'
import router from './router'

import axios from 'axios';

// http://127.0.0.1:8000/
// db.mloelszaaibsbbsztrir.supabase.co/
axios.defaults.baseURL = "django-vue-sklep.onrender.com/";
// axios.defaults.headers.patch['Content-Type'] = 'application/json';

import '../static/css/base.css';

import Toast from "vue-toastification"
import "vue-toastification/dist/index.css";

//Toast options
const options ={
    position: "top-right",
      timeout: 2500,
      closeOnClick: true,
      pauseOnFocusLoss: true,
      pauseOnHover: true,
      draggable: true,
      draggablePercent: 0.6,
      showCloseButtonOnHover: false,
      hideProgressBar: true,
      closeButton: "button",
      icon: true,
      rtl: false,
      transition: "Vue-Toastification__fade",
      maxToasts: 20,
      newestOnTop: true,
      // For the actual toast, including different toast types:
      toastClassName: "toast-class",
      // For the toast body when using strings or a custom component as content
      bodyClassName: ["toast-body-class-1", "toast-body-class-2"],
    }


const app = createApp(App)
app.use(router)
app.use(createPinia())
app.use(Toast, options)
app.mount('#root')
