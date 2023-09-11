<script setup>
import {ref, defineProps} from 'vue';
const props = defineProps(['product'])
const product = props.product;

</script>

<template>
<div class="product-right" v-if="product">
    <p class="manufacturer">{{ product.manufacturer.name }}</p>
    <div class="product-title"><p>{{ product.name.toUpperCase() }}</p></div>
    <div class="product-rating">
        <ion-icon name="star-outline"></ion-icon>
        <p class="numbers">{{product.rating_average}}/5</p>
        <!-- przenosi do headera na stronie?? -->
        <p>see all reviews</p>
    </div>
    <div class="facts">
        <p v-if="product.type == 'effect'">5 Facts:</p>
        <p v-else>Facts</p>
        <ul>
            <li>{{ product.character }}</li>
            <li>{{ product.warranty }} years warranty</li>
            <div v-if="product.type=='effect'">
                <li>{{ product.effect_type }}</li>
                <li>{{ product.size_type }}</li>
                <li>{{ product.power_type }} powered</li>
            </div>
        </ul>
    </div>
    <div class="price">
        <p class="price-text" v-if="product.discount == 0">{{ product.price }} ,-</p>
        <div class="price-div" v-else>
            <p class="price-text price-discounted">{{ product.price }}</p>
            <p class="price-text price-new">{{ (product.price * (1-product.discount)).toFixed(2) }}</p>
        </div>
        <p class="free">free shipping included*</p>
    </div>
    <!-- FUNKCJONALNOSCI -->
    <button class="buy-button">BUY NOW</button>
    <div class="buy-options">
        <div>
            <ion-icon class="rating-icon" name="star-outline"></ion-icon>
            <p class="buy-option">ADD TO FAVOURITES</p>
        </div>
        <p>or</p>
        <div>
            <ion-icon class="rating-icon" name="cart-outline"></ion-icon>
            <p class="buy-option">ADD TO CART</p>
        </div>
    </div>
</div>
</template>

<style scoped>
.product-right{
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    /* gap: 5px; */
    width: 350px;
    margin: 0 auto;
}
.manufacturer{
    margin-left: auto;
    font-size: 12px;
    font-weight: 500;
}
.product-title{
    background-color: var(--gray-lightest);
    padding: 10px;
}

.product-title p{
    font-size: 40px;
}

.product-rating{
    display: flex;
    gap: 10px;
    justify-content: center;
    align-items: center;
    font-size: 20px;
}
.rating-icon{
    width: 25px;
    height: 25px;
}
.numbers{
    font-size: 30px;
}

.facts{
    display: flex;
    flex-direction: column;
    gap: 5px;
    font-size: 24px;
}

.facts p{
    font-weight: 700;
}

.facts ul{
    list-style: none;
    font-size: 18px;
}

.price{
    display: flex;
    flex-direction: column;
    align-items: end;
    margin-left: auto;
}
.price-text{
    font-size: 24px;
    font-weight: 500;
}
.price-div{
    display: flex;
    flex-direction: column;
    gap: 5px;
}
.price-discounted{
    text-decoration: line-through;
}
.price-new{
    color: var(--green-main);
}

.free{
    font-size: 12px;
    color: var(--gray-light);
}
.buy-button{
    background-color: var(--color-main);
    color: var(--white-main);
    padding: 10px;
    border: none;
    font-size: 24px;
}
.buy-options{
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    font-size: 20px;
}
/* 
.buy option{
    font-size: 
} */

.buy-options div{
    display: flex;
    align-items: center;
    gap: 5px;
}
</style>