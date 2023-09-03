<script setup>
import Toolbar from '../components/Toolbar.vue';
import Nav from '../components/Nav.vue';
import PromoBar from '../components/PromoBar.vue';
import Product from '../components/Product.vue';
import ProductDescription from '../components/ProductDescription.vue';
import ProductReviewSection from "../components/ProductReviewSection.vue";
import SimilarProducts from '../components/SimilarProducts.vue';
import { useRoute } from 'vue-router';
const route = useRoute();
const product_slug = route.params.product_slug;
// TODO: dynamicznie
</script>

<template>
<PromoBar></PromoBar>
<p>product_slug: {{ product_slug }}</p>
<Product></Product>
<ProductDescription></ProductDescription>
<ProductReviewSection></ProductReviewSection>
<SimilarProducts></SimilarProducts>
</template>

<style scoped>
</style>