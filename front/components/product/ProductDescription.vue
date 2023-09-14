<script setup>
</script>

<template>
<section class="desc-section">
    <div class="tabs">
        <p class="active">About</p>
        <p>Technical details</p>
        <p>Shipping and warranty</p>
        <p>Other</p>
    </div>
    <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Rem exercitationem labore molestias dolor iusto voluptates aperiam, voluptate dolorum doloremque corrupti provident reiciendis consectetur nisi. Dolore magnam eveniet similique at repudiandae.
        Lorem ipsum dolor sit dolor sit, amet consectetur adipisicing elit. Magnam, ab? Quod voluptate ipsa praesentium provident sapiente deserunt voluptas architecto itaque, sed quas ab dolores similique dignissimos exercitationem, molestiae sunt iusto.
    </p>
    <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Rem exercitationem labore molestias dolor iusto voluptates aperiam, voluptate dolorum doloremque corrupti provident reiciendis consectetur nisi. Dolore magnam eveniet similique at repudiandae.</p>
</section>
</template>

<style scoped>
.desc-section{
    max-width: var(--max-page-width);
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 20px;
    margin: 0 auto;
    margin-bottom: var(--section-margin);
}
.tabs{
    display: flex;
    gap: 10px;
    font-size: 24px;
}

.tabs p{
    font-size: 16px;
}

.active{
    font-weight: 600;
    text-decoration: underline;
}
</style>