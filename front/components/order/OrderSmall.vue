<script setup>
import {ref, defineProps} from 'vue'
const props = defineProps(['order']);
const order = ref(props.order);
</script>

<template>
<div class="order-small unified-border" v-if="order">
    <div class="order-left">
        <!-- TODO: moze wlasnie jakis taki number generowany jako slug etc -->
        <p class="order-number">Order no. #0431921</p>
        <!-- TODO: count -->
        <p class="items-title">Items ordered:</p>
        <div class="order-items" v-if="order.products">
            <p v-for="(product, index) in order.products" :key="index">
            {{ product.name }} - {{ product.price }}</p>
            <!-- <p>The Yellow Menace - 1 x 199,99 = 199,99</p>
            <p>The Blue Guitar - 2 x 99,99 = 199,98</p> -->
            <!-- TODO: suma kalkulowanna -->
            <p class="total">total: 399,97</p>
        </div>
    </div>
    <div class="order-right">
        <p class="text-right">ordered on: {{ order.date_ordered }}</p>
        <p class="text-right">status: {{ order.status }} [{{ order.date_updated }}]</p>
    </div>
</div>
</template>

<style scoped>
.order-small{
    display: flex;
    padding: 10px;
    justify-content: space-between;
    width: 100%;
    background-color: var(--white-main);
}

.order-left, .order-right, .order-items{
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.order-items{
    gap: 5px;
}

.order-items p{
    font-size: 12px;
    font-weight: 400;
    color: var(--gray-light);
}

.total{
    color: var(--gray-main);
    font-size: 14px;
}

.items-title, .text-right{
    font-size: 12px;
}

.order-number{
    font-size: 20px;
    font-weight: 500;
}

</style>