<script setup>
import Hero from '../components/home/Hero.vue';
import LineBar from '../components/nav/LineBar.vue';
import Fsection from '../components/home/Fsection.vue';
import ReviewsSection from '../components/home/ReviewsSection.vue';
import GalleryPreview from '../components/home/GalleryPreview.vue';
import CallToAction from "../components/home/CallToAction.vue";
import EndSection from "../components/home/EndSection.vue";
import ModelPreview from "../components/home/ModelPreview.vue";
import Footer from "../components/Footer.vue";
import Dropdown from '../components/Dropdown.vue';

// const items  = ['oneitem','oneitem', 'oneitemitem', 'one' ]
// const bgColor = "#333333";
// const color = "#AAAAAA";
// const font = 12;
</script>

<template>
    <!-- <Dropdown :items=items :bgcolor=bgColor :color=color :font=font></Dropdown> -->
    <Hero></Hero>
    <LineBar></LineBar>
    <Fsection></Fsection>
    <ReviewsSection></ReviewsSection>
    <ModelPreview></ModelPreview>
    <GalleryPreview></GalleryPreview>
    <CallToAction></CallToAction>
    <EndSection></EndSection>
    <!-- <Footer></Footer> -->
</template>