<script setup>
import StoreGrid from '../components/store/StoreGrid.vue';
import { useAxiosGetPaginated } from '../composables/useAxiosGetPaginated';
import { useUser } from '../composables/useUser';
import { ref } from 'vue';
const user = useUser();
const products = ref();
const pages_prop = ref();

const fav_url = `api/products/?favourited_by=${user.value.username}`;
const getFavouriteItems = async(link) => {
    const {data, pages, error} = await useAxiosGetPaginated(link);
    products.value = data.value;
    pages_prop.value = pages.value;
}

getFavouriteItems(fav_url);

</script>

<template>
    <main class="main">
    <p class="title">FAVOURITES</p>
    <StoreGrid :products="products" :pages="pages_prop" v-if="products"
    @favourited="getFavouriteItems(fav_url)"></StoreGrid>
    </main>
</template>

<style scoped>
.main{
    padding: 20px;
}
.title{
    font-size: 32px;
    font-weight: 500;
    color: var(--gray-main);
    /* width: 100%; */
    margin: 0 auto;
}
</style>