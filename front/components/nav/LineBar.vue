<script setup>
// TODO: przyjmowanie w propie co wyswietlac na lewo (tytul) i jakie przedmioty?

</script>

<template>
    <section class="accolades">
        <div class="accolades-main">
            <p class="accolades-left">AS SEEN IN:</p>
            <div class="accolades-center">
                <p class="accolades-item">Rock Magazine #134</p>
                <p class="accolades-item">Insider</p>
                <p class="accolades-item">Scaruffi</p>
                <p class="accolades-item">Pitchfork #134</p>
            </div>
        </div>
    </section>
</template>

<style scoped>
.accolades{
    background-color: var(--dark-main);
    width: 100%;
}

.accolades-main{
    max-width: var(--max-page-width);
    display: flex;
    color: var(--white-main);
    font-size: 20px;
    height: 40px;
    align-items: center;
    padding: 5px;
    margin: 0 auto;
}

.accolades-left{
    font-weight: 700;
}

.accolades-center{
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 5px;
    width: 60%;
    margin: 0 auto;
}

.accolades-item{
    height: 20px;
    font-size: 16px;
}
</style>