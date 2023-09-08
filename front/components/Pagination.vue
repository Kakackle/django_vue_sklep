<script setup>
import {defineProps, defineEmits, ref} from 'vue'
const props = defineProps(['pages']);
const pages = ref(props.pages);
const emit = defineEmits(['page_change'])

const selected_page = ref(0);

const change_page = (link, page_index) =>{
    selected_page.value = page_index;
    console.log(`selected: ${selected_page.value}, index: ${page_index}`);
    emit('page_change', link, selected_page.value);
}


const is_selected = (page_index) => {
    return {'selected': selected_page.value === page_index }
}

</script>

<template>
    <div class="pages" v-if="pages" :key="selected_page">
        <p class="page" v-for="(page, page_index) in pages"
        @click="change_page(page[0], page_index)"
        :class="is_selected(page_index)" :key="page_index">
        {{ page[1] }}</p>
        <!-- <p>selected page: {{ selected_page }}</p> -->
    </div>
</template>

<style scoped>
.pages{
    display: flex;
    justify-content: center;
    font-size: 20px;
    gap: 1rem;
}
.page:hover{
    font-weight: 600;
    cursor: pointer;
}
.selected{
    font-weight: 700;
}
</style>