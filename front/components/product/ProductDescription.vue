<script setup>
import { ref, defineProps, defineEmits } from 'vue';
const props = defineProps(['product']);
const product = ref(props.product);
// about, technical, shipping/waranty, other
const tabs = [
    {
        title: 'About',
        content: product.value.about
    },
    {
        title: 'Technical',
        content: product.value.technical
    },
    {
        title: 'Shipping & warranty',
        content: `warranty: ${product.value.warranty}, shipping: ${product.value.shipping}`
    },
    {
        title: 'Other',
        content: product.value.other
    },
]

const selected_tab = ref(0);

</script>

<template>
<section class="desc-section">
    <div class="tabs" v-if="tabs">
        <p v-for="(tab, index) in tabs"
        @click="selected_tab=index"
        class="tab hover-underline"
        :class="{'active': (selected_tab===index)}">{{ tab.title }}</p>
    </div>
    <div class="tab-content" v-if="tabs" :key="selected_tab">
        <p class="tab-p">{{ tabs[selected_tab].content }}</p>
    </div>
</section>
</template>

<style scoped>
.desc-section{
    max-width: var(--max-page-width);
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 20px;
    margin: 0 auto;
    margin-bottom: var(--section-margin);
}
.tabs{
    display: flex;
    /* gap: 10px; */
    font-size: 24px;
}
.tab {
    padding: 4px 10px;
    border-radius: 1px;
    border: 1px solid var(--gray-lighter);
    font-size: 16px;
}

.tab-content{
    padding: 10px;
    border: 1px solid var(--gray-lightest);
}

.active{
    font-weight: 600;
    text-decoration: underline;
}
</style>