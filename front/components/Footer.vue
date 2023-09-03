<script setup>
// TODO: niekompletne to jest jakies
</script>

<template>
<section class="footer-section">
    <main class="footer">
        <div class="footer-col">
            <p class="footer-title"> Contact</p>
            <div class="footer-content">
                <p><ion-icon name="call-outline"></ion-icon>(+48) 592-203-458</p>
                <p><ion-icon name="mail-open-outline"></ion-icon>kalopsia@effects.com</p>
                <div class="socials">
                    <ion-icon class="footer-logo" name="logo-instagram"></ion-icon>
                    <ion-icon class="footer-logo" name="logo-facebook"></ion-icon>
                    <ion-icon class="footer-logo" name="logo-twitter"></ion-icon>
                    <ion-icon class="footer-logo" name="logo-amazon"></ion-icon>
                </div>
                <div class="address">
                    <p>Age Street 01-245</p>
                    <p>Queens, NY</p>
                    <p>ZZ District 55</p>
                </div>
            </div>
        </div>
        <div class="footer-col">
            <p class="footer-title"> About Kalopsia</p>
            <div class="footer-content"></div>
        </div>
        <div class="footer-col">
            <p class="footer-title"> Our Partners</p>
            <div class="footer-content"></div>
        </div>
        <div class="footer-col">
            <p class="footer-title"> Help</p>
            <div class="footer-content"></div>
        </div>
        <div class="footer-col">
            <p class="footer-title"> Legal</p>
            <div class="footer-content"></div>
        </div>
    </main>
</section>
</template>

<style scoped>
.footer-section{
    background-color: var(--color-main);
}

.footer{
    max-width: var(--max-page-width);
    margin: 0 auto;
    display: flex;
    flex-wrap: wrap;
    /* gap: 2rem; */
    justify-content: space-around;
    padding: 20px;
}

.footer-col{
    display: flex;
    flex-direction: column;
    align-items: start;
    /* width: 100%; */
    gap: 20px;
}

.footer-title{
    font-size: 20px;
    font-weight: 500;
    color: var(--white-main);
    text-decoration: underline;
}

.footer-content{
    display: flex;
    flex-direction: column;
    font-size: 20px;
    font-weight: 300;
    color: var(--white-main);
    gap: 10px;
}

.footer-content p{
    display: flex;
    gap: 5px;
    align-items: center;
}

.footer-logo{
    height: 20px;
    width: 20px;
}

.socials{
    display: flex;
    justify-content: center;
    gap: 5px;
    font-size: 50px;
}

.address{
    font-size: 15px;
}

</style>