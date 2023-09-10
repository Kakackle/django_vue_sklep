<script setup>
import ProductReview from './ProductReview.vue';

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
const {loggedUser} = storeToRefs(userStore)

const url = `api/reviews/?product=${product.value.slug}`;
console.log(`url: ${url}`);

const getReviews = (link) => {
    axios.get(link)
    .then((res)=>{
        reviews.value = res.data.results;
        console.log(`reviews: ${JSON.stringify(reviews.value)}`)
        pages.value = res.data.context.page_links;
        console.log(res);
    })
    .catch((err)=>{
        console.log(err);
    })
}

getReviews(url);

// TODO: jakos dziwnie refresh zadzialal, 2 rayz ten sam review zwrocil
// ale po refreshu calej strony juz okej

// TODO: daty brzydkie w chuj w formacie datetime z django - moze jest jakas biblioteka
// do tego, jak w django humanize i naturaltime

const post_url = `api/reviews/`

const newTitle = ref();
const newMessage = ref();
const newRating = ref();

const postReview = (link) =>{
    let newData = {
        author: loggedUser.value.username,
        message: newMessage.value,
        rating: newRating.value,
        product: product.value.slug,
        title: newTitle.value,
    };
    let token = '';
    axios.get(`api/get_token`)
    .then((res)=>{
        token=res.data.token;
        console.log(`token gotten: ${token}`);
        newData.csrfmiddlewaretoken = token;
        console.log(`data to be sent: ${JSON.stringify(newData)}`);
        // console.log(`newData ting: ${newData.message}`);
        return axios.post(`${link}`, newData, {
            headers: {
                'X-CSRFToken': token,
                "Content-Type": "multipart/form-data"
            },
        })
    })
    .then((res)=>{
        console.log('review POST sent');
        console.log(res);
        // odswiezenie
        getReviews(url);
        emit('review_posted');
    })
    .catch((err)=>{
        console.log(err);
    })
}

</script>

<template>
    <section class="review-section">
        <p class="title">User reviews</p>
        <container class="reviews" v-if="reviews">
            <ProductReview v-for="review in reviews" :review="review"></ProductReview>
        </container>
        <p class="reviews" v-else>No reviews yet</p>
        <div class="review-form">
            <div class="label-div">
                <label for="review-message">Message</label>
                <textarea name="review-message" placeholder="Review message" v-model="newMessage">
                </textarea>
            </div>
            <div class="label-div">
                <label for="review-title">Title</label>
                <input type="text" name="review-title" placeholder="review title" v-model="newTitle">
            </div>
            <div class="label-div">
                <label for="review-rating">Rating</label>
                <select type="select" v-model="newRating">
                    <option v-for="i in 5">{{ i }}</option>
                </select>
            </div>
            <button @click="postReview(post_url)">create review</button>
        </div>
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