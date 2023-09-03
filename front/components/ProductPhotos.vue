<script setup>
import PhotoWheel from './PhotoWheel.vue';
</script>

<template>
<section class="product-photos">
    <PhotoWheel></PhotoWheel>
    <div class="photo-main">
        <div class="photo-bg">
            <img class="main-img" src="../../static/img/products/yellow/yellow_1.png">
            <div class="arr-right unified-shadow">
                <p>&gt;</p>
            </div>
            <div class="arr-left unified-shadow">
                <p>&lt;</p>
            </div>
        </div>
    </div>
</section>
</template>

<style scoped>
.product-photos{
    display: flex;
    gap: 80px;
}
.photo-main{
    display: flex;
    align-items: center;
    justify-content: center;
}

.photo-bg{
    width: 380px;
    height: 380px;
    border-radius: 50%;
    background-color: var(--color-main);
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
}

.main-img{
    height: 350px;
    width: 350px;
    object-fit: contain;
}

.arr-left, .arr-right{
    width: 40px;
    height: 40px;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: var(--white-main);
    position: absolute;
    border-radius: 50%;
    font-size: 50px;
    font-weight: 500;
    color: var(--gray-main);
}

.arr-left{
    left: 0;
    transform: translateX(-50%);
}
.arr-right{
    right: 0;
    transform: translateX(50%);
}

</style>