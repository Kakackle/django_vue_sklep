<script setup>
import CartItemMin from './CartItemMin.vue';
</script>

<template>
    <div class="cart-drop">
        <CartItemMin></CartItemMin>
        <CartItemMin></CartItemMin>
        <CartItemMin></CartItemMin>
        <p class="total">TOTAL: 349,96</p>
        <button class="go-button hover">TO CART -></button>
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