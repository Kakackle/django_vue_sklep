<script setup>
// TODO: udanamicznic
</script>

<template>
    <section class="similar-section">
        <p class="title">SIMILAR PRODUCTS</p>
        <container class="similar unified-border">
            <img class="similar-img unified-border" src="../../static/img/products/board/board_1.png">
            <img class="similar-img unified-border" src="../../static/img/products/used/used_2.png">
            <img class="similar-img unified-border" src="../../static/img/products/used/used_front.png">
        </container>
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