<script setup>
import { ref, defineProps } from "vue";
import CartItemMin from "./CartItemMin.vue";
import Pagination from "../Pagination.vue";

const props = defineProps(['items', 'pages'])
const items = ref(props.items);
const pages = ref(props.pages);

</script>

<template>
<div class="cart-left">
    <div class="cart-items" v-if="items">
        <CartItemMin v-for="(item, index) in items" :item="item"></CartItemMin>
    </div>
    <Pagination v-if="pages" :pages="pages"></Pagination>
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

</style>