<script setup>
import {ref} from 'vue';
import { RouterLink, RouterView } from 'vue-router'
// const USER_TYPES = JSON.parse(document.getElementById('user-types').textContent);
const test = JSON.parse(document.getElementById('test').textContent);
const user = JSON.parse(document.getElementById('user').textContent);
const count = ref(0);
const other = ref('b');
const fetched = ref();

//nie rozumiem jak by to mialo odkryc niby
const URLS = {
  PRODUCT_LIST: '{% url "api:api_product_list" %}',
};


fetch('http://localhost:8000/api/products/')
// fetch('api/products')
// fetch(URLS.PRODUCT_LIST)
.then((res)=>res.json())
.then((data)=>{
    fetched.value = data;
})
.catch((err)=>{
    console.log(err);
})

</script>

<template>
    <header>
        <h1>Hello Vue</h1>
        <h2>Test: {{ test }}</h2>
        <!-- TODO: bo chcialbym nav zrobic w vue dynamiczny...
        ale moze w django lepszy bo tutaj {% url %} i blizej koszyka itd -->
        <h3>user:{{ user }}</h3>
        <a href="http://127.0.0.1:8000/accounts/login">Login</a>
        <button @click="count++">{{ count }}</button>
        <p v-if="other == 'a'">A: {{ other }}</p>
        <p v-else>B: {{ other }}</p>
        <p v-if="count == 2">Count is 2</p>
        <p v-for="prod in fetched">{{ prod.name }}</p>
        <!-- <p v-for="user in USER_TYPES">{{ user }}</p> -->
    </header>
    <main>
        <RouterView></RouterView>
    </main>
    
</template>

<style scoped></style>