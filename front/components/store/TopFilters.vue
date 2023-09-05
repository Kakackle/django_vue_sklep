<script setup>
</script>

<template>
    <div class="filters">
        <div class="filter-boxes">
            <span class="active">CENA</span>
            <span>PRODUCENT</span>
            <span>OPINIE</span>
        </div>
        <p>Liczba produktów: 99</p>
    </div>
</template>

<style scoped>
.filters{
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-right: auto;
}
.filters p{
    font-size: 10px;
    color: var(--gray-lighter);
}
.filter-boxes{
    display: flex;
    gap: 5px;
    flex-wrap: wrap;
}
.filter-boxes span{
    border: 1px solid var(--gray-lighter);
    padding: 5px;
    font-size: 16px;
    color: var(--gray-light);
}
.active{
    border-color: black;
    border-width: 1.5px;
    color: black;
}

</style>