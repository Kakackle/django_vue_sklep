<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter();
const props = defineProps(['user', 'URLS'])
const user = ref(props.user)
</script>

<template>
    <div class="acc-drop">
        <div class="logged" v-if="user.is_authenticated">
            <div class="user">
                <img class="user-img" :src="user.profile_image">
                <p class="user-name">{{ user.username }}</p>
            </div>
            <a class="logout hover-underline"
            @click="router.push({name: 'user', params: {user_slug: user.username}})">Go to account</a>
            <a class="logout hover-underline" :href="URLS.logout">Logout</a>
        </div>
        <div class="logged" v-else>
            <p class="user-name">No user logged in</p>
            <a class="logout hover-underline" :href="URLS.login">Login</a>
            <a class="logout hover-underline" :href="URLS.signup">Sign up</a>
        </div>
    </div>
</template>

<style scoped>
.acc-drop{
    padding: 10px;
    border: 1px solid var(--gray-main);
    background-color: var(--white-main);
    z-index: 3;
}
.logged{
    display: flex;
    flex-direction: column;
    gap: 5px;
    align-items: center;
    min-width: 100px;
}

.user{
    display: flex;
    gap: 10px;
    align-items: center;
}
.user-img{
    height: 50px;
    width: 50px;
    border-radius: 50%;
    background-color: var(--gray-lighter);
}

.user-name{
    font-size: 16px;
    font-weight: 500;
}

.logout{
    color: var(--gray-main);
    font-size: 14px;;
    text-decoration: none;
}
</style>