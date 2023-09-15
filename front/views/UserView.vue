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

const getProfile = (slug) => {
    axios.get(`api/profiles/${user_slug}/`)
    .then((res)=>{
        profile.value = res.data;
        console.log(res);
        getOrdersByUser(user_slug);
    })
    .catch((err)=>{
        console.log(err);
    })
}

const getOrdersByUser = (slug) => {
    axios.get(`api/orders/?user=${slug}`)
    .then((res)=>{
        orders.value = res.data.results;
        pages.value = res.data.context.page_links;
        console.log(res);
    })
    .catch((err)=>{
        console.log(err);
    })
}

getProfile(user_slug);


</script>

<template>
<main class="user-main" v-if="profile">
    <UserInfo :profile="profile"></UserInfo>
    <OrderSmallPaginated :orders="orders" v-if="orders" class="orders">
    </OrderSmallPaginated>
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
}

.orders{
    width: 90%;
}
</style>