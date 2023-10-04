<script setup>
import CartItem from "./CartItem.vue";
import Pagination from "../Pagination.vue";
import { useUser } from "../../composables/useUser";
import { useAxiosGetPaginated }  from "../../composables/useAxiosGetPaginated";
import {ref, defineEmits} from 'vue';
const emit = defineEmits(['cart_updated']);

const user = useUser();
const url = ref(`api/carts/${user.value.username}-cart/items/`);

// const products = ref();
const items = ref();
const pages_prop = ref();

const loading = ref(0);
const getProducts = async (link) => {
    loading.value = 1;
    const {data, pages, error} = await useAxiosGetPaginated(link);
    items.value = data.value;
    pages_prop.value = pages.value;
    loading.value = 0;
    // console.log(`got pages: ${JSON.stringify(pages_prop.value)}`);
    // error.value = error.value;
}

getProducts(url);

const emit_changes = () =>{
    getProducts(url);
    emit('cart_updated');
}

</script>

<template>
<div class="cart-left">
    <p class="loading" v-if="loading">Loading cart items...</p>
    <div class="cart-items" v-if="items" :key="items">
        <CartItem v-for="(item, index) in items" :key="prod"
        :item="item" @product_changed="emit_changes">
        </CartItem>
    </div>
    <div :key="pages_prop" v-if="pages_prop">
        <Pagination :pages="pages_prop"></Pagination>
    </div>
    
</div>
</template>

<style scoped>
.cart-left{
    flex-grow: 1;
    /* padding: 10px; */
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
}

.cart-items{
    display: flex;
    flex-direction: column;
    width: 100%;
    gap: 10px;
}

.pagination{
    display: flex;
    gap: 5px;
}

.active{
    font-weight: 600;
}
</style>