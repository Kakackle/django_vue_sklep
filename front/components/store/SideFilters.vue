<script setup>
import {ref, defineEmits} from 'vue'
import { useAxiosGet } from '../../composables/useAxiosGet';
const emit = defineEmits(['filter_type'])

const effect_types = ref();

const get_effect_types = async () => {
    const {data, error} = await useAxiosGet(`api/effecttypes/`);
    effect_types.value = data.value;
}

get_effect_types();

const selected_type = ref(0);
const selected_effect = ref(-1);
const search_value = ref('');

const filter_string = ref(``);
// effect, guitar, accessory

// kwestia resetowania tego query stringa po zmianie typu
const select_guitar = () => {
    selected_type.value = 1;
    selected_effect.value = -1;
    filter_string.value = '?';
    filter_string.value += '&type=guitar';
    emit('filter_type', filter_string.value);
}

const select_accessory = () => {
    selected_type.value = 2;
    selected_effect.value = -1;
    filter_string.value = '?';
    filter_string.value += '&type=accessory';
    emit('filter_type', filter_string.value);
}

const select_effect = () => {
    selected_type.value = 0;
    selected_effect.value = -1;
    filter_string.value = '?';
    filter_string.value += '&type=effect';
    emit('filter_type', filter_string.value);
}

const select_effect_type = (effect, index) => {
    selected_effect.value = index;
    filter_string.value = '?&type=effect';
    filter_string.value += `&effect_type=${effect.name}`;
    emit('filter_type', filter_string.value);
}

const search_by_name = () => {
    // if (!filter_string.value.includes(`&name=`))
    // filter_string.value += `&name=`;
    // if (!filter_string.value.includes(`&search=`))
    // filter_string.value += `&search=${search_value.value}`;
    emit(`filter_type`, filter_string.value + `&search=${search_value.value}`);
}

</script>

<template>
<div class="side">
    <div class="side-top">
        <p>CATALOGUE</p>
        <input type="search" placeholder="Search by name"
        v-model="search_value"
        @change="search_by_name">
    </div>
    <div class="side-lists">
        <ul class="side-list">
            <li class="side-category">
                <p :class="{'active': (selected_type === 0)}"
                class="hover-underline"
                @click="select_effect">Effects</p>
                <ul class="category-list" v-if="effect_types && selected_type === 0">
                    <!-- <li class="category-item"><p class="active">Distortion</p></li> -->
                    <li class="category-item hover-underline"
                    v-for="(effect, index) in effect_types" :key="effect"
                    @click="select_effect_type(effect, index)"
                    :class="{'active': (selected_effect===index)}">
                        <p>{{ effect.name }}</p>
                    </li>
                </ul>    
            </li>
            <li class="side-category hover-underline"
            :class="{'active': (selected_type === 1)}"
            @click ="select_guitar">
                <p>Guitars</p>
            </li> 
            <li class="side-category hover-underline"
            :class="{'active': (selected_type === 2)}"
            @click ="select_accessory"
            ><p>Accesories</p>
            </li> 
        </ul>
    </div>
</div>
</template>

<style scoped>
.side{
    display: flex;
    flex-direction: column;
    gap: 20px;
}
.side-top p{
    font-size: 30px;
    font-weight: 700;
}

.side-top input{
    font-size: 16px;
    background-color: var(--gray-lightest);
    color: var(--gray-light);
    border: none;
    width: 140px;
    padding: 5px;
}
.side-lists{
}

.side-list{
    list-style: none;
}

.side-category{
    font-size: 20px;
    margin-bottom: 5px;
}

.category-list{
    list-style: none;
    margin-top: 10px;
    margin-left: 10%;
}

.category-item{
    font-size: 20px;
}

.active{
            font-weight: 600;
        }
</style>