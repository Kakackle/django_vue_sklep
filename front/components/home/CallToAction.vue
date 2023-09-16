<script setup>
import { useAxiosPost } from '../../composables/useAxiosPost';
import { useToast } from 'vue-toastification';
import { ref } from 'vue';
const newEmail = ref();
const newName = ref();
const newFrequency = ref();
const post_url = `api/subscribers/`;

const postSubscriberForm = async (link) => {
    let newData = {
        'email': newEmail.value,
        'name': newName.value,
        'frequency': newFrequency.value
    }
    const {data, error} = await useAxiosPost(link, newData);
    useToast(data, error, 'succesfully subscribed', 'failed to subscribe');
    newEmail.value = undefined;
    newName.value = undefined;
    newFrequency.value = undefined;
}
</script>

<template>
<section class="cta-section">
    <div class="cta-center-div">
    <container class="cta-container">
        <div class="cta-left cta-item">
            <img class="cta-img" src="../../../static//img/cta.png">
        </div>
        <div class="cta-center cta-item">
            <div class="cta-title">
                <p>Want to know more?</p>
                <p>Sign up for our newsletter!</p>
            </div>
            <div class="cta-inputs">
                <div class="label-div">
                    <label class="cta-label" for="cta-mail">Your e-mail:</label>
                    <input class="cta-input" type="email" id="cta-mail"
                     placeholder="example@gmail.com" v-model="newEmail">
                </div>
                <div class="label-div">
                    <label class="cta-label" for="cta-name">Your name:</label>
                    <input class="cta-input" type="text" id="cta-name"
                     placeholder="John Smith" v-model="newName">
                </div>
                <div class="label-div">
                    <label class="cta-label"  for="cta-frequency">How often would you like to receive this newsletter?</label>
                    <select class="cta-select" id="cta-frequency" v-model="newFrequency">
                        <option value=7>Weekly</option>
                        <option value=14>Bi-weekly</option>
                        <option value=31>Once a month</option>
                    </select>
                </div>
            </div>
        </div>
        <div class="cta-right cta-item">
            <p>Hope we see you there! (We won't spam your inbox, we promise)</p>
            <div class="cta-go hover" @click="postSubscriberForm(post_url)">
                <p>></p>
            </div>
        </div>
    </container>
    </div>
</section>
</template>

<style scoped>
.cta-section{
    width: 100%;
    background-color: var(--color-main);
    display: flex;
    justify-content: center;
    margin-bottom: var(--section-margin);
}

.cta-center-div{
    width: 900px;
}

.cta-container{
    background-color: var(--color-main);
    /* max-width: 900px; */
    /* border: 1px solid black;
    display: flex;
    justify-content: center; */
    display: grid;
    /* grid-template-columns: repeat(3,1fr); */
    grid-template-columns: repeat(auto-fill, 300px);
    /* height: 320px; */
}

.cta-item{
    /* border: 1px solid $gray-lighter; */
    display: flex;
    justify-content: center;
    align-items: center;
}

.cta-left{
    padding: 10px;
}

.cta-img{
        width: 300px;
        height: 300px;
    }

.cta-center{
    display: flex;
    flex-direction: column;
    gap: 20px;
    justify-content: start;
    padding: 20px;
}

.cta-title{
    font-size: 30px;
    color: var(--white-main);
    font-weight: 500;
    /* margin-right: auto; */
}

.cta-inputs{
    display: flex;
    flex-direction: column;
    align-items: start;
    /* width: 100%; */
    gap: 10px;
}

.label-div{
    display: flex;
    flex-direction: column;
}

.cta-label{
    font-size: 10px;
    color: var(--white-main);
}

.cta-input, .cta-select{
    height: 25px;
    width: 250px;
    font-size: 15px;
    /* @include bg-with-opacity($gray-main, 0.75); */
    background-color: var(--gray-main);
    filter: opacity(0.8);
    border-radius: 5px;
    border: none;
    color: var(--white-main);
    padding: 0 10px;
}

.cta-right{
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.cta-right p{
    font-size: 20px;
    color: var(--white-main);
    font-weight: 300;
}

.cta-go{
    background-color: var(--second-main);
    /* padding: 20px; */
    width: 50px;
    height: 50px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.cta-go p{
    color: var(--white-main);
    font-size: 35px;
    font-weight: 500;
}

</style>