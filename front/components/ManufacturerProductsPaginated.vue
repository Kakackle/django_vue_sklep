<script setup>
import CartItemMin from './cart/CartItemMin.vue';
import Pagination from './Pagination.vue';
</script>

<template>
<main class="prod-main">
    <div class="products">
        <div class="first">
            <CartItemMin></CartItemMin>
        </div>
        <CartItemMin></CartItemMin>
        <CartItemMin></CartItemMin>
    </div>
    <Pagination></Pagination>
</main>
</template>

<style scoped>
.prod-main{
    display: flex;
    flex-direction: column;
    gap: 10px;
    padding: 10px;
    align-items: center;
}

.products{
    display: flex;
    flex-direction: column;
    gap: 5px;
}

.first{
    padding: 10px;
    background-color: var(--second-main);
}
</style>