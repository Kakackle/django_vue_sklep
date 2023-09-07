<script setup>
import ManufacturerInfo from '../components/ManufacturerInfo.vue';
import ManufacturerProductsPaginated from '../components/ManufacturerProductsPaginated.vue';

import { ref } from 'vue';
import axios from 'axios';
import { useRoute } from 'vue-router';
const route = useRoute();
const man_slug = route.params.man_slug;

const manufacturer = ref();

const getManufacturer = (slug) =>{
    manufacturer.value = undefined;
    axios.get(`api/manufacturers/${slug}/`)
    .then((res)=>{
        console.log(res);
        manufacturer.value = res.data;
    })
    .catch((err)=>{
        console.log(err);
    })
}

getManufacturer(man_slug);

</script>

<template>
<main class="man-main" v-if="manufacturer" :key="manufacturer">
    <ManufacturerInfo :man="manufacturer" @desc_update="getManufacturer(man_slug)"></ManufacturerInfo>
    <ManufacturerProductsPaginated class="prods"></ManufacturerProductsPaginated>
</main>
</template>

<style scoped>
.main-main{
    max-width: var(--max-page-width);
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: center;
}
.prods{
    width: 100%;
}
</style>