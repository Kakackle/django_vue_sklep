<script setup>
import {ref, defineProps, defineEmits} from 'vue'; 
const props = defineProps(['images', 'selected_image']);
const images = ref(props.images);
const selected_image = ref(props.selected_image);
const emit = defineEmits(['photo_changed']);

const isSelectedImage = (index)=>{
    return {'active': selected_image.value === index};
}

const selectImage = (img, index)=>{
    emit('photo_changed', img, index);
}

</script>

<template>
<div class="photo-wheel unified-shadow" v-if="images" :key="selected_image">
    <img v-for="(img, index) in images" class="wheel-img"
    :src="img" :class="isSelectedImage(index)"
    @click="selectImage(img, index)">
    <!-- <img class="wheel-img" src="../../../static/img/products/yellow/yellow_front.png"> -->
</div>
</template>

<style scoped>
.photo-wheel{
    display: flex;
    flex-direction: column;
    padding: 10px;
    gap: 10px;
    overflow: hidden;
    height: 380px;
}

.wheel-img{
    height: 100px;
    width: 100px;
    object-fit: contain;
}

.active{
    background-color: var(--gray-lighter);
    border-radius: 20px;
}
</style>