<script setup>
import {ref} from "vue";
const banner_index = ref(0); //ktory banner jest aktualnie wyswietlany

const base_image_path="../../static/img/banners/";
const image_paths = [
    "Banner-1.png",
    "Banner-2.png",
    "Banner.png",
    "Group 7.png",
];

const banner_backgrounds = [
    "#F5D8B7",
    "#e7c15f",
    "#282a2a",
    "#282a2a"
];
const banner_background = ref(banner_backgrounds[0]);

// TODO: moze dlarego tak skacze, bo miedzy ladowaniem obrazkow nie ma nic
// a zamiast tego powinno byc zajmujace miejsce pole albo jakies opoznienie znikania wzgledem pojawiania sie

// TODO: moze slide transition zamiast fade

const num_of_images = image_paths.length; //for dot generation
const image_path = ref(base_image_path + image_paths[0]); //current image path
const image_url = ref(`url(${image_path.value})`);

//funkcja aktualizujaca licznik liczbowo z czasem
const update_index = function(){
    banner_index.value += 1;
    banner_index.value %= num_of_images;
    change_path(banner_index.value);
}

//funkcja wyswietlajaca (ustawiajaca zrodlo obrazku) banner na bazie licznika
const change_path = function(index) {
    image_path.value = base_image_path + image_paths[index];
    image_url.value = `url(${image_path.value})`;
    banner_background.value = banner_backgrounds[index];
    console.log(`banner_index: ${banner_index}, new image path: ${image_path.value},
    banner_background: ${banner_background.value}`);
}

let bannerInterval = setInterval(update_index, 5000);

//funkcja zmieniajaca banner na podstawie inputu uzytkownika
const changeBanner = function(index){
    banner_index.value = index - 1;
    console.log(`banner_index: ${banner_index.value}`);
    change_path(banner_index.value);
    clearInterval(bannerInterval);
    bannerInterval = setInterval(update_index, 5000);
}

</script>

<template>
    <transition name="fade" mode="out-in">
    <main class="hero" :style="{backgroundColor: banner_background}" :key=banner_index>
        <!-- <transition name="slide"> -->
            <div class="banner-wrapper">
                <img class="banner" :src=image_path :key=banner_index>
                <div class="dots">
                    <p v-for="index in num_of_images" @click="changeBanner(index)"
                    class="dot unified-shadow hover"
                    :class="{active: index-1 === banner_index}"></p>
                </div>
            </div>
    </main>
    </transition>
</template>

<style scoped>
.hero{
    width: 100vw;
    overflow: hidden;
    display: flex;
    justify-content: center;
}
.banner-wrapper{
    /* max-width: 100%; */
    /* max-width: var(--max-page-width); */
    /* width: clamp(400px, 100%, var(--max-page-width)); */
    width: clamp(400px, 100%, 1420px);
    position: relative;
    /* max-height: 600px; */
    margin: 0 auto;
}

.banner{
    max-width: 100%;
    height: auto;
}

.dots{
    position: absolute;
    right: 40px;
    bottom: 20px;
    display: flex;
    gap: 10px;
}
/* FIXME: z jakiegos powod uten kolor sie nie aplikuje... */
.dot{
    height: 10px;
    width: 10px;
    border-radius: 50%;
    background-color: #FEFEFE;
}

.active{
    background-color: #e7c15f;
}

/* .slide-leave-active,
.slide-enter-active {
  transition: 1s;
}
.slide-enter {
  transform: translate(100%, 0);
}
.slide-leave-to {
  transform: translate(-100%, 0);
} */

.fade-enter-active{
    transition: opacity .5s ease
}

.fade-leave-active{
    transition: opacity .6s ease
}

.fade-enter,
.fade-leave-to {
    opacity: 0
}

</style>