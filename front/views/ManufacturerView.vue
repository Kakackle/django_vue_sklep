<script setup>
import ManufacturerInfo from '../components/ManufacturerInfo.vue';
import ManufacturerProductsPaginated from '../components/ManufacturerProductsPaginated.vue';
</script>

<template>
<main class="man-main">
    <ManufacturerInfo></ManufacturerInfo>
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