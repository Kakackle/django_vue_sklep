<script setup>
import {ref, defineProps, defineEmits} from 'vue';
import axios from 'axios';
import { useAxiosPost } from '../../composables/useAxiosPost';

const props = defineProps(['product']);
const product = ref(props.product);

import { useUserStore } from "../../stores/user.js"
import { storeToRefs } from "pinia";
const userStore = useUserStore();
const {loggedUser} = storeToRefs(userStore);

const emit = defineEmits(['review_posted']);

const post_url = `api/reviews/`

const newTitle = ref();
const newMessage = ref();
const newRating = ref();

const postReview = async (link) =>{
    let newData = {
    author: loggedUser.value.username,
    message: newMessage.value,
    rating: newRating.value,
    product: product.value.slug,
    title: newTitle.value,
    };
    const {data, error} = await useAxiosPost(link, newData);
    emit('review_posted');
}

</script>

<template>
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
    <button @click="postReview(post_url)" v-if="product">create review</button>
</div>
</template>

<style scoped>
.review-form{
    display: flex;
    flex-direction: column;
    width: 100%;
    gap: 10px;
    padding: 10px;
}
.label-div{
    display: flex;
    flex-direction: column;
}

.label-div label{
    font-size: 14px;
}

.label-div input, textarea{
    font-size: 16px;
}
</style>