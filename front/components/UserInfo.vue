<script setup>
</script>

<template>
<div class="user-info">
    <div class="user-left">
        <img class="user-img" src="">
    </div>
    <div class="user-right">
        <p class="name">Admin</p>
        <p class="text">admin@localhost.com</p>
        <p class="smth">something</p>
        <p class="bio">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Aut ipsam doloribus maxime exercitationem assumenda sint veniam blanditiis, consectetur accusamus explicabo non illo qui quis ad asperiores necessitatibus ratione optio repudiandae.</p>
    </div>
</div>
</template>

<style scoped>
    .user-info{
        display: flex;
        gap: 20px;
        padding: 20px;
        margin: 0 auto;
    }
    .user-img{
        padding: 10px;
        border-radius: 50%;
        border: 4px solid var(--gray-main);
        width: 150px;
        height: 150px;
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