<template>
    <div class="page" style="background: linear-gradient(to bottom right, #FE2C55, #25F4EE); text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh;"> 
        <img class="tik-tok-logo" src="../assets/images/tiktok-logo.png" />  
        <router-link to="/top-favorite-creators">
            <img class="arrow-left" src="../assets/images/arrow-left-solid.svg" alt="Previous Page" />
        </router-link>
        <router-link to="/top-history-sounds">
            <img class="arrow-right" src="../assets/images/arrow-right-solid.svg" alt="Next Page" />
        </router-link>
        
        <div class="row" style="width: 80%;">
            <div class="general-text" style="text-align: center;">
                Let the beats and melodies resonate!
            </div>
            <div class="general-text" style="padding-top: 20%;">
                These are the sounds that accompanied your year on TikTok...
            </div>
        </div>
    </div>
</template>
