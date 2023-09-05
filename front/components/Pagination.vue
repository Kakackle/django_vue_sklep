<script setup>
</script>

<template>
<div class="pagination">
    <p class="active hover-underline">1</p>
    <p class="hover-underline">2</p>
    <p class="hover-underline">3</p>
    <p class="hover-underline">...</p>
    <p class="hover-underline">99</p>
</div>
</template>

<style scoped>
.pagination{
    display: flex;
    gap: 10px;
    font-size: 14px;
}

.active{
    font-weight: 600;
}
</style>