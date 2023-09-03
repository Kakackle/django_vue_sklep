<script setup>
</script>

<template>
<div class="photo-wheel unified-shadow">
    <img class="wheel-img" src="../../static/img/products/yellow/yellow_front.png">
    <img class="wheel-img active" src="../../static/img/products/yellow/yellow_1.png">
    <img class="wheel-img" src="../../static/img/products/yellow/yellow_3.png">
    <img class="wheel-img" src="../../static/img/products/yellow/yellow_1.png">
</div>
</template>

<style scoped>
.photo-wheel{
    display: flex;
    flex-direction: column;
    padding: 10px;
    gap: 10px;
    overflow: hidden;
    height: 380px;
}

.wheel-img{
    height: 100px;
    width: 100px;
    object-fit: contain;
}

.active{
    background-color: var(--gray-lighter);
    border-radius: 20px;
}
</style>