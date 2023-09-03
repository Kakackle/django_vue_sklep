<script setup>
// TODO: dynamiczne
// TODO: rozdzial na komonenty
// TODO: hovery i funkcjonalnosci zmiany zdjecia itd
// TODO: requesty na buy, add itd
// TODO: i moze wszedzie: kolro czcionki zamiast czarnego jakis prawie-czarny
import ProductPhotos from './ProductPhotos.vue';
</script>

<template>
<section class="product-section">
    <div class="product-left">
        <ProductPhotos></ProductPhotos>
    </div>
    <div class="product-right">
        <p class="manufacturer">Kalopsia effects</p>
        <div class="product-title"><p>THE YELLOW MENACE</p></div>
        <div class="product-rating">
            <ion-icon name="star-outline"></ion-icon>
            <p class="numbers">4.56/5</p>
            <p>see all reviews</p>
        </div>
        <div class="facts">
            <p>5 Facts:</p>
            <ul>
                <li>Distortion</li>
                <li>Fuzzy</li>
                <li>Compact</li>
                <li>9V Powered</li>
                <li>2 Year warranty</li>
            </ul>
        </div>
        <div class="price">
            <p class="price-text">349.00 ,-</p>
            <p class="free">free shipping included*</p>
        </div>
        <button class="buy-button">BUY NOW</button>
        <div class="buy-options">
            <div>
                <ion-icon class="rating-icon" name="star-outline"></ion-icon>
                <p class="buy-option">ADD TO FAVOURITES</p>
            </div>
            <p>or</p>
            <div>
                <ion-icon class="rating-icon" name="cart-outline"></ion-icon>
                <p class="buy-option">ADD TO CART</p>
            </div>
        </div>
    </div>
</section>
</template>

<style scoped>
.product-section{
    max-width: var(--max-page-width);
    display: flex;
    padding: 20px;
    gap: 40px;
    flex-wrap: wrap;
    margin: 0 auto;
    margin-bottom: var(--section-margin);
}

.product-right{
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    /* gap: 5px; */
    width: 350px;
    margin: 0 auto;
}
.manufacturer{
    margin-left: auto;
    font-size: 12px;
    font-weight: 500;
}
.product-title{
    background-color: var(--gray-lightest);
    padding: 10px;
}

.product-title p{
    font-size: 40px;
}

.product-rating{
    display: flex;
    gap: 10px;
    justify-content: center;
    align-items: center;
    font-size: 20px;
}
.rating-icon{
    width: 25px;
    height: 25px;
}
.numbers{
    font-size: 30px;
}

.facts{
    display: flex;
    flex-direction: column;
    gap: 5px;
    font-size: 24px;
}

.facts p{
    font-weight: 700;
}

.facts ul{
    list-style: none;
    font-size: 18px;
}

.price{
    display: flex;
    flex-direction: column;
    align-items: end;
    margin-left: auto;
}
.price-text{
    font-size: 24px;
    font-weight: 500;
}
.free{
    font-size: 12px;
    color: var(--gray-light);
}
.buy-button{
    background-color: var(--color-main);
    color: var(--white-main);
    padding: 10px;
    border: none;
    font-size: 24px;
}
.buy-options{
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    font-size: 20px;
}
/* 
.buy option{
    font-size: 
} */

.buy-options div{
    display: flex;
    align-items: center;
    gap: 5px;
}
</style>