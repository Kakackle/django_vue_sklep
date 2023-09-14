<script setup>
import {ref, defineProps, defineEmits} from 'vue';
import { useAxiosPatch } from '../../composables/useAxiosPatch';
import { useRouter } from 'vue-router';
const router = useRouter();
const props = defineProps(['product', 'user']);
const product = ref(props.product);
const user = ref(props.user);
const emit = defineEmits(['favourited']);

const in_favourite = (prod) =>{
    const fav = product.value.favourited_by.includes(user.value.username)
    return fav;
}

const addProductToFavourites = async (prod) =>{
    let url = `api/products/${prod.slug}/favourite`;
    const {data, error} = await useAxiosPatch(url, {});
    emit('favourited');
}

const addProductToCart = async (prod) => {
    console.log(`adding prod ${prod.slug} to cart`);
    let url = `api/products/${prod.slug}/add_cart`;
    const {data, error} = await useAxiosPatch(url, {});
    emit('favourited');
}

</script>

<template>
<div class="item-card unified-shadow">
    <img class="product-img" :src="product.main_product_image">
    <!-- <p class="fav"><ion-icon name="heart-outline"></ion-icon></p> -->
    <div @click="addProductToFavourites(product)" class="fav hover">
        <ion-icon class="favourited" name="heart"
            v-if="in_favourite(product)"></ion-icon>
        <ion-icon class=""
            name="heart-outline"
            v-else></ion-icon>
    </div>
    <div class="card-bottom">
        <p class="title hover-underline"
        @click="router.push({name: 'product', params: {product_slug: product.slug}})"
        >{{ product.name }}</p>
        <p class="prod"
        @click="router.push({name: 'manufacturer', params: {man_slug: product.manufacturer.slug}})"
        >{{ product.manufacturer.name }}</p>
        <p class="price">{{ product.price }} ,-</p>
        <p class="add-cart hover-underline" @click="addProductToCart(product)">ADD TO CART</p>
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
    position: relative;
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

.add-cart{
    position: absolute;
    right: 5px;
    bottom: 5px;
    font-size: 14px;
    font-weight: 500;
}
</style>