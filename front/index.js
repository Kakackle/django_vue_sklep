// import _ from 'lodash';

// function component() {
//   const element = document.createElement('div');
//   element.innerHTML =  _.join(['Hello', 'lodash'], ' ');
//   return element;
// }
// document.body.appendChild(component());

import {createApp} from 'vue'

import App from './App.vue'

import router from './router'

import '../static/css/base.css';

const app = createApp(App)
app.use(router)
app.mount('#root')
