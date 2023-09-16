<script setup>
// TODO: wlasciwie jak LineBar tylko inny slot i kolor tla
</script>

<template>
 <div class="shipping-banner">
    <ion-icon class="shipping-icon" name="car-outline"></ion-icon>
    <p class="promo">FREE SHIPPING WITH ORDERS OVER 250 ,-!</p>
</div>
</template>

<style scoped>
.shipping-banner{
    background-color: var(--green-main);
    color: var(--white-main);
    font-size: 20px;
    padding: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
}
.shipping-icon{
    width: 20px;
    height: 20px;
}
.promo{
    color: var(--white-main);
}
</style>