<template>
    <div class="page" style="background: linear-gradient(to bottom right, #FE2C55, #25F4EE); text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh;"> 
        <img class="tik-tok-logo" src="../assets/images/tiktok-logo.png" />  
        <router-link to="/opening">
            <img class="arrow-left" src="../assets/images/arrow-left-solid.svg" alt="Previous Page" />
        </router-link>
        <router-link to="/top-history-creators">
            <img class="arrow-right" src="../assets/images/arrow-right-solid.svg" alt="Next Page" />
        </router-link>
        
        <div class="row" style="width: 80%;">
            <div class="general-text" style="text-align: center;">
                Let's start our journey through your TikTok memory lane.
            </div>
            <div class="general-text" style="padding-top: 20%;">
                Here are the creators who left a mark on your FYP.
            </div>
        </div>
    </div>
</template>
