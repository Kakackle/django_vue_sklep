<script setup>
import {ref} from 'vue';
import PromoBar from "../components/nav/PromoBar.vue";
import Breadcrumbs from "../components/nav/Breadcrumbs.vue";
import SimilarProducts from "../components/SimilarProducts.vue";

import CartRight from "../components/cart/CartRight.vue";
import CartItemsPaginated from "../components/cart/CartItemsPaginated.vue";

import CartDrop from "../components/cart/CartDrop.vue";

import { useUser } from "../composables/useUser";
import { useAxiosGet } from "../composables/useAxiosGet";
import { useAxiosPatch } from '../composables/useAxiosPatch';

const user = useUser();

const cart_url = `api/carts/${user.value.username}-cart/`;
const cart = ref();

const getCart = async (link) =>{
    const {data, error} = await useAxiosGet(link);
    cart.value = data.value;
}

getCart(cart_url);

const clearCart = async () => {
    const url = `api/carts/${user.value.username}-cart/clear/`
    const {data, error} = await useAxiosPatch(url);
    getCart(cart_url);
}

</script>

<template>
<PromoBar></PromoBar>
<!-- <Breadcrumbs></Breadcrumbs> -->
<p class="title">CART</p>
<section class="cart-section" :key="cart">
    <p class="clear hover-underline" @click="clearCart" v-if="cart">clear cart</p>
    <CartItemsPaginated @emit_changes="getCart(cart_url)"></CartItemsPaginated>
    <CartRight :cart="cart" :user="user" v-if="cart" :key="cart"></CartRight>
</section>
<!-- <CartDrop></CartDrop> -->
<SimilarProducts></SimilarProducts>
</template>

<style scoped>

.title{
    font-size: 40px;
    font-weight: 500;
    color: var(--gray-main);
    /* width: 100%; */
    margin: 0 auto;
}
.cart-section{
    max-width: var(--max-page-width);
    margin: 0 auto;
    margin-bottom: var(--section-bottom);
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    padding: 10px;
    position: relative;
}

.clear{
    color: var(--gray-lighter);
    font-size: 14px;
    position: absolute;
    right: 10px;
    top: -10px;
}
</style>