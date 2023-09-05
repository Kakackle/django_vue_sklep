<script setup>
</script>

<template>
<div class="order-small unified-border">
    <div class="order-left">
        <p class="order-number">Order no. #0431921</p>
        <p class="items-title">Items ordered:</p>
        <div class="order-items">
            <p>The Yellow Menace - 1 x 199,99 = 199,99</p>
            <p>The Blue Guitar - 2 x 99,99 = 199,98</p>
            <p class="total">total: 399,97</p>
        </div>
    </div>
    <div class="order-right">
        <p class="text-right">ordered on: 04.09.2023</p>
        <p class="text-right">status: paid [04.09.2023]</p>
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