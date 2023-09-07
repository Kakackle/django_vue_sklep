<script setup>
// TODO: moze zrobic z tego jakies generalne list component a potem to umieszczac
// w roznych view, ale chyba nie, bo rozne dane i nie bedzie tak duzo typow

import { ref } from 'vue';
import axios from 'axios';

const url = "api/manufacturers/";
const manufacturers = ref([]);

const getManufacturers = ()=>{
    axios.get(url)
    .then((res)=>{
        console.log(res);
        manufacturers.value = res.data.results;
    })
    .catch((err)=>{
        console.log(err);
    })
}

getManufacturers();

</script>

<template>
<main class="man-list" v-if="manufacturers">
    <p class="title">Manufacturer List</p>
    <div v-for="(man, index) in manufacturers" :key="man" class="man-item">
    <p class="name">{{man.name}}</p>
    <p class="data data-gray">Est.: {{ man.date_created }}</p>
    <p class="data data-normal">owner: {{ man.owner.first_name }}{{ man.owner.last_name }}</p>
    <ul class="products">
        <li v-for = "(prod, pindex) in man.products" :key="pindex"
         class="data prod">{{ prod }}</li>
    </ul>
</div>
</main>
</template>

<style scoped>
.title{
    font-size: 36px;
    font-weight: 500;
}
.man-list{
    display: flex;
    flex-direction: column;
    gap: 10px;
    max-width: var(--max-page-width);
    padding: 20px;
}

.man-item{
    display: flex;
    flex-direction: column;
    gap: 2px;
}

.name{
    font-size: 20px;
}

.data{
    font-size: 14px;
}

.data-gray{
    color: var(--gray-light);
}

.data-normal{
    color:var(--gray-main);
}
</style>