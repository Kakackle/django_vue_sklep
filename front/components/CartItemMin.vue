<script setup>
</script>

<template>
<div class="cart-item">
    <div class="cart-item-left">
        <img class="cart-item-img" src="">
    </div>
    <div class="cart-item-right">
        <div class="right-left">
            <p class="item-name">The Yellow Menace</p>
            <div class="item-facts">
                <p>Effect: fuzz</p>
                <p>Quantity left: 4</p>
            </div>
            <p class="item-manufacturer">Kalopsia Effects</p>
            <p class="item-date">added to cart: 04.09.2023 </p>
        </div>
        <div class="item-right">
            <div class="right-info">
                <p class="item-price item-discounted">199.99</p>
                <p class="item-discount item-newprice">99.99</p>
            </div>
            <!-- <div class="right-controls">
                <ion-icon class="fav-icon" name="star-outline"></ion-icon>
                <ion-icon class="fav-icon" name="trash-outline"></ion-icon>
            </div> -->
        </div>
    </div>
</div>
</template>

<style scoped>
.cart-item{
    display: flex;
    padding: 10px;
    /* border: 1px solid var(--gray-lighter); */
    border-bottom: 1px solid var(--gray-main);
    gap: 10px;
    width: 100%;
}

.cart-item-left{
    padding: 0px 10px;
    display: flex;
    justify-content: center;
    align-items: center;

}

.cart-item-img{
    background-color: var(--gray-lighter);
    width: 100px;
    height: 100px;
}

.cart-item-right{
    width: 100%;
    display: flex;
    justify-content: space-between;
}

.right-left{
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.item-name{
    color: var(--gray-main);
    font-size: 16px;
    font-weight: 500;
}

.item-facts{
    display: flex;
    gap: 10px;
}

.item-facts p{
    font-size: 12px;
    font-weight: 300;
    color: var(--gray-lighter);
}

.item-manufacturer{
    font-size: 12px;
    color: var(--gray-light);
    font-weight: 500;
}

.item-date{
    font-size: 12px;
    color: var(--gray-lighter);
    font-weight: 300;
}

.right-info{
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.item-right{
    display: flex;
    gap: 10px;
}

.item-price{
    color: var(--gray-main);
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

/* .item-quantity{
    display: flex;
    padding: 2px;
    align-items: center;
    gap: 5px;
} */
.item-quantity{
    font-size: 14px;
    border: 1px solid var(--gray-main);
    color: var(--gray-main)
}

.right-controls{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    /* padding: 10px 0; */
}

.fav-icon{
    font-size: 14px;
    color: var(--gray-lighter);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
</style>