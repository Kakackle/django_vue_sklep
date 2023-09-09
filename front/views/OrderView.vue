<script setup>
import CartItemsMinPaginated from '../components/cart/CartItemsMinPaginated.vue';
</script>

<template>
<main class="order-main">
    <p class="order-number">Order no. #2343248</p>
    <p class="order-info">admin</p>
    <p class="order-info">status: paid</p>
    <button class="tracking hover">TRACK</button>
    <p class="order-info">ordered on: 04.09.2023</p>
    <CartItemsMinPaginated></CartItemsMinPaginated>
</main>
</template>

<style scoped>
.order-main{
    max-width: var(--max-page-width);
    padding: 0px 20px;
    display: flex;
    flex-direction: column;
    gap: 5px;
}

.order-number{
    font-size: 24px;
    font-weight: 500;
}

.order-info{
    font-size: 14px;
}

.tracking{
    background-color: var(--second-main);
    color: var(--gray-main);
    padding: 5px;
    font-weight: 500;
    width: 80px;
}
</style>