<template>
    <div class="page" style="background: linear-gradient(180deg, rgba(255, 0, 50, 0.83) 0%, rgba(225, 27, 78, 0.84) 8.506933599710464%, rgba(33, 186, 235, 0.86) 53.5416305065155%, rgba(37, 244, 238, 0.86) 88.71526718139648%); text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh;"> 
        <img class="tik-tok-logo" src="../assets/images/tiktok-logo.png" />  
        <router-link to="/top-favorite-sounds">
            <img class="arrow-left" src="../assets/images/arrow-left-solid.svg" alt="Previous Page" />
        </router-link>
        <router-link to="/top-hashtags">
            <img class="arrow-right" src="../assets/images/arrow-right-solid.svg" alt="Next Page" />
        </router-link>
        
        <div class="row" style="width: 80%;">
            <div class="general-text" style="color: black; text-align: center;">
                Unlock the power of hashtags!
            </div>
            <div class="general-text" style="color: black; padding-top: 20%;">
                Here are the tags that lit up your TikTok experience...
            </div>
        </div>
    </div>
</template>
