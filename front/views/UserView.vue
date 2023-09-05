<script setup>
import UserInfo from '../components/UserInfo.vue';
import OrderSmallPaginated from '../components/order/OrderSmallPaginated.vue';
</script>

<template>
<main class="user-main">
    <UserInfo></UserInfo>
    <OrderSmallPaginated class="orders"></OrderSmallPaginated>
</main>
</template>

<style scoped>
.user-main{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    padding: 10px;
    max-width: var(--max-page-width);
}

.orders{
    width: 90%;
}
</style>