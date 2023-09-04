<script setup>
// generalny komponent na dropdown z itemai podanymi
// TODO: jakies przekazywanie funkcji do tych itemow?
// TODO: i moze slot by sie przydal gdybys chcial nie tylko tekst ale..
const props = defineProps(['items', 'bgcolor', 'color', 'fontsize']);
</script>

<template>
    <ul class="dropdown" :style="{backgroundColor: props.bgcolor, color:props.color}">
        <li v-for="(item, index) in props.items" :key="index"
        :style="{fontSize: props.fontsize + 'px'}">{{ item }}</li>
    </ul>
</template>

<style scoped>
.dropdown{
    display: flex;
    flex-direction: column;
    gap: 2px;
}
</style>