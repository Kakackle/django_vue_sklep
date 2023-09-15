<script setup>
import Toolbar from '../components/nav/Toolbar.vue';
import Nav from '../components/nav/Nav.vue';
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

// const product = ref();

// const getProduct = (link) => {
//     axios.get(link)
//     .then((res)=>{
//         product.value = res.data;
//         console.log(res);
//     })
//     .catch((err)=>{
//         console.log(err);
//     })
// }

// getProduct(url);

// const {product, error} = await useAxiosGet(url);
const product = ref();
const error = ref();

const getProduct = async (link) =>{
    const {data, error} = await useAxiosGet(link);
    // console.log(`get_prod data ${JSON.stringify(data.value)}`);
    product.value = data.value;
    if (error) error.value = error.value;
}

getProduct(url.value);

</script>

<template>
<PromoBar></PromoBar>
<Product :product="product" v-if="product"
@refresh="getProduct(url)" :key="product"></Product>
<ProductDescription :product="product"></ProductDescription>
<ProductReviewSection :product="product" v-if="product"
@review_posted="getProduct(url)"></ProductReviewSection>
<SimilarProducts></SimilarProducts>
</template>

<style scoped>
</style>