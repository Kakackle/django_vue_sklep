<script setup>
import {defineProps, ref} from 'vue';
import { formatDate } from '../../composables/formatDate';
import { useRouter } from 'vue-router';
const router = useRouter();
const props = defineProps(['manufacturer']);
const man = ref(props.manufacturer);
</script>

<template>
<div class="man-item">
    <p class="name hover-underline"
    @click="router.push({name: 'manufacturer', params: {'man_slug':man.slug}})">
    {{man.name}}</p>
    <p class="data data-gray">Est.: {{ formatDate(man.date_created) }}</p>
    <p class="data data-normal hover-underline"
    @click="router.push({name: 'user', params: {'user_slug':man.owner.username}})">
    owner: {{ man.owner.username }}</p>
    <ul class="products">
        <li v-if="man.products"
        v-for = "(prod, pindex) in man.products.slice(0,5)" :key="pindex"
        class="data prod hover-underline"
        @click="router.push({name: 'product', params: {'product_slug':prod}})">
        {{ prod }}</li>
    </ul>
</div>
</template>

<style scoped>
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

.products{
    padding: 0px 20px;
}
</style>