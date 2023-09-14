<script setup>
import { useAxiosGet } from '../../composables/useAxiosGet';
import { useAxiosPost } from '../../composables/useAxiosPost';

import {ref, defineProps, defineEmits} from 'vue';
import {useRouter} from 'vue-router';
const router = useRouter();
const props = defineProps(['user', 'cart']);
const user = ref(props.user);
const cart = ref(props.cart);

const addr_url = `api/address/?user=${user.value.username}`;
const user_addresses = ref();
const new_address = ref();
const address = ref();

const new_street = ref();
const new_number = ref();
const new_country = ref();
const new_zipcode = ref();

const getUserAdresses = async (link) => {
    const {data, error} = await useAxiosGet(link);
    user_addresses.value = data.value;
    console.log(`addresses: ${JSON.stringify(user_addresses.value)}`);
}
getUserAdresses(addr_url);

const shipping_method = ref();
const methods = ref();

const getShippingMethods = async () => {
    const {data, error} = await useAxiosGet(`api/shippings/`);
    methods.value = data.value;
    console.log(`metods: ${JSON.stringify(methods.value)}`);
}

getShippingMethods();

const promo_code = ref();
const discount = ref({
    discount: 0,
});

const getDiscount = async () =>{
    const {data, error} = await useAxiosGet(`api/discounts/${promo_code.value}/`);
    discount.value = data.value;
} 

const createOrder = async () => {
    const url = `api/orders/`;
    let newData = {};
    if (address.value)
    {
        newData.address = address.value.id;
    }
    else{
        newData.new_address = true;
        newData.country = new_country.value;
        newData.street = new_street.value;
        newData.street_number = new_number.value;
        newData.zipcode = new_zipcode.value;
    }
    if (discount)
    {
        newData.discount = discount.value.discount;
    }
    else{
        newData.discount = 0;
    }

    newData.shipping_method = shipping_method.value.name;
    console.log(`shipping: ${JSON.stringify(shipping_method.value)}`)

    const {data, error} = await useAxiosPost(url, newData);
    // emit()
}

</script>

<template>
<div class="cart-right">
    <div class="shipping-div">
        <p class="input-title">WYBIERZ SPOSÓB DOSTAWY</p>
        <select class="input-select" v-model="shipping_method" v-if="methods">
            <option class="input-option"
            v-for="(met, index) in methods" :key="met"
            :value="met">{{ met.name }} - {{ met.price }} ({{ met.days_minimum }} days min.)
            </option>
        </select>
    </div>
    <div class="addr-div">
        <p class="input-title">WPISZ ADRES LUB WYBIERZ Z LISTY</p>
        <!-- czemu na froncie ten select sie pojawia ale pusty... -->
        <select class="input-select" v-model="address"
        v-if="user_addresses">
            <option class="input-option"
            v-for="(add, index) in user_addresses" :key="add"
            :value="add">{{ add.street }} {{ add.street_number }} {{ add.country }}
            </option>
        </select>
        <div class="label-div">
            <label class="addr-label" for="street">Street</label>
            <input class="input-gray" type="text" name="street" v-model="new_street">
        </div>
        <div class="label-div">
            <label class="addr-label" for="streetn">Street number</label>
            <input class="input-gray" type="number" name="streetn" v-model="new_number">
        </div>
        <div class="label-div">
            <label class="addr-label" for="country">Country</label>
            <input class="input-gray" type="text" name="country" v-model="new_country">
        </div>
        <div class="label-div">
            <label class="addr-label" for="zipcode">Zipcode</label>
            <input class="input-gray" type="number" name="zipcode" v-model="new_zipcode">
        </div>
    </div>
    <div class="label-div">
        <label class="promo-label" for="promo">WPISZ KOD PROMOCYJNY</label>
        <input class="input-white" type="text" name="promo" v-model="promo_code">
    </div>
    <button v-if="promo_code" @click="getDiscount"
    class="hover">apply promo</button>
    <p v-if="discount">discount applied: {{ discount.name }}</p>
    <p class="total-items">Total items: {{ cart.sum_items }}</p>
    <div class="price-div">
        <p class="item-discount item-newprice">{{ cart.sum_cost * (1-discount.discount) }}</p>
        <p class="item-price item-discounted" v-if="discount"
        >{{ cart.sum_cost }}</p>
    </div>
    <div class="button-div">
        <button class="order-button hover"
        @click="createOrder">ORDER</button>
        <a class="back-button hover"
        @click="router.push({name: 'home'})">go back to shopping</a>
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