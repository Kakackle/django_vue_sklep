<script setup>
import ProductCard from '../product/ProductCard.vue';
import Pagination from '../Pagination.vue';
import { useUser } from '../../composables/useUser';
import {ref, defineProps, defineEmits} from 'vue';
const props = defineProps(['products', 'pages']);
const products = ref(props.products);
const pages = ref(props.pages);

const emit = defineEmits(['favourited', 'page_change']);

const page_change = (link, index) =>{
    emit('page_change', link, index);
}

const loggedUser = useUser();

</script>

<template>
<main class="main">
    <div class="items" v-if="products" :key="products">
        <ProductCard v-for="(prod, index) in products"
        :product="prod" :user="loggedUser"
        @favourited="emit('favourited')" :key="prod"></ProductCard>
    </div>
    <Pagination v-if="pages" :pages="pages" class="pagination"
    @change_page="page_change">
    </Pagination>
</main>
</template>

<style scoped>
.main{
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 30px;
    align-items: center;
}
.items{
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
    }

.pagination{
    align-items: center;
}

.active{
    font-weight: 800;
}
</style>