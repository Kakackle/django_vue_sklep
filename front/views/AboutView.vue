<script setup>
import { useRouter, RouterLink } from 'vue-router';
const router = useRouter();
const URLS = JSON.parse(document.getElementById('URLS').textContent);
const base_path = URLS.base_path;
const backend_links = {
    'manufacturer_create': base_path + '/backend/manufacturers/create',
    'product_create': base_path + '/backend/products/create',
    'shipping_create': base_path + '/backend/shipping/create',
    'effect_type_create': base_path + '/backend/effect_type/create'
}

</script>

<template>
<main class="main">
    <h1>About view</h1>
    <h3>Helpful links</h3>
    <ul class="links">
        <li><RouterLink class="link hover-underline"
            to="/manufacturers/list">Manufacturer list</RouterLink></li>
        <li><RouterLink class="link hover-underline"
            to="/users/list">User list</RouterLink></li>   
        <li><RouterLink class="link hover-underline"
            to="/favourite">Favourited products</RouterLink></li>  
        <li><a class="link hover-underline" 
            :href="backend_links.manufacturer_create">Add new manufacturer</a></li>
        <li><a class="link hover-underline" 
            :href="backend_links.product_create">Add new product</a></li>
        <li><a class="link hover-underline" 
            :href="backend_links.shipping_create">Add new shipping method</a></li>
        <li><a class="link hover-underline" 
            :href="backend_links.effect_type_create">Add new effect type</a></li>
        
    </ul>

</main>
</template>

<style scoped>
.main{
    max-width: var(--max-page-width);
    width: 100%;
    margin: 0 auto;
    padding: 10px;
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.links{
    display: flex;
    flex-direction: column;
    gap: 5px;
    padding: 0px 20px;
}
.link{
    text-decoration: none;
    font-size: 16px;
    color: var(--gray-main);
}

</style>