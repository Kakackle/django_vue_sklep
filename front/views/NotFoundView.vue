<script setup>
import { useRouter } from 'vue-router';
const router = useRouter();
</script>

<template>
    <div class="main">
        <p class="title">404 Page Not Found</p>
        <p class="msg">perhaps you entered in a wrong id or url</p>
        <p class="hover-underline big-button"
        @click="router.push({name: 'home'})">Go back to Home</p>
    </div>
</template>

<style scoped>
.main{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 10px;
}
.title{
    font-size: 40px;
    border-bottom: 2px solid black;
}
.msg{
    font-size: 20px;
}
.big-button{
    font-size: 30px;
}
</style>