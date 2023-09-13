<script setup>
import CartItem from "./CartItem.vue";
import Pagination from "../Pagination.vue";
import { useUser } from "../../composables/useUser";
import { useAxiosGetPaginated }  from "../../composables/useAxiosGetPaginated";
import {ref, defineEmits} from 'vue';


const user = useUser();
const url = ref(`api/carts/${user.value.username}-cart/items/`);

// const products = ref();
const items = ref();
const pages = ref();

const getProducts = async (link) => {
    const {data, pages, error} = await useAxiosGetPaginated(link);
    items.value = data.value;
    pages.value = pages.value;
    // error.value = error.value;
}

getProducts(url);

</script>

<template>
<div class="cart-left">
    <div class="cart-items" v-if="items" :key="items">
        <CartItem v-for="(item, index) in items" :key="prod"
        :item="item" @product_changed="getProducts(url)">
        </CartItem>
    </div>
    <Pagination :pages="pages" v-if="pages"></Pagination>
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