<script setup>
</script>

<template>
<div class="side">
    <div class="side-top">
        <p>KATALOG</p>
        <input type="search" placeholder="Search">
    </div>
    <div class="side-lists">
        <ul class="side-list">
            <li class="side-category">
                <p>Wzmacniacze</p>
            </li> 
            <li class="side-category">
                <p class="active">Efekty</p>
                <ul class="category-list">
                    <li class="category-item"><p class="active">Distortion</p></li>
                    <li class="category-item"><p>Fuzz</p></li>
                    <li class="category-item"><p>Chorus</p></li>
                    <li class="category-item"><p>Reverb</p></li>
                </ul>    
            </li> 
            <li class="side-category"><p>Kable</p></li> 
            <li class="side-category"><p>Akcesoria</p></li> 
        </ul>
    </div>
</div>
</template>

<style scoped>
.side{
    display: flex;
    flex-direction: column;
    gap: 20px;
}
.side-top p{
    font-size: 30px;
    font-weight: 700;
}

.side-top input{
    font-size: 16px;
    background-color: var(--gray-lightest);
    color: var(--gray-light);
    border: none;
    width: 140px;
    padding: 5px;
}
.side-lists{
}

.side-list{
    list-style: none;
}

.side-category{
    font-size: 20px;
    margin-bottom: 5px;
}

.category-list{
    list-style: none;
    margin-top: 10px;
    margin-left: 10%;
}

.category-item{
    font-size: 20px;
}

.active{
            font-weight: 600;
        }
</style>