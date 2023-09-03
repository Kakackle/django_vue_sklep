<script setup>
import Toolbar from '../components/Toolbar.vue';
import Nav from '../components/Nav.vue';
import PromoBar from '../components/PromoBar.vue';
import Breadcrumbs from '../components/Breadcrumbs.vue';
import SideFilters from '../components/SideFilters.vue';
import TopFilters from "../components/TopFilters.vue";
import StoreGrid from '../components/StoreGrid.vue';
</script>

<template>
<!-- <Toolbar></Toolbar>
<Nav></Nav> -->
<PromoBar></PromoBar>
<Breadcrumbs></Breadcrumbs>

<section class="store-section">
        <SideFilters></SideFilters>
        <div class="store-main">
            <TopFilters></TopFilters>
            <StoreGrid></StoreGrid>
        </div>
    </section>
</template>

<style scoped>
.store-section{
    display: flex;
    gap: 80px;
    max-width: var(--max-page-width);
    margin: 0 auto;
    margin-bottom: var(--section-margin);
    padding: 20px;
}

</style>