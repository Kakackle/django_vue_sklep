<script setup>
</script>

<template>
    <section class="end-section">
        <p id="end1">Still need help? Reach out to our team through the contant info below</p>
        <p id="end2">Otherwise, keep on rocking in the free world with...</p>
        <img src="../../../static/img/kalopsia.png">
    </section>
</template>

<style scoped>
.end-section{
    max-width: var(--max-page-width);
    display: flex;
    flex-direction: column;
    padding: 10px 40px;
    margin: 0 auto;
}

.end-section p{
    font-size: 15px;
    color: var(--gray-main);
    font-weight: 500;
}

#end1{
    margin-right:auto;
}

#end2{
    margin-left: auto;
}
.end-section img{
    width: 250px;
    margin: 0 auto;
}

</style>