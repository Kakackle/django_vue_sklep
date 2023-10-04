<script setup>
import UserInfo from '../components/user/UserInfo.vue';
import OrderSmallPaginated from '../components/order/OrderSmallPaginated.vue';

import axios from 'axios';
import { ref } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute()
const user_slug = route.params.user_slug;

const profile = ref();

const orders = ref();
const pages = ref();

const loading_profile = ref(0);
const getProfile = (slug) => {
    loading_profile.value = 1;
    axios.get(`api/profiles/${user_slug}/`)
    .then((res)=>{
        profile.value = res.data;
        console.log(res);
        getOrdersByUser(user_slug);
    })
    .catch((err)=>{
        console.log(err);
    })
    .finally(()=>{
        loading_profile.value = 0;
    })
}

const loading_orders = ref(0);
const getOrdersByUser = (slug) => {
    loading_orders.value = 1;
    axios.get(`api/orders/?user=${slug}`)
    .then((res)=>{
        orders.value = res.data.results;
        pages.value = res.data.context.page_links;
        console.log(res);
    })
    .catch((err)=>{
        console.log(err);
    })
    .finally(()=>{
        loading_orders.value = 0;
    })
}

getProfile(user_slug);


</script>

<template>
<main class="user-main">
    <UserInfo :profile="profile" v-if="profile"></UserInfo>
    <OrderSmallPaginated :orders="orders" v-if="orders" class="orders">
    </OrderSmallPaginated>
    <p class="loading" v-if="loading_profile">Loading profile...</p>
    <p class="loading" v-if="loading_orders">Loading orders...</p>
    <p v-else>No orders yet</p>
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
    height: 100vh;
}

.orders{
    width: 90%;
}
</style>