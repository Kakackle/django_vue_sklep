<script setup>
import { useAxiosGetPaginated } from '../composables/useAxiosGetPaginated';
import { useRouter } from 'vue-router';
import { ref } from 'vue';
const router = useRouter();

const products = ref();
const getProducts = async () => {
    const {data, pages, error} = await useAxiosGetPaginated(`api/products/`);
    products.value = data.value;
}

getProducts();

</script>

<template>
    <section class="similar-section">
        <p class="title">SIMILAR PRODUCTS</p>
        <div class="similar unified-border" v-if="products">
            <!-- <img class="similar-img unified-border" src="../../static/img/products/board/board_1.png"> -->
            <img class="similar-img unified-border hover"
            v-for="(prod, index) in products" :key="prod"
            :src="prod.main_product_image"
            @click="router.push({name: 'product', params: {'product_slug': prod.slug}})">
        </div>
    </section>
</template>

<style scoped>
.similar-section{
    max-width: var(--max-page-width);
    margin: 0 auto;
    padding: 20px;
}

.title{
    font-size: 2rem;
}
.similar{
    display: flex;
    padding: 10px;
    gap: 20px;
}

.similar-img{
    padding: 10px;
    height: 100px;
    width: 100px;
    object-fit: contain;
}
</style>