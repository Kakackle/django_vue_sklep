<script setup>
import {ref} from 'vue';
import { RouterLink, RouterView } from 'vue-router'
import Nav from './components/Nav.vue';

// const USER_TYPES = JSON.parse(document.getElementById('user-types').textContent);
const user = JSON.parse(document.getElementById('user').textContent);
const URLS = JSON.parse(document.getElementById('URLS').textContent);
const fetched = ref();


fetch(URLS.api_product_list)
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
        <Nav></Nav>
        <h1>Hello Vue</h1>
        <h3>user:{{ user.username }}</h3>
        <p v-for="url in URLS">{{ url }}</p>
        <!-- <a href="http://127.0.0.1:8000/accounts/login">Login</a>
        <p v-for="prod in fetched">{{ prod.name }}</p> -->
        <!-- <p v-for="user in USER_TYPES">{{ user }}</p> -->
    </header>
    <main>
        <RouterView></RouterView>
    </main>
    
</template>

<style scoped></style>