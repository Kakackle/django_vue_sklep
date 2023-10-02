<script setup>
import ProductReview from './ProductReview.vue';
import ProductReviewForm from './ProductReviewForm.vue';
import Pagination from '../Pagination.vue';
import { useUser } from '../../composables/useUser';
import { useAxiosGetPaginated } from '../../composables/useAxiosGetPaginated';

import {ref, defineEmits, defineProps} from 'vue'
import axios from 'axios';

const props = defineProps(['product']);
const product = ref(props.product);
console.log(`product: ${JSON.stringify(product.value)}`);

const emit = defineEmits(['review_posted']);

const reviews = ref();
const pages = ref();
const error = ref();

const loggedUser = useUser();

const url = ref(`api/reviews/?product=${product.value.slug}`);

const getReviews = async (link) => {
    const {data, pages, error} = await useAxiosGetPaginated(link);
    reviews.value = data.value;
    pages.value = pages.value;
    console.log(`pages: ${pages.value}`);
    if (error) error.value = error.value;
}

getReviews(url.value);

const review_posted = async () =>{
    emit('review_posted');
    await getReviews(url);
}

const change_page =(link) => {
    getReviews(link);
}

</script>

<template>
    <section class="review-section">
        <p class="title">User reviews</p>
        <div class="reviews" v-if="reviews" :key="reviews">
            <ProductReview v-for="review in reviews" :review="review"
            @review_liked="review_posted" :key="review"></ProductReview>
        </div>
        <p class="reviews" v-else>No reviews yet</p>
        <Pagination @page_change="change_page"
        :pages="pages" v-if="pages">
        </Pagination>
        <ProductReviewForm @review_posted="review_posted"
        :product="product"></ProductReviewForm>
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