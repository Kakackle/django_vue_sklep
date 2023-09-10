<script setup>
import {ref, defineProps, defineEmits} from 'vue';

const props = defineProps(['review']);
const review = ref(props.review);

const emit = defineEmits(['product_liked']);

</script>

<template>
<div class="review unified-shadow" v-if="review">
    <div class="review-left">
        <img class="profile-img">
        <p>{{ review.date_created }}</p>
    </div>
    <div class="review-right">
        <div class="review-top">
            <div>
                <p class="author">{{ review.author.username }}</p>
                <p class="title">{{ review.title }}</p>
            </div>
            <div class="likes">
                <!-- TODO: sprawdzanie czy zalogowany uzytkownik w liked_by -->
                <ion-icon name="thumbs-up-outline"></ion-icon>
                <p>{{ review.like_count }}</p>
            </div>
        </div>
        <div class="review-bot">
            <p>{{ review.message }}</p>
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