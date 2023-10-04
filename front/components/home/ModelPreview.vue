<script setup>
</script>

<template>
<section class="model-section">
    <p class="section-title">Take a closer look at one of our flagship models!</p>
    <model-viewer
        class="pedal-model"
        src="../../../static/img/products/yellow/model/scene.gltf"
        alt="guitar pedal model"
        auto-rotate
        camera-controls
        ar
        ios-src="../../../static/img/products/yellow/model/scene.gltf"
        shadow-intensity="0.5"
      ></model-viewer>
</section>
</template>

<style scoped>
.model-section{
    max-width: var(--max-page-width);
    width: 100%;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 20px;
    align-items: center;
    justify-content: center;
}
.pedal-model {
    height: 500px;
    width: 500px;
}
</style>