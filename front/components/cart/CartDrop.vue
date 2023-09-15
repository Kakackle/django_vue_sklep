<script setup>
import CartItemMin from './CartItemMin.vue';
import { useUser } from '../../composables/useUser';
import { useAxiosGetPaginated } from '../../composables/useAxiosGetPaginated';
import { useAxiosGet } from '../../composables/useAxiosGet';
import { ref, defineEmits } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter();
// console.log(`cart drop opened`);
const emit = defineEmits(['cart_change']);

const user = useUser();
const items_url = ref(`api/carts/${user.value.username}-cart/items/`);
const items = ref();

const getCartItems = async (link) => {
    const {data, pages, error} = await useAxiosGetPaginated(link);
    items.value = data.value;
    pages.value = pages.value;
}

getCartItems(items_url);

const cart_url = ref(`api/carts/${user.value.username}-cart/`);
const cart = ref();

const getCart = async (link) => {
    const {data, error} = await useAxiosGet(link);
    cart.value = data.value;
    emit('cart_change', cart.value.sum_items);
}

getCart(cart_url);

</script>

<template>
    <div class="cart-drop" v-if="cart">
        <CartItemMin v-for="(item, index) in items" :key="item"
        :item="item"></CartItemMin>
        <p class="total">TOTAL: {{ cart.sum_cost }} ,-</p>
        <button class="go-button hover"
        @click="router.push({name: 'cart'})">TO CART -></button>
    </div>
</template>

<style scoped>
.cart-drop{
    background-color: var(--white-main);
    display: flex;
    flex-direction: column;
    align-items: center;
    /* gap: 10px; */
    width: 400px;
    border: 1px solid var(--gray-light);
}

.total{
    color: var(--gray-main);
    align-self: flex-end;
    padding: 10px;
}

.go-button{
    background-color: var(--gray-main);
    font-size: 20px;
    font-weight: 500;
    padding: 10px;
    width: 100%;
    color: var(--white-main);
    border: none;
}
</style>