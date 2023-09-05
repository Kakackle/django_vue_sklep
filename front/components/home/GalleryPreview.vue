<script setup>
// TODO: dynamiczne
// TODO: link do sklepu
</script>

<template>
    <section class="gallery-section">
        <p class="section-title">Reach out to the sun</p>
        <container class="gallery-imgs">
            <img class="gallery-img">
            <img class="gallery-img">
            <img class="gallery-img">
            <img class="gallery-img">
            <img class="gallery-img">
            <img class="gallery-img">
            <img class="gallery-img">
            <img class="gallery-img">
            <img class="gallery-img">
            <img class="gallery-img">
            <img class="gallery-img">
            <img class="gallery-img">
            <img class="gallery-img">
            <img class="gallery-img">
            <img class="gallery-img">
            <img class="gallery-img">
        </container>
        <button class="gallery-button">GO TO STORE &rarr;</button>
    </section>
</template>

<style scoped>
.gallery-section{
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 10px;
    margin-bottom: var(--section-margin);
}

.gallery-imgs{
    max-width: var(--max-page-width);
    /* width: 100%; */
    max-height: 320px;
    /* border: 2px solid black; */
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    overflow: auto;
    gap: 30px;
    padding: 40px;
}

.gallery-img{
    width: 150px;
    height: 150px;
    background-color: var(--gray-lighter);
}

.gallery-button{
    border: 5px solid var(--second-main);
    background-color: var(--white-main);
    padding: 5px;
    font-size: 20px;
    font-weight: 500;
    border-radius: 10px;
}

.gallery-button:hover{
    cursor: pointer;
    filter: brightness(0.75);
}

</style>