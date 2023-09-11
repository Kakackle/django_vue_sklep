<script setup>
import ProductReview from './ProductReview.vue';
import ProductReviewForm from './ProductReviewForm.vue';

import {ref, defineEmits, defineProps} from 'vue'
import axios from 'axios';

const props = defineProps(['product']);
const product = ref(props.product);
console.log(`product: ${JSON.stringify(product.value)}`);

const emit = defineEmits(['review_posted']);

const reviews = ref();
const pages = ref();
// TODO: paginacja...

import { useUserStore } from "../../stores/user.js"
import { storeToRefs } from "pinia";
const userStore = useUserStore();
const {loggedUser} = storeToRefs(userStore);

const url = `api/reviews/?product=${product.value.slug}`;
console.log(`url: ${url}`);

const getReviews = (link) => {
    console.log(`=========== get reviews called ==========`)
    axios.get(link)
    .then((res)=>{
        reviews.value = res.data.results;
        // console.log(`reviews: ${JSON.stringify(reviews.value)}`)
        pages.value = res.data.context.page_links;
        // console.log(res);
    })
    .catch((err)=>{
        console.log(err);
    })
}

getReviews(url);

// TODO: daty brzydkie w chuj w formacie datetime z django - moze jest jakas biblioteka
// do tego, jak w django humanize i naturaltime

</script>

<template>
    <section class="review-section">
        <p class="title">User reviews</p>
        <container class="reviews" v-if="reviews" :key="reviews">
            <ProductReview v-for="review in reviews" :review="review"
            @review_liked="getReviews(url)" :key="review"></ProductReview>
        </container>
        <p class="reviews" v-else>No reviews yet</p>
        <ProductReviewForm @review_posted="getReviews(url)"
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