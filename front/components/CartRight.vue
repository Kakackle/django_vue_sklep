<script setup>
</script>

<template>
<div class="cart-right">
    <div class="shipping-div">
        <p class="input-title">WYBIERZ SPOSÓB DOSTAWY</p>
        <select class="input-select">
            <option class="input-option">Kurier - 15,99</option>
            <option class="input-option">Inpost - 10,99</option>
            <option class="input-option">Inpost - 10,99</option>
        </select>
    </div>
    <div class="addr-div">
        <p class="input-title">WPISZ ADRES LUB WYBIERZ Z LISTY</p>
        <div class="label-div">
            <label class="addr-label" for="addr1">addr 1</label>
            <input class="input-gray" type="text" name="addr1">
        </div>
        <div class="label-div">
            <label class="addr-label" for="addr2">addr 2</label>
            <input class="input-gray" type="text" name="addr2">
        </div>
    </div>
    <div class="label-div">
        <label class="promo-label" for="promo">WPISZ KOD PROMOCYJNY</label>
        <input class="input-white" type="text" name="promo">
    </div>
    <p class="total-items">Total items: 3</p>
    <div class="price-div">
        <p class="item-discount item-newprice">99.99</p>
        <p class="item-price item-discounted">199.99</p>
    </div>
    <div class="button-div">
        <button class="order-button hover">ORDER</button>
        <a class="back-button hover">go back to shopping</a>
    </div>
</div>
</template>

<style scoped>
.cart-right{
    /* width: clamp(200px, 100%, 400px); */
    padding: 10px;
    border: 1px solid var(--gray-light);
    display: flex;
    flex-direction: column;
    gap: 16px;
    height: 100%;
}

.shipping-div{
    display: flex;
    flex-direction: column;
    gap: 2px;
}

.input-title{
    font-size: 16px;
    font-weight: 400;
}

.label-div{
    display: flex;
    flex-direction: column;
}

.addr-div{
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.addr-label{
    font-size: 10px;
}

.input-gray{
    background-color: var(--gray-lighter);
    border: none;
    height: 16px;
    padding: 4px 2px;
}

.input-white{
    background-color: var(--white-main);
    padding: 2px 2px;
    border: 1px solid var(--gray-light);
}

.total-items{
    font-size: 12px;
    color: var(--gray-light);
}

.price-div{
    display: flex;
    align-items: center;
    gap: 10px;
}

.button-div{
    display: flex;
    flex-direction: column;
}

.order-button{
    font-size: 32px;
    padding: 4px;
    color: var(--color-main);
    background-color: var(--white-main);
    border: 1px solid var(--gray-main);
    border-bottom: 8px solid var(--color-main);
}

.back-button{
    font-size: 12px;
    color: var(--gray-light);
    font-weight: 500;
    align-self: flex-end;
}


.item-price{
    font-size: 24px;
    font-weight: 500;
}
.item-discount{
    font-size: 12px;
    color: var(--gray-lighter);
}
.item-discounted{
    text-decoration: line-through;
}
.item-newprice{
    font-size: 26px;
    font-weight: 500;
    color: var(--green-main);
}
</style>