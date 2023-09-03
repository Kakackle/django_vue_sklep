<script setup>
// TODO: lepsze obrazki, opisy itd
// TODO: przesylanie jsona z sciezkami do obrazkow i tekstami w propach?
// 
</script>

<template>
<section class="f-section">
        <container class="f-item">
            <div class="f-left">
                <div class="f-bg color-second">
                    <img class="f-blob" src="../../static/img/home/blob_1.png">
                    <img class="f-img">
                </div>
            </div>
            <div class="f-right">
                <div class="f-title">ONLY THE BEST IMPORTED PARTS</div>
                <div class="f-subtitle">Ordered directly from the manufacturers</div>
                <div class="f-desc">Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium, velit sed? Vitae rem, quos libero consectetur aspernatur autem eos laudantium facere hic ducimus dolorum nisi ullam, accusamus harum natus facilis.</div>
            </div>
        </container>
        <container class="f-item">
            <div class="f-left">
                <div class="f-bg color-main">
                    <img class="f-blob" src="../../static/img/home/blob_2.png">
                    <img class="f-img">
                </div>
            </div>
            <div class="f-right">
                <div class="f-title">HANDCRAFTED ACCORDING TO YOUR NEEDS</div>
                <div class="f-subtitle">Ordered directly from the manufacturers</div>
                <div class="f-desc">Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium, velit sed? Vitae rem, quos libero consectetur aspernatur autem eos laudantium facere hic ducimus dolorum nisi ullam, accusamus harum natus facilis.</div>
            </div>
        </container>
        <container class="f-item">
            <div class="f-left">
                <div class="f-bg color-gray">
                    <img class="f-blob" src="../../static/img/home/blob_3.png">
                    <img class="f-img">
                </div>
            </div>
            <div class="f-right">
                <div class="f-title">HANDCRAFTED ACCORDING TO YOUR NEEDS</div>
                <div class="f-subtitle">Ordered directly from the manufacturers</div>
                <div class="f-desc">Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium, velit sed? Vitae rem, quos libero consectetur aspernatur autem eos laudantium facere hic ducimus dolorum nisi ullam, accusamus harum natus facilis.</div>
            </div>
        </container>
    </section>
</template>

<style scoped>
.f-section{
    margin: 0 auto;
    max-width: var(--max-page-width);
    height: 100%;
    display: flex;
    flex-direction: column;
    padding: 20px 40px;
    gap: 60px;
    margin-bottom: var(--section-margin);
}

.f-item{
    display: flex;
    margin: 0 auto;
    column-gap: 120px;
    row-gap: 20px;
    flex-wrap: wrap;
}

.f-left{
    display: flex;
    justify-content: center;
    align-items: center;
    /* max-width: 100%; */
    /* justify-self: center; */
    /* min-width: 300px; */
    position: relative;
}

@media (max-width: 760px) {
    .f-left{
        width: 100%;
    }
}

.f-bg{
    height: 200px;
    width: 200px;
    /* border-radius: 50%; */
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
}

/* .color-second{
    background-color: var(--second-main);
}

.color-main{
    background-color: var(--color-main);
}

.color-gray{
    background-color: var(--gray-main);
} */

.f-blob{
    position: absolute;
    width: 280px;
    height: 220px;
}

.f-img{
    height: 160px;
    width: 220px;
    background-color: var(--gray-lighter);
    border-radius: 20px;
    position: absolute;
    border: none;
}

.f-right{
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 10px;
}

.f-title{
    font-size: 30px;
    font-weight: 600;
}

.f-subtitle{
    font-size: 20px;
    font-weight: 500;
}

.f-desc{
    font-size: 15px;
    font-weight: 300;
    max-width: 600px;
}
</style>