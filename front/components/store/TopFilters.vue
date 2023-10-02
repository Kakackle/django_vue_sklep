<script setup>
import {ref, defineEmits, defineProps} from 'vue';
const emit = defineEmits(['ordering']);
const props = defineProps(['count']);
const count = props.count;

const order_options = [
    {
        title: 'PRICE',
        value: 'price'
    },
    {
        title: 'MANUFACTURER',
        value: 'manufacturer__name'
    },
    {
        title: 'RATING',
        value: 'rating_average'
    },
    {
        title: 'BOUGHT COUNT',
        value: 'bought_count'
    },
]

const selected_order = ref(-1);
const order_by = (value, index) => {
    selected_order.value = index;
    emit('ordering', `&ordering=${value}`)
}

</script>

<template>
    <div class="filters">
        <p class="sort-title">Sort results</p>
        <div class="filter-boxes">
            <span v-for="(order, index) in order_options"
            @click="order_by(order.value, index)"
            class="hover"
            :class="{'active': (selected_order===index)}"
            >{{ order.title }}</span>
        </div>
        <p>Products found: {{ count }}</p>
    </div>
</template>

<style scoped>
.filters{
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-right: auto;
}
.filters p{
    font-size: 10px;
    color: var(--gray-lighter);
}

.sort-title{
    font-size: 16px;
}
.filter-boxes{
    display: flex;
    gap: 5px;
    flex-wrap: wrap;
}
.filter-boxes span{
    border: 1px solid var(--gray-lighter);
    padding: 5px;
    font-size: 16px;
    color: var(--gray-light);
}
.active{
    background-color: var(--gray-lighter);
}

</style>