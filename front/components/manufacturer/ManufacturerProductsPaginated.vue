<script setup>
import CartItemMin from '../cart/CartItemMin.vue';
import Pagination from '../Pagination.vue';

import axios from 'axios';
import { ref, nextTick, defineProps } from 'vue';

const props = defineProps(['manufacturer']);
const manufacturer = ref(props.manufacturer);

const products = ref();
const pages_prop = ref();

const query_string = `api/products/?manufacturer=${manufacturer.value.slug}`;

const getProducts = (link) =>{
    axios.get(link)
    .then((res)=>{
        products.value = res.data.results;
        pages_prop.value = res.data.context.page_links;
        console.log(res);
    })
    .catch((err)=>{
        console.log(err);
    })
}

const getProductsByPage = (link, page_index) => {
    getProducts(link);
}

const change_page = (link, page_index) => {
    getProductsByPage(link, page_index);
}

getProducts(query_string);

</script>

<template>
<main class="prod-main">
    <div class="products" v-if="products" :key="products">
        <div v-for="(prod, index) in products">
            <div class="first" v-if="index === 0">
                <CartItemMin :product="prod"></CartItemMin>
            </div>
            <CartItemMin v-else :product="prod">
            </CartItemMin>
        </div>
    </div>
    <Pagination @page_change="change_page"
    :pages="pages_prop" v-if="pages_prop"></Pagination>
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
    width: 100%;
}

.first{
    padding: 10px;
    background-color: var(--second-main);
}



</style>