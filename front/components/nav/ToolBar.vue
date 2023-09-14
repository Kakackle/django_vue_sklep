<script setup>
import { ref } from 'vue';
const switchActive = ref(0);
</script>

<template>
    <section class="toolbar">
        <div>
            <ion-icon name="moon-outline"></ion-icon>
            <div class="switch-outer hover" @click="switchActive =!switchActive">
                <!-- <div class="switch-inner" :class="{switchActive ? 'switch-inner-left' : 'switch-inner-right'}"
                ></div> -->
                <div class="switch-inner" :class="{'switch-inner-left': switchActive, 'switch-inner-right': !switchActive}"
                ></div>
            </div>
            <ion-icon name="sunny-outline"></ion-icon>
        </div>
        <div>
            <ion-icon name="language-outline"></ion-icon>
            <p class="lang">ENG</p>
        </div>
        <div>
            <ion-icon name="logo-euro"></ion-icon>
            <p class="lang">EUR</p>
        </div>
    </section>
</template>

<style scoped>
.toolbar{
    width: 100%;
    display: flex;
    justify-content: end;
    align-items: center;
    gap: 20px;
    background-color: var(--gray-main);
    color: var(--white-main);
    padding: 2px 20px;
}

.toolbar div{
    display: flex;
    align-items: center;
    gap: 5px;
}

.lang{
    font-size: 16px;
}

.switch-outer{
    width: 50px;
    height: 10px;
    background-color: var(--gray-light);
    border-radius: 10px;
}

.switch-inner{
    width: 30px;
    height: 10px;
    background-color: var(--white-main);
    border-radius: 10px;
    /* margin-left: auto; */
}
.switch-inner-left{
    margin-left: auto;
}
.switch-inner-right{
    margin-right: auto;
}

</style>