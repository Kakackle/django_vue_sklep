<script setup>
import OrderSmall from './OrderSmall.vue';
import Pagination from '../Pagination.vue';
</script>

<template>
<main class="orders-main">
    <div class="orders">
        <OrderSmall></OrderSmall>
        <OrderSmall></OrderSmall>
        <OrderSmall></OrderSmall>
    </div>
    <Pagination></Pagination>
</main>
</template>

<style scoped>
.orders-main{
    display: flex;
    flex-direction: column;
    gap: 10px;
    /* max-width: var(--max-page-width); */
    align-items: center;
}

.orders{
    display: flex;
    flex-direction: column;
    width: 100%;
    gap: 10px;
}
</style>