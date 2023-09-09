<script setup>
import {defineProps, ref} from 'vue';
const props = defineProps(['manufacturer']);
const man = ref(props.manufacturer);
</script>

<template>
<div class="man-item">
    <p class="name">{{man.name}}</p>
    <p class="data data-gray">Est.: {{ man.date_created }}</p>
    <p class="data data-normal">owner: {{ man.owner.first_name }}{{ man.owner.last_name }}</p>
    <ul class="products">
        <li v-if="man.products"
        v-for = "(prod, pindex) in man.products.slice(0,5)" :key="pindex"
        class="data prod">{{ prod }}</li>
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
</style>