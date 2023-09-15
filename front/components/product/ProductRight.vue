<script setup>
import {ref, defineProps, defineEmits} from 'vue';
import { useUser } from "../../composables/useUser.js";
import { useAxiosPatch } from '../../composables/useAxiosPatch';
import { useToasts } from '../../composables/useToasts';
import { useRouter } from 'vue-router';
const URLS = JSON.parse(document.getElementById('URLS').textContent);
const base_path = URLS.base_path;
const router = useRouter();

const props = defineProps(['product'])
const product = ref(props.product);
const edit_path = base_path + `/backend/products/${product.value.slug}/edit`;

const emit = defineEmits(['favourited']);

const loggedUser = useUser();

const addProductToFavourites = async (prod) =>{
    let url = `api/products/${prod.slug}/favourite`;
    const {data, error} = await useAxiosPatch(url, {});
    emit('favourited');
} 

const addProductToCart = async (prod) => {
    console.log(`adding prod ${prod.slug} to cart`);
    let url = `api/products/${prod.slug}/add_cart`;
    const {data, error} = await useAxiosPatch(url, {});
    useToasts(data, error, `${prod.name} added to cart`, `failed to add to cart`);
    // emit('tocart');
}

const buyNow = async (prod) => {
    await addProductToCart(prod);
    router.push({name: 'cart'});
}

const in_favourite = (prod) =>{
    const fav = product.value.favourited_by.includes(loggedUser.value.username)
    // const fav = loggedUser.value.favourite_products.includes(prod.name);
    // console.log(`in_fav: ${fav}`);
    return fav;
}
</script>

<template>
<div class="product-right" v-if="product">
    <div class="right-top">
        <a class="edit hover-underline" v-if="product.owner.username === loggedUser.username"
        :href="edit_path">Edit product</a>
        <p class="manufacturer"
        @click="router.push({name: 'manufacturer', params: {man_slug: product.manufacturer.slug}})"
        >{{ product.manufacturer.name }}</p>
    </div>
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
    <button class="buy-button hover" @click="buyNow(product)">BUY NOW</button>
    <div class="buy-options">
        <div @click="addProductToFavourites(product)" class="hover">
            <ion-icon class="rating-icon" name="heart"
             v-if="in_favourite(product)"></ion-icon>
            <ion-icon class="rating-icon favourited"
             name="heart-outline"
             v-else></ion-icon>
            <p class="buy-option">ADD TO FAVOURITES</p>
        </div>
        <p>or</p>
        <div class="hover" @click="addProductToCart(product)">
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
.right-top{
    display: flex;
    justify-content: space-between;
}

.edit{
    font-size: 12px;
    text-decoration: none;
    color: var(--gray-light);
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
    width: 40px;
    height: 40px;
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
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    font-size: 20px;
}

.buy-option{
    font-size: 16px; 
}

.buy-options div{
    display: flex;
    align-items: center;
    gap: 5px;
}

.buy-options div, p{
    align-self: center;
    justify-self: center;
}
</style>