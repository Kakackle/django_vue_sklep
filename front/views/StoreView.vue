<script setup>
import PromoBar from '../components/nav/PromoBar.vue';
import Breadcrumbs from '../components/nav/Breadcrumbs.vue';
import SideFilters from '../components/store/SideFilters.vue';
import TopFilters from "../components/store/TopFilters.vue";
import StoreGrid from '../components/store/StoreGrid.vue';

import {ref} from 'vue';
import { useAxiosGetPaginated } from '../composables/useAxiosGetPaginated';

const products = ref();
const pages_prop = ref();
const count_prop = ref();

const url_base = `api/products/?`;
const url_query = ref(url_base);

const getProducts = async (link) => {
    const {data, pages, error, count} = await useAxiosGetPaginated(link);
    products.value = data.value;
    pages_prop.value = pages.value;
    error.value = error.value;
    count_prop.value = count.value;
}

getProducts(url_base);

const url_query_filtered = ref(url_query);

const filter = (filter_string) => {
    url_query.value = url_base + filter_string;
    url_query_filtered.value = url_query.value;
    console.log(`received query: ${url_query.value}`);
    getProducts(url_query.value);
}

const order = (order_string) => {
    url_query.value = url_query_filtered.value + order_string;
    console.log(`received query: ${url_query.value}`);
    getProducts(url_query.value);
}

const page_change = (link, index)=>{
    getProducts(link);
}

</script>

<template>
<PromoBar></PromoBar>
<!-- <Breadcrumbs></Breadcrumbs> -->

<section class="store-section">
        <SideFilters @filter_type="filter"></SideFilters>
        <div class="store-main">
            <TopFilters @ordering="order" :count="count_prop"
             v-if="products" class="section-margin"></TopFilters>
            <StoreGrid :products="products" :pages="pages_prop"
             @favourited="getProducts(url_query)" v-if="products" :key="products"
             @page_change="page_change">
            </StoreGrid>
            <p v-else>No products to display yet</p>
        </div>
    </section>
</template>

<style scoped>
.store-section{
    display: flex;
    gap: 80px;
    max-width: var(--max-page-width);
    margin: 0 auto;
    margin-bottom: var(--section-margin);
    padding: 20px;
}

.store-main{
    width: 100%;
}

</style>