<script setup>
// TODO: dynamiczne
// TODO: podyial na komonenty
// TODO: hovery i funkcjonalnosci zmiany zdjecia itd
// TODO: requesty na buy, add itd
// TODO: i moze wszedzie: kolro czcionki zamiast czarnego jakis prawie-czarny
import ProductPhotos from './ProductPhotos.vue';
import ProductRight from './ProductRight.vue';

import {ref, defineProps, defineEmits} from 'vue'

const props = defineProps(['product']);
const product = ref(props.product);

const emit = defineEmits(['refresh']);

const refresh_product = ()=>{
    emit('refresh');
}
</script>

<template>
<section class="product-section">
    <div class="product-left">
        <ProductPhotos :product="product"></ProductPhotos>
    </div>
    <ProductRight :product="product" v-if="product" :key="product"
    @favourited="refresh_product"></ProductRight>
</section>
</template>

<style scoped>
.product-section{
    max-width: var(--max-page-width);
    display: flex;
    padding: 20px;
    gap: 40px;
    flex-wrap: wrap;
    margin: 0 auto;
    margin-bottom: var(--section-margin);
}

</style>