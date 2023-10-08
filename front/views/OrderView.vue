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

const URLS = JSON.parse(document.getElementById('URLS').textContent);
const base_path = URLS.base_path;
const checkout_path = ref('')

const getOrder = async (link) => {
    const {data, error} = await useAxiosGet(link);
    order.value = data.value;
    checkout_path.value = base_path + `/backend/checkout/${order.value.id}`;
}

getOrder(order_link);

const loading = ref(0);
const getOrderItems = async (link) => {
    loading.value = 1;
    const {data, pages, error} = await useAxiosGetPaginated(link);
    items.value = data.value;
    pages_prop.value = pages.value;
    loading.value = 0;
}

getOrderItems(order_items_link);

</script>

<template>
<main class="order-main" v-if="order">
    <p class="order-number">Order no. #{{ order.id }}</p>
    <p class="order-info">{{ order.user.username }}</p>
    <p class="order-info">status: {{ order.status }}</p>
    <div class="controls">
        <a class="pay hover-underline" :href="checkout_path">PAY FOR ORDER</a>
        <button class="tracking hover">TRACK</button>
    </div>
    <p class="order-info">ordered on: {{ formatDate(order.date_ordered) }}</p>
    <p class="order-info">Items in order:</p>
    <CartItemsMinPaginated v-if="items" :items="items" :pages="pages_prop"></CartItemsMinPaginated>
</main>
<p v-else class="loading">Loading order...</p>
</template>

<style scoped>
.order-main{
    max-width: var(--max-page-width);
    padding: 20px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 5px;
    border: 1px solid var(--gray-lighter);
    margin-top: 20px;
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

.pay{
    background-color: var(--gray-main);
    color: var(--white-main);
    padding: 10px;
    font-weight: 500px;
    text-decoration: none;
}

.controls{
    display: flex;
    align-items: center;
    gap: 20px;
}

</style>