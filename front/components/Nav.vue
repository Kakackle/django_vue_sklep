<script setup>
import { useRouter, RouterLink } from 'vue-router';
const router = useRouter();
import axios from "axios"
import {ref, watch} from "vue"
import {useToast} from "vue-toastification"
const toast = useToast();

import { useUserStore } from "../stores/user.js"
import { storeToRefs } from "pinia";
const userStore = useUserStore();
const {loggedUser} = storeToRefs(userStore)

//from Django
const user = JSON.parse(document.getElementById('user').textContent);
const URLS = JSON.parse(document.getElementById('URLS').textContent);
loggedUser.value = user;
const loggedIn = ref(0);
if (user.is_authenticated) loggedIn.value = 1;

// TODO:? get cart from API (by user)

</script>

<template>
    <main class="main-nav">
        <div class="nav-container">
            <div class="logo-div">
                <!-- <img src="./images/kalopsia.svg"> -->
                <p class="logo">KALOPSIA</p>
            </div>
            <ul class="nav-menu">
                <RouterLink to="/" class="nav-link">HOME</RouterLink>
                <li class="nav-link">STORE</li>
                <RouterLink to="/about" class="nav-link">ABOUT</RouterLink>
                <li class="nav-link">PARTNERS</li>
                <div v-if="loggedUser.is_authenticated" class="acc-div">
                    <li class="acc">{{loggedUser.username}}</li>
                    <a class="acc" :href="URLS.logout">Logout</a>
                </div>
                <div v-else class="acc-div">
                    <a class="acc" :href="URLS.login">Login</a>
                    <a class="acc" :href="URLS.signup">Signup</a>
                </div>
                <!-- <li class="acc">ACC</li> -->
                <li class="cart"><ion-icon class="icon-2rem" name="cart-outline"></ion-icon>CART (1)</li>
            </ul>
        </div>
    </main>
</template>

<style scoped>
.main-nav {
  width: 100lvw;
  background-color: var(--color-main);
  padding: 10px;
}

.nav-container {
  background-color: var(--color-main);
  max-width: var(--max-page-width);
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
}

.logo {
  font-size: 20px;
  color: var(--white-main);
  font-weight: 600;
}

.nav-menu {
  display: flex;
  gap: 20px;
  list-style: none;
  flex-wrap: wrap;
}

.active, .router-link-active  {
  text-decoration: underline;
}

.nav-link {
  font-size: 20px;
  color: var(--white-main);
}

.acc {
  font-size: 20px;
  color: var(--white-main);
  font-weight: 500;
}

.acc-div{
    display: flex;
    gap: 10px;
}

.cart {
  font-size: 20px;
  color: var(--second-main);
  display: flex;
  align-items: center;
  gap: 5px;
  margin-left: 5px;
}
</style>