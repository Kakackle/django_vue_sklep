<script setup>

import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

import ManufacturerListItem from '../components/manufacturer/ManufacturerListItem.vue';
import Pagination from '../components/Pagination.vue';

const router = useRouter();

const url = "api/manufacturers/";
const manufacturers = ref([]);

const pages = ref([]);

const loading = ref(0);

const getManufacturers = (link)=>{
    loading.value = 1;
    axios.get(link)
    .then((res)=>{
        console.log(res);
        manufacturers.value = res.data.results;
        pages.value = res.data.context.page_links;
    })
    .catch((err)=>{
        console.log(err);
    })
    .finally(()=>{
        loading.value = 0;
    })
}

getManufacturers(url);

const change_page = (link, page_index) => {
    getManufacturers(link);
}

</script>

<template>
<main>
    <div class="man-list" v-if="manufacturers" :key="manufacturers">
        <p class="title">Manufacturer List</p>
        <ManufacturerListItem v-for="(man, index) in manufacturers" :key="man"
        :manufacturer="man"
        class="list-item-separator"></ManufacturerListItem>
        <Pagination :pages="pages" @page_change="change_page"></Pagination>
    </div>
    <p v-else>No manufacturers to display</p>
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

.list-item-separator{
    border-bottom: 1px solid var(--gray-light);
}
</style>