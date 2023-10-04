<script setup>
import PhotoWheel from './PhotoWheel.vue';
import {ref, defineProps} from "vue"
import axios from 'axios';
const props = defineProps(['product'])
const product = ref(props.product);

const url = `api/productimages/?product=${product.value.slug}`;
const product_images = ref();
const images = ref([]);
const main_image = ref(product.value.main_product_image);
const selected_image = ref(0);

// --------- MAGNIFIER -----------
// var evt = new Event(),
//   m = new Magnifier(evt);

// const setup_magnifier = () => {
// m.attach({
//   thumb: "#thumb",
//   large: url(main_image.value),
//   //   largeWrapper: "preview",
//   mode: "inside",
// });
// }

import VueMagnifier from '@websitebeaver/vue-magnifier'
import '@websitebeaver/vue-magnifier/styles.css'

const loading = ref(0);

const get_product_images = (link) => {
    loading.value = 1;
    axios.get(link)
    .then((res)=>{
        product_images.value = res.data.results;
        product_images.value.forEach((img)=>{
            images.value.push(img.image);
        })
        images.value.unshift(main_image.value);
        // setup_magnifier();
        loading.value = 0;
    })
    .catch((err)=>{
        console.log(err);
        loading.value = 0;
    })
}

get_product_images(url);

const change_photo_wheel = (img, index) => {
    selected_image.value = index;
    main_image.value = img;
}

const change_photo_next = () =>{
    selected_image.value += 1;
    selected_image.value %= images.value.length;
    main_image.value = images.value[selected_image.value];
}

const change_photo_back = () =>{
    selected_image.value -= 1;
    selected_image.value = selected_image.value <0 ? images.value.length: selected_image.value;
    selected_image.value %= images.value.length;
    main_image.value = images.value[selected_image.value];
}

</script>

<template>
<section class="product-photos">
    <PhotoWheel v-if="product_images" :images="images"
     :selected_image="selected_image" :key="selected_image"
    @photo_changed="change_photo_wheel"></PhotoWheel>
    <p class="loading" v-if="loading">Loading photos...</p>
    <div class="photo-main">
        <div class="photo-bg">
            <!-- <div class="magnifier-thumb-wrapper" :src="main_image">
                <img class="main-img" id="thumb" :src="main_image" :key="main_image"> 
            </div> -->
            <VueMagnifier
            className="main-img" :src="main_image" :key="main_image"
            mgShape="square"
            height="350px"
            width="auto">
            </VueMagnifier>
            <div class="arr-right hover unified-shadow" @click="change_photo_next">
                <p>&gt;</p>
            </div>
            <div class="arr-left hover unified-shadow" @click="change_photo_back">
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

.vue-magnifier__magnifier-image{
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