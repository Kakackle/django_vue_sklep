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

const get_product_images = (link) => {
    axios.get(link)
    .then((res)=>{
        product_images.value = res.data.results;
        product_images.value.forEach((img)=>{
            images.value.push(img.image);
        })
        images.value.unshift(main_image.value);
    })
    .catch((err)=>{
        console.log(err);
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
    <div class="photo-main">
        <div class="photo-bg">
            <!-- <img class="main-img" src="../../../static/img/products/yellow/yellow_1.png"> -->
            <img class="main-img" :src="main_image" :key="main_image">
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