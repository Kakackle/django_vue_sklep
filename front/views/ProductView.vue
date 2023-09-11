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
const route = useRoute();
const product_slug = route.params.product_slug;

import { ref } from 'vue';
import axios from 'axios';

const url = `api/products/${product_slug}/`;

const product = ref();

const getProduct = (link) => {
    axios.get(link)
    .then((res)=>{
        product.value = res.data;
        console.log(res);
    })
    .catch((err)=>{
        console.log(err);
    })
}

getProduct(url);

// TODO: dynamicznie cd
</script>

<template>
<PromoBar></PromoBar>
<p>product_slug: {{ product_slug }}</p>
<Product :product="product" v-if="product"></Product>
<ProductDescription :product="product"></ProductDescription>
<ProductReviewSection :product="product" v-if="product"></ProductReviewSection>
<SimilarProducts></SimilarProducts>
</template>

<style scoped>
</style>