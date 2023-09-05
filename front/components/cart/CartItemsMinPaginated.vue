<script setup>
import CartItemMin from "./CartItemMin.vue";
import Pagination from "../Pagination.vue";
</script>

<template>
<div class="cart-left">
    <div class="cart-items">
        <CartItemMin></CartItemMin>
        <CartItemMin></CartItemMin>
        <CartItemMin></CartItemMin>
    </div>
    <Pagination></Pagination>
</div>
</template>

<style scoped>
.cart-left{
    flex-grow: 1;
    /* padding: 10px; */
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
}

.cart-items{
    display: flex;
    flex-direction: column;
    width: 100%;
    gap: 10px;
}

</style>