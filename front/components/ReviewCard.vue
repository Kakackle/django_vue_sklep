<script setup>
// TODO: dynamiczne z propow przeslanych z ReviewsSecion np
</script>

<template>
    <div class="rev-outer unified-shadow">
        <div class="rev-inner">
            <img class="rev-img" src="">
            <p class="rev-desc">"Lorem ipsum, dolor sit amet consectetur adipisicing elit.
                Voluptates quo quisquam qui aperiam nemo facilis aliquam blanditiis excepturi
                harum perferendis iure praesentium fugit, laudantium non alias,
                voluptatem maiores neque! Officiis?"</p>
        </div>
        <p class="rev-author">- Stu from KGLW</p>
    </div>
</template>

<style scoped>
.rev-outer{
    /* height: 180px; */
    width: 200px;
    /* @include unified-shadow; */
    padding: 10px;
    display: flex;
    flex-direction: column;
    flex-shrink: 0;
    gap: 5px;
}

.rev-inner{

}

.rev-img{
    height: 60px;
    width: 60px;
    border-radius: 50%;
    background-color: var(--gray-lighter);
    float: left; /* for text wrapping around image */
    margin: 5px;
}

.rev-desc{
    margin-top: 10px;
    font-size: 11px;
}
.rev-author{
    font-size: 12px;
    color: var(--gray-lighter);
    margin-left: auto;
}

</style>