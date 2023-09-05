<script setup>
import { useRouter, RouterLink } from 'vue-router';
const router = useRouter();
import axios from "axios"
import {ref, watch} from "vue"
import {useToast} from "vue-toastification"
const toast = useToast();

import { useUserStore } from "../../stores/user.js"
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
// TODO: cos ten cart wystaje poza ekran czasem
// TODO: nav active zjebany ale jakos sie naprawi autonakladanie przez routerlinki
// TODO: oddzielnie link na konto (tylko dla zalogowanego) i user view (dla kazdego)
import CartDrop from '../cart/CartDrop.vue';
const isCartDisplay = ref(0);

const displayCart = ()=>{
  isCartDisplay.value = !isCartDisplay.value;
  console.log(`isCartDisplay: ${isCartDisplay.value}`);
}

import AccountDrop from './AccountDrop.vue';
const isAccountDisplay = ref(0);
</script>

<template>
    <main class="main-nav">
        <div class="nav-container">
            <div class="logo-div">
                <!-- <img src="./images/kalopsia.svg"> -->
                <p class="logo">KALOPSIA</p>
            </div>
            <ul class="nav-menu">
                <RouterLink to="/" class="nav-link hover">HOME</RouterLink>
                <RouterLink to ="/store" class="nav-link hover">STORE</RouterLink>
                <RouterLink to="/about" class="nav-link hover">ABOUT</RouterLink>
                <li class="nav-link">PARTNERS</li>
                <div class="acc-div">
                  <img class="acc-img hover" :src="loggedUser.profile_image"
                    v-if="loggedUser.is_authenticated"
                    @click="isAccountDisplay = !isAccountDisplay">
                  <ion-icon class="acc-icon hover" v-else name="person-circle-outline"
                  @click="isAccountDisplay = !isAccountDisplay"></ion-icon>

                  <AccountDrop class="acc-drop" v-if="isAccountDisplay"
                  :user="loggedUser" :URLS="URLS"></AccountDrop>
                </div>
                <!-- <div v-if="loggedUser.is_authenticated" class="acc-div">
                    <a class="acc hover" href="/">{{loggedUser.username}}</a>
                    <a class="acc hover" :href="URLS.logout">Logout</a>
                </div>
                <div v-else class="acc-div">
                    <a class="acc hover" :href="URLS.login">Login</a>
                    <a class="acc" :href="URLS.signup">Signup</a>
                </div> -->
                <!-- <li class="acc">ACC</li> -->
                <li class="cart" v-if="loggedUser.is_authenticated">
                  <div class="cart-click hover" @click="displayCart">
                    <ion-icon class="icon-2rem" name="cart-outline"></ion-icon>
                    <p>CART (1)</p>
                  </div>
                  <CartDrop v-if="isCartDisplay" class="cart-drop"></CartDrop>
                </li>
            </ul>
        </div>
    </main>
</template>

<style scoped>
.main-nav {
  width: 100%;
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

a.router-link-exact-active  {
  text-decoration: underline;
}

.nav-link {
  font-size: 20px;
  color: var(--white-main);
  text-decoration: none;
}

.acc {
  font-size: 20px;
  color: var(--white-main);
  font-weight: 500;
  text-decoration: none;
}

.acc-div{
  position: relative;
}

.acc-drop{
  position: absolute;
  top:30px;
  right:0px;
  z-index: 3;
}

.acc-img{
  width: 25px;
  height: 25px;
  background-color: var(--gray-lighter);
  border-radius: 50%;
}

.acc-icon{
  font-size: 25px;
  color: var(--white-main);
}

.cart {
  font-size: 20px;
  color: var(--second-main);
  margin-left: 5px;
  position: relative;
}

.cart-click{
  display: flex;
  gap: 5px;
  align-items: center;
}

.cart-drop{
  position: absolute;
  top: 30px;
  right: 0;
  z-index: 2;
}
</style>