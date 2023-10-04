<script setup>
import {defineProps, ref} from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter();
const props = defineProps(['item']);
const item = ref(props.item);
const product = ref(item.value.product);
</script>

<template>
<div class="cart-item hover" v-if="product"
@click="router.push({name: 'product', params: {product_slug: product.slug}})">
    <div class="cart-item-left">
        <img class="cart-item-img" :src="product.main_product_image">
    </div>
    <div class="cart-item-right">
        <div class="right-left">
            <p class="item-name">{{ product.name }}</p>
            <div class="item-facts">
                <p>{{ product.type }}
                <span v-if="product.type == 'effect'">: {{ product.effect_type }}</span>
                </p>
                <p>Quantity left: {{ product.quantity }}</p>
            </div>
            <p class="item-manufacturer"
            @click="router.push({name: 'manufacturer', params: {man_slug: product.manufacturer.slug}})"
            >{{ product.manufacturer.name }}</p>
            <!-- <p class="item-date">added to cart: 04.09.2023 </p> -->
        </div>
        <div class="item-right">
            <div class="right-info" v-if="product.discount >0">
                <p class="item-price item-discounted">{{ Number(product.price).toFixed(2) }}</p>
                <p class="item-discount item-newprice">
                {{ Number(product.price * (1-product.discount)).toFixed(2) }}
                </p>
                <p>x{{item.quantity}}</p>
            </div>
            <div class="right-info" v-else>
                <p class="item-price">{{ Number(product.price).toFixed(2) }}</p>
                <p>x{{item.quantity}}</p>
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
    background-color: var(--white-main);
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
    object-fit: contain;
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