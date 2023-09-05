<script setup>
// TODO: dynamicznosc
// TODO: klikanie fav, przechodzenie do strony produktu itd
</script>

<template>
<div class="item-card unified-shadow">
    <img class="product-img" src="../../../static/img/products/yellow/yellow_front.png">
    <p class="fav"><ion-icon name="heart-outline"></ion-icon></p>
    <div class="card-bottom">
        <p class="title">The yellow menace</p>
        <p class="prod">Kalopsia effects</p>
        <p class="price">349.00 ,-</p>
    </div>
</div>
</template>

<style scoped>
.item-card{
    display: flex;
    flex-direction: column;
    width: 200px;
    height: 300px;
    position: relative;
}
.fav{
    position: absolute;
    right: 0;
    padding: 10px;
    top: 20px;
    font-size: 30px;
    background-color: var(--white-main);
    display: flex;
    justify-content: center;
    align-items: center;
}

.product-img{
    background-color: var(--gray-lightest);
    /* width: 100%;
    height: 100%; */
    width: 200px;
    height: 230px;
    object-fit: contain;
    border:none;
}

.card-bottom{
    padding: 5px;
    display: flex;
    flex-direction: column;
    gap: 5px;
}

.title{
    font-size: 16px;
    font-weight: 600;
}
.prod{
    font-size: 10px;
}
.price{
    font-size: 12px;
    font-weight: 500;
}
</style>