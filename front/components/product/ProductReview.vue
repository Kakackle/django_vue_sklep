<script setup>
import {ref, defineProps, defineEmits} from 'vue';

const props = defineProps(['review']);
const review = ref(props.review);

console.log(`review: ${JSON.stringify(review)}`);

const emit = defineEmits(['review_liked']);

import { useUserStore } from "../../stores/user.js"
import { storeToRefs } from "pinia";
import axios from 'axios';
const userStore = useUserStore();
const {loggedUser} = storeToRefs(userStore);

let liked_by_names = []
if(review.value.liked_by){
    review.value.liked_by.forEach((rev)=>{
        liked_by_names.push(rev.username);
    })
    // console.log(`liked by names: ${liked_by_names}`);
    // console.log(`${loggedUser.value.username} in liked_by: ${liked_by_names.includes(loggedUser.value.username)}`);
};

const like_url = `api/reviews/${review.value.slug}/like`;

const like_review = (link) =>{
    console.log(`liked with url ${link}`);
    let token = '';
    axios.get(`api/get_token`)
    .then((res)=>{
        token = res.data.token;
        return axios.patch(link, {
            user: loggedUser.value.username,
        },
        {
            headers: {
                'X-CSRFToken': token,
                "Content-Type": "multipart/form-data"
            },
        })
    })
    .then((res)=>{
        emit('review_liked');
        // console.log(res);
    })
    .catch((err)=>{
        console.log(err);
    })
}

const user_url = `api/profiles/${review.value.author.username}/`;
const profile = ref();

const get_user_profile = (link) =>{
    axios.get(link)
    .then((res)=>{
        // console.log(res)
        profile.value = res.data;
    })
    .catch((err)=>{
        console.log(err);
    })
}

get_user_profile(user_url);

</script>

<template>
<div class="review unified-shadow" v-if="review" :key="review">
    <div class="review-left">
        <img class="profile-img" :src="profile.profile_image"
        v-if="profile">
        <p>{{ review.date_created }}</p>
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