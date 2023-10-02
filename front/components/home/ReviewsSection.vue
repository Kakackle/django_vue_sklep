<script setup>
import ReviewCard from './ReviewCard.vue';
// FIXME: to by trzeba jakis GET kilku losowych recenzji przez api?
</script>

<template>
    <section class="reviews-section">
        <p class="section-title">See what they say about us:</p>
        <div class="reviews">
            <ReviewCard></ReviewCard>
            <ReviewCard></ReviewCard>
            <ReviewCard></ReviewCard>
        </div>
    </section>
</template>

<style scoped>
.reviews-section{
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: var(--section-margin);
}

.reviews{
    width: 100%;
    max-width: calc(var(--max-page-width) - 100px);
    /* border: 2px solid black; */
    height: 100%;
    padding: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    gap: 40px;
}
</style>