<script setup>
import Toolbar from '../components/nav/Toolbar.vue';
import Nav from '../components/nav/Nav.vue';
import PromoBar from '../components/nav/PromoBar.vue';
import Breadcrumbs from '../components/nav/Breadcrumbs.vue';
import SideFilters from '../components/store/SideFilters.vue';
import TopFilters from "../components/store/TopFilters.vue";
import StoreGrid from '../components/store/StoreGrid.vue';
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