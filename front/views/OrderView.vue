<script setup>
import CartItemsMinPaginated from '../components/cart/CartItemsMinPaginated.vue';
import { useRoute, useRouter } from 'vue-router';
import { ref } from 'vue';
import { useAxiosGetPaginated } from '../composables/useAxiosGetPaginated';
import { useAxiosGet } from '../composables/useAxiosGet';
import { formatDate } from '../composables/formatDate';

const router = useRouter();
const route = useRoute();
const order_pk = route.params.order_pk;

const order_link = `api/orders/${order_pk}/`;
const order_items_link = `api/orders/${order_pk}/items/`;

const order = ref();
const items = ref();
const pages_prop = ref();

const getOrder = async (link) => {
    const {data, error} = await useAxiosGet(link);
    order.value = data.value;
}

getOrder(order_link);

const getOrderItems = async (link) => {
    const {data, pages, error} = await useAxiosGetPaginated(link);
    items.value = data.value;
    pages_prop.value = pages.value;
}

getOrderItems(order_items_link);

const base_path = URLS.base_path;
const checkout_path = base_path + `/backend/checkout/${order.id}`;
</script>

<template>
<main class="order-main" v-if="order">
    <p class="order-number">Order no. #{{ order.id }}</p>
    <p class="order-info">{{ order.user.username }}</p>
    <p class="order-info">status: {{ order.status }}</p>
    <button class="tracking hover">TRACK</button>
    <a class="tracking hover-underline" :href="checkout_path">PAY FOR ORDER</a>
    <p class="order-info">ordered on: {{ formatDate(order.date_ordered) }}</p>
    <CartItemsMinPaginated v-if="items" :items="items" :pages="pages_prop"></CartItemsMinPaginated>
</main>
</template>

<style scoped>
.order-main{
    max-width: var(--max-page-width);
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 5px;
    border: 1px solid var(--gray-lighter);
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