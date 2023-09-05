<script setup>
import ProductCard from '../product/ProductCard.vue';
</script>

<template>
<div class="items">
    <ProductCard></ProductCard>
    <ProductCard></ProductCard>
    <ProductCard></ProductCard>
</div>
<div class="pagination">
    <p class="active">1</p>
    <p>2</p>
    <p>3</p>
    <p>...</p>
    <p>10</p>
</div>
</template>

<style scoped>
.items{
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
    }

.pagination{
    display: flex;
    gap: 10px;
    font-size: 20px;
}

.active{
    font-weight: 800;
}
</style>