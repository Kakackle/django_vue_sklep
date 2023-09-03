<script setup>
</script>

<template>
<div class="review unified-shadow">
    <div class="review-left">
        <img class="profile-img">
        <p>14.07.2023</p>
    </div>
    <div class="review-right">
        <div class="review-top">
            <div>
                <p class="author">Real_user_123</p>
                <p class="title">Love it! Best yellow disto on the market...</p>
            </div>
            <div class="likes">
                <ion-icon name="thumbs-up-outline"></ion-icon>
                <p>3</p>
            </div>
        </div>
        <div class="review-bot">
            <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Exercitationem, architecto labore. Velit est impedit, nisi eaque error asperiores facilis suscipit. Eos maiores porro maxime debitis odio, sed quisquam dolor consequuntur?</p>
            <p class="rating">5/5</p>
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
</style>