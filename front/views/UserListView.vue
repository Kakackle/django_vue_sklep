<script setup>
import {ref} from "vue"
import axios from "axios";

import UserListItem from "../components/user/UserListItem.vue";
import Pagination from "../components/Pagination.vue";

const url = "api/profiles/";

const profiles = ref([]);
const pages = ref([])

const getProfiles = function(link){
    axios.get(link)
    .then((res)=>{
        profiles.value = res.data.results;
        pages.value = res.data.context.page_links;
        console.log(res);
    })
    .catch((err)=>{
        console.log(err);
    })
}

getProfiles(url);

const change_page = (link, page_index)=>{
    getProfiles(link);
}

</script>

<template>
    <main class="user-list main">
        <div class="user-list" v-if="profiles" :key="profiles">
            <UserListItem v-for="(profile, index) in profiles"
            :profile="profile" class="list-item" :key="index"></UserListItem>
        </div>
        <p v-else>No users to display</p>
        <Pagination :pages="pages" @page_change="change_page"
        v-if="pages"></Pagination>
    </main>
</template>

<style scoped>
.main{
    align-items: center;
}
.user-list{
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.list-item{
    border-bottom: 1px solid var(--gray-light);
}
</style>