<script setup>
import {ref} from 'vue';
import { RouterLink, RouterView } from 'vue-router'
import Nav from './components/nav/Nav.vue';
import Toolbar from './components/nav/Toolbar.vue';
import Footer from './components/Footer.vue';

// const USER_TYPES = JSON.parse(document.getElementById('user-types').textContent);
const user = JSON.parse(document.getElementById('user').textContent);
const URLS = JSON.parse(document.getElementById('URLS').textContent);

</script>

<template>
    <header>
        <Toolbar></Toolbar>
        <Nav></Nav>
    </header>
    <main class="main-main">
        <RouterView></RouterView>
    </main>
    <Footer class="footer"></Footer>
</template>

<style scoped>
.main-main{
    /* height: 100vw; */
    min-height: 100vw;
    height: 100%;
}
.footer{
    margin-top: auto;
    width: 100%;
    background-color: var(color-main);
    bottom: 0;
}
</style>