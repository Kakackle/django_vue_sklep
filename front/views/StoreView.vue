<script setup>
import Toolbar from '../components/nav/Toolbar.vue';
import Nav from '../components/nav/Nav.vue';
import PromoBar from '../components/nav/PromoBar.vue';
import Breadcrumbs from '../components/nav/Breadcrumbs.vue';
import SideFilters from '../components/store/SideFilters.vue';
import TopFilters from "../components/store/TopFilters.vue";
import StoreGrid from '../components/store/StoreGrid.vue';

import {ref} from 'vue';
import { useAxiosGetPaginated } from '../composables/useAxiosGetPaginated';

const products = ref();
const pages = ref();

const url = `api/products/`;

const getProducts = async (link) => {
    const {data, pages, error} = await useAxiosGetPaginated(link);
    products.value = data.value;
    pages.value = pages.value;
    error.value = error.value;
}

getProducts(url);

</script>

<template>
<!-- <Toolbar></Toolbar>
<Nav></Nav> -->
<PromoBar></PromoBar>
<Breadcrumbs></Breadcrumbs>

<section class="store-section">
        <SideFilters></SideFilters>
        <div class="store-main">
            <TopFilters></TopFilters>
            <StoreGrid :products="products"
             @favourited="getProducts(url)" v-if="products" :key="products">
            </StoreGrid>
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

</style>