<script setup>
import OrderSmall from './OrderSmall.vue';
import Pagination from '../Pagination.vue';
import {ref, defineProps} from 'vue'
const props = defineProps(['orders']);
const orders = ref(props.orders);
</script>

<template>
<main class="orders-main">
    <div class="orders" v-if="orders">
        <OrderSmall v-for="(order, index) in orders"
        :order="order"></OrderSmall>
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