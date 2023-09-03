<script setup>
import ProductReview from './ProductReview.vue';
</script>

<template>
    <section class="review-section">
        <p class="title">User reviews</p>
        <container class="reviews">
            <ProductReview></ProductReview>
            <ProductReview></ProductReview>
        </container>
    </section>
</template>

<style scoped>
.review-section{
    max-width: var(--max-page-width);
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 10px;
    padding: 20px;
}

.title{
    font-size: 16px;
    font-weight: 500;
}

.reviews{
    width: 100%;
    display: flex;
    flex-direction: column;
    padding: 0 10px;
    gap: 5px;
}
</style>