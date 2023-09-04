<script setup>
// TODO: odbieranie zalogowanego uzytkownika
// TODO: GET przedmiotow z cartu itd
// TODO: wszedzie brakuje hover i hover_underline

import PromoBar from "../components/PromoBar.vue";
import Breadcrumbs from "../components/Breadcrumbs.vue";
import SimilarProducts from "../components/SimilarProducts.vue";

import CartRight from "../components/CartRight.vue";
import CartItemsPaginated from "../components/CartItemsPaginated.vue";

import CartDrop from "../components/CartDrop.vue";
</script>

<template>
<PromoBar></PromoBar>
<Breadcrumbs></Breadcrumbs>
<p class="title">CART</p>
<section class="cart-section">
    <CartItemsPaginated></CartItemsPaginated>
    <CartRight></CartRight>
</section>
<CartDrop></CartDrop>
<SimilarProducts></SimilarProducts>
</template>

<style scoped>

.title{
    font-size: 40px;
    font-weight: 500;
    color: var(--gray-main);
    /* width: 100%; */
    margin: 0 auto;
}
.cart-section{
    max-width: var(--max-page-width);
    margin: 0 auto;
    margin-bottom: var(--section-bottom);
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    padding: 10px;
}
</style>