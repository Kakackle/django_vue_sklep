<script setup>
import { defineProps, ref, defineEmits } from 'vue';
import axios from 'axios';
const props = defineProps(['man',]);
const emit = defineEmits(['desc_update',]);

const man = ref(props.man);

const update_man_desc = (slug, man)=> {
    axios.patch(`api/manufacturers/${slug}`, {
        'description': man.description += ' 1',
        'csrfmiddlewaretoken': "Gd7syxIww0Krspr1IPqYi1Eq4vPNtQc3uBQeXkcInpeO05Clex6QQMZkaGxWR22E"
    })
    .then((res)=>{
        console.log(`desc updated`);
        emit('desc_update');
    })
    .catch((err)=>{
        console.log(err);
    })
}
</script>

<template>
<main class="man-main">
    <div class="user-info" v-if="man">
        <div class="user-left">
            <img class="user-img" :src="man.logo_image">
        </div>
        <div class="user-right">
            <p class="name">{{man.name}}</p>
            <p class="text">since: {{ man.date_created }}</p>
            <p class="bio">{{ man.description }}</p>
        </div>
    </div>
    <p v-else>No manufacturer details to display</p>
    <div v-if="man">
        <p>Update manufacturer desc:</p>
        <button class="button"
        @click="update_man_desc(man_slug, man)"
        >DESC += 1</button>
    </div>
</main>
</template>

<style scoped>
.man-main{
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.user-info{
    display: flex;
    gap: 20px;
    padding: 20px;
    margin: 0 auto;
}
.user-img{
    padding: 10px;
    border-radius: 50%;
    border: 4px solid var(--gray-main);
    width: 150px;
    height: 150px;
}

.user-right{
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.name{
    font-size: 24px;
    font-weight: 500;
    text-decoration: underline;
}

.text{
    font-size: 14px;
}

.bio{
    line-height: 1.5;
    width: 400px;
}
</style>