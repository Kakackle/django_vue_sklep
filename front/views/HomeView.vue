<script setup>
import Hero from '../components/Hero.vue';
import LineBar from '../components/LineBar.vue';
import Fsection from '../components/Fsection.vue';
import ReviewsSection from '../components/ReviewsSection.vue';
import GalleryPreview from '../components/GalleryPreview.vue';
import CallToAction from "../components/CallToAction.vue";
import EndSection from "../components/EndSection.vue";
import Footer from "../components/Footer.vue";
import Dropdown from '../components/Dropdown.vue';

const items  = ['oneitem','oneitem', 'oneitemitem', 'one' ]
const bgColor = "#333333";
const color = "#AAAAAA";
const font = 12;
</script>

<template>
    <Dropdown :items=items :bgcolor=bgColor :color=color :font=font></Dropdown>
    <Hero></Hero>
    <LineBar></LineBar>
    <Fsection></Fsection>
    <ReviewsSection></ReviewsSection>
    <GalleryPreview></GalleryPreview>
    <CallToAction></CallToAction>
    <EndSection></EndSection>
    <!-- <Footer></Footer> -->
</template>