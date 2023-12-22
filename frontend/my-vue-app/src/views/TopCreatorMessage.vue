<template>
    <div class="page" style="background: linear-gradient(to bottom right, #FE2C55, #25F4EE); text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh;"> 
        <img class="tik-tok-logo" src="../assets/images/tiktok-logo.png" />  
        <router-link to="/trends">
            <img class="arrow-left" src="../assets/images/arrow-left-solid.svg" alt="Previous Page" />
        </router-link>
        <router-link to="/top-creator-overall">
            <img class="arrow-right" src="../assets/images/arrow-right-solid.svg" alt="Next Page" />
        </router-link>
        
        <div class="row" style="width: 80%;">
            <div class="general-text" style="text-align: center;">
                Crowning the ultimate TikTok royalty!
            </div>
            <div class="general-text" style="padding-top: 20%;">
                Your top creator, ruling across all realms...
            </div>
        </div>
    </div>
</template>
