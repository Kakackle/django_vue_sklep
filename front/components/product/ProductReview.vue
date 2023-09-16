<script setup>
import {ref, defineProps, defineEmits} from 'vue';
import { useUser } from '../../composables/useUser';
import { useAxiosGet } from '../../composables/useAxiosGet';
import { useAxiosPatch } from "../../composables/useAxiosPatch";
import { formatDate } from "../../composables/formatDate";
import {useAxiosDelete} from "../../composables/useAxiosDelete";
const props = defineProps(['review']);
const review = ref(props.review);

console.log(`review: ${JSON.stringify(review)}`);

const emit = defineEmits(['review_liked']);

import axios from 'axios';

const loggedUser = useUser();

let liked_by_names = []
if(review.value.liked_by){
    review.value.liked_by.forEach((rev)=>{
        liked_by_names.push(rev.username);
    })
    // console.log(`liked by names: ${liked_by_names}`);
    // console.log(`${loggedUser.value.username} in liked_by: ${liked_by_names.includes(loggedUser.value.username)}`);
};

const like_url = `api/reviews/${review.value.slug}/like`;
const del_url = `api/reviews/${review.value.slug}/`

const like_review = async (link) =>{
    let newData = {
        user: loggedUser.value.username,
    }
    const {data, error} = await useAxiosPatch(link, newData);
    emit('review_liked');
}

const user_url = ref(`api/profiles/${review.value.author.username}/`);
const profile = ref();
const error = ref();

const get_user_profile = async (link) => {
    const {data, error} = await useAxiosGet(link);
    profile.value = data.value;
    if (error) error.value = error.value;
}

get_user_profile(user_url);

const delete_review = async (link) => {
    const {data, error} = await useAxiosDelete(link);
    emit('review_liked');
}

</script>

<template>
<div class="review unified-shadow" v-if="review" :key="review">
    <div class="review-left">
        <img class="profile-img" :src="profile.profile_image"
        v-if="profile">
        <p>{{ formatDate(review.date_created) }}</p>
    </div>
    <div class="review-right">
        <div class="review-top">
            <div>
                <p class="author">{{ review.author.username }}</p>
                <p class="title">{{ review.title }}</p>
            </div>
            <div class="likes" v-if="loggedUser">
                <ion-icon class="liked hover-color" name="thumbs-up-sharp"
                v-if="liked_by_names.includes(loggedUser.username)"
                @click="like_review(like_url)"></ion-icon>
                <ion-icon class="unliked hover-color" name="thumbs-up-outline"
                v-else
                @click="like_review(like_url)"></ion-icon>
   
                <p>{{ review.like_count }}</p>
            </div>
        </div>
        <div class="review-bot">
            <p class="message">{{ review.message }}</p>
            <p class="rating">{{review.rating}}/5</p>
        </div>
        <button @click="delete_review(del_url)">delete review</button>
    </div>
</div>
</template>

<style scoped>
.review{
    padding: 20px 10px;
    display: flex;
}

.review-left{
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 10px;
    gap: 10px;
}

.review-left p{
    font-size: 12px;
}

.profile-img{
    height: 30px;
    width: 30px;
    background-color: var(--gray-lightest);
    border-radius: 50%;
}

.review-right{
    display: flex;
    flex-direction: column;
    width: 100%;
}

.review-top{
    display: flex;
    justify-content: space-between;
}

.message{
    font-weight: 300;
}

.author{
    font-size: 10px;
}
.likes{
    font-size: 20px;
    display: flex;
    align-items: center;
    gap: 5px;
}

.review-bot{
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 16px;
}
.rating{
    font-size: 24px;
    font-weight: 500;
}

.unliked{
    font-size: 20px;
    color: var(--gray-main);
    background-color: var(--white-main);
}

.liked{
    font-size: 20px;
    color: var(--second-main);
    background-color: var(--white-main);
}
</style>