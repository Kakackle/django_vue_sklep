<script setup>
import CartItem from "../components/CartItem.vue";
</script>

<template>
<div class="cart-left">
    <div class="cart-items">
        <CartItem></CartItem>
        <CartItem></CartItem>
        <CartItem></CartItem>
    </div>
    <div class="pagination">
        <p class="active">1</p>
        <p>2</p>
        <p>3</p>
        <p>...</p>
        <p>99</p>
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