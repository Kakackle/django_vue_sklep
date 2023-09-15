<script setup>
import { defineProps, ref, defineEmits } from 'vue';
import { useUser } from '../../composables/useUser';
const props = defineProps(['man',]);
const emit = defineEmits(['desc_update',]);
const man = ref(props.man);
const user = useUser();
import { formatDate } from '../../composables/formatDate';
const URLS = JSON.parse(document.getElementById('URLS').textContent);
const base_path = URLS.base_path;
const edit_url = base_path + `/backend/manufacturers/${man.value.slug}/update`;
</script>

<template>
<main class="man-main">
    <div class="user-info" v-if="man">
        <div class="user-left">
            <img class="user-img" :src="man.logo_image">
        </div>
        <div class="user-right">
            <p class="name">{{man.name}}</p>
            <p class="text">since: {{ formatDate(man.date_created) }}</p>
            <p class="bio">{{ man.description }}</p>
            <a class="edit hover-underline"
            v-if="man.owner.username === user.username"
            :href="edit_url"
            >Edit manufacturer</a>
        </div>
    </div>
    <p v-else>No manufacturer details to display</p>
    <!-- <div v-if="man">
        <p>Update manufacturer desc:</p>
        <button class="button"
        @click="update_man_desc(man.slug, man)"
        >DESC += 1</button>
    </div> -->
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
    /* border-radius: 50%; */
    border: 4px solid var(--gray-main);
    width: 180px;
    height: 100px;
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

.edit{
    text-decoration: none;
    color: var(--gray-main);
}
</style>