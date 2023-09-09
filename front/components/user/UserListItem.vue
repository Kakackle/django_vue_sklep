<script setup>
import {defineProps, ref} from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter();
const props = defineProps(['profile']);
const profile = ref(props.profile);
</script>

<template>
    <div class="user-info" v-if="profile">
        <div class="user-left">
            <img class="user-img" :src="profile.profile_image">
        </div>
        <div class="user-right">
            <p class="name hover-underline"
            @click="router.push({name:'user', params: {user_slug: profile.user.username}})">
            {{ profile.user.username }}</p>
            <p class="text">{{ profile.user.email }}</p>
            <p class="smth">{{ profile.user.first_name }}</p>
            <p class="bio">{{ profile.bio }}</p>
        </div>
    </div>
</template>

<style scoped>
    .user-info{
        display: flex;
        gap: 20px;
        padding: 20px;
        /* margin: 0 auto; */
        width: 100%;
    }
    .user-img{
        /* padding: 10px; */
        border-radius: 50%;
        border: 4px solid var(--gray-main);
        width: 50px;
        height: 50px;
    }

    .user-right{
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    .name{
        font-size: 24px;
        font-weight: 500;
        text-decoration: underline;
    }

    .text{
        font-size: 14px;
    }

    .bio{
        line-height: 1.5;
        width: 400px;
    }
</style>