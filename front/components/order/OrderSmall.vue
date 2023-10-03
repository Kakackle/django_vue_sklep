<script setup>
import {ref, defineProps} from 'vue'
import { useRouter } from 'vue-router';
import {useAxiosGetPaginated} from "../../composables/useAxiosGetPaginated.js";
import { formatDate } from '../../composables/formatDate';
const props = defineProps(['order']);
const order = ref(props.order);
const order_url = `api/orders/${order.value.id}/items/`;
const products = ref();
const router = useRouter();

const getProductsByOrder = async (link) =>{
    const {data, pages, error} = await useAxiosGetPaginated(link);
    products.value = data.value;
    // console.log(`products: ${JSON.stringify(products.value)}`);
}

getProductsByOrder(order_url);

</script>

<template>
<div class="order-small unified-border" v-if="order">
    <div class="order-left">
        <p class="order-number hover-underline"
        @click="router.push({name: 'order', params: {'order_pk': order.id}})">Order no. #{{ order.id }}</p>
        <p class="items-title">Items ordered: {{ order.sum_items }}</p>
        <div class="order-items" v-if="products">
            <p v-for="(product, index) in products" :key="index">
            {{ product.quantity }}x 
            {{ product.product.name }} - {{ product.product.price }}</p>
            <!-- <p>The Yellow Menace - 1 x 199,99 = 199,99</p>
            <p>The Blue Guitar - 2 x 99,99 = 199,98</p> -->
            <p class="total">total: {{ order.sum_cost }}</p>
        </div>
    </div>
    <div class="order-right">
        <p class="text-right">ordered on: {{ formatDate(order.date_ordered) }}</p>
        <p class="text-right">status: {{ order.status }} [{{ formatDate(order.date_updated) }}]</p>
    </div>
</div>
</template>

<style scoped>
.order-small{
    display: flex;
    padding: 10px;
    justify-content: space-between;
    width: 100%;
    background-color: var(--white-main);
}

.order-left, .order-right, .order-items{
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.order-items{
    gap: 5px;
}

.order-items p{
    font-size: 12px;
    font-weight: 400;
    color: var(--gray-light);
}

.total{
    color: var(--gray-main);
    font-size: 14px;
}

.items-title, .text-right{
    font-size: 12px;
}

.order-number{
    font-size: 20px;
    font-weight: 500;
}

</style>