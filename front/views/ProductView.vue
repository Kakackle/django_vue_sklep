<script setup>
import PromoBar from '../components/nav/PromoBar.vue';
import Product from '../components/product/Product.vue';
import ProductDescription from '../components/product/ProductDescription.vue';
import ProductReviewSection from "../components/product/ProductReviewSection.vue";
import SimilarProducts from '../components/SimilarProducts.vue';
import Breadcrumbs from '../components/nav/Breadcrumbs.vue';
import { useRoute } from 'vue-router';
import { useAxiosGet } from '../composables/useAxiosGet.js';

const route = useRoute();
const product_slug = route.params.product_slug;

import { ref } from 'vue';
import axios from 'axios';

const url = ref(`api/products/${product_slug}/`);

const product = ref();
const error = ref();
const loading = ref(0);
const getProduct = async (link) =>{
    loading.value = 1;
    const {data, error} = await useAxiosGet(link);
    // console.log(`get_prod data ${JSON.stringify(data.value)}`);
    product.value = data.value;
    if (error) error.value = error.value;
    loading.value = 0;
}

getProduct(url.value);

</script>

<template>
<PromoBar></PromoBar>
<Product :product="product" v-if="product"
@refresh="getProduct(url)" :key="product"></Product>
<p v-if="loading" class="loading">Loading product...</p>
<ProductDescription :product="product" v-if="product"></ProductDescription>
<ProductReviewSection :product="product" v-if="product"
@review_posted="getProduct(url)"></ProductReviewSection>
<SimilarProducts></SimilarProducts>
</template>

<style scoped>
</style>