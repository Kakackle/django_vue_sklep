<script setup>
import CartItemsPaginated from '../components/cart/CartItemsPaginated.vue';
</script>

<template>
    <p class="title">FAVOURITES</p>
    <CartItemsPaginated></CartItemsPaginated>
</template>

<style scoped>
.title{
    font-size: 32px;
    font-weight: 500;
    color: var(--gray-main);
    /* width: 100%; */
    margin: 0 auto;
}
</style>