<script setup>
import {ref} from 'vue';
import { useRouter } from 'vue-router';
import { useAxiosGetPaginated } from '../../composables/useAxiosGetPaginated';
const router = useRouter();

const images_url = `api/productimages/?page_size=20`
const images = ref();
const loading = ref(0);
const getPreviewImages = async (link) => {
    loading.value = 1;
    const {data, pages, error} = await useAxiosGetPaginated(link);
    images.value = data.value;
    loading.value = 0;
}

getPreviewImages(images_url);

</script>

<template>
    <section class="gallery-section">
        <p class="section-title">Reach out to the sun</p>
        <div class="gallery-imgs" v-if="images">
            <img class="gallery-img" v-for="(img, index) in images" :key="img" :src="img.image">
            <img class="gallery-img" src="">
            <img class="gallery-img" src="">
            <img class="gallery-img" src="">
            <img class="gallery-img" src="">
            <img class="gallery-img" src="">
            <img class="gallery-img" src="">
            <img class="gallery-img" src="">
            <img class="gallery-img" src="">
            <img class="gallery-img" src="">
        </div>
        <p v-if="loading">Loading images...</p>
        <button class="gallery-button"
        @click="router.push({name: 'store'})">GO TO STORE &rarr;</button>
    </section>
</template>

<style scoped>
.gallery-section{
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 10px;
    margin-bottom: var(--section-margin);
}

.gallery-imgs{
    max-width: var(--max-page-width);
    /* width: 100%; */
    max-height: 320px;
    /* border: 2px solid black; */
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    overflow: auto;
    gap: 30px;
    padding: 40px;
    background-color: var(--gray-lightest);
    /* border-bottom: 4px solid var(--gray-lighter); */
}

.gallery-img{
    width: 150px;
    height: 150px;
    object-fit: contain;
    background-color: var(--white-main);
}

.gallery-button{
    border: 5px solid var(--second-main);
    background-color: var(--white-main);
    padding: 5px;
    font-size: 20px;
    font-weight: 500;
    border-radius: 10px;
}

.gallery-button:hover{
    cursor: pointer;
    filter: brightness(0.75);
}

</style>