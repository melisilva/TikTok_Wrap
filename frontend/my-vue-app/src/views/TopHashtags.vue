<template>
     <img class="tik-tok-logo" src="../assets/images/tiktok-logo.png" style="z-index: 10"/>
     <router-link to="/top-favorite-sounds">
		<img class="arrow-left" src="../assets/images/arrow-left-solid.svg" alt="Previous Page" />
	</router-link>
	<router-link to="/ads-message">
		<img class="arrow-right" src="../assets/images/arrow-right-solid.svg" alt="Next Page" />
	</router-link>
     <div class="page" style="background: #3B719F; display: flex; flex-direction: column;">
         <div class="top-history-creators" style="width: 100%; height: 10%;">
             Your Top 5 Watched Hastags
         </div>
         <br class="space-for-title"/>

         <div style="height: 80%">
             <div class="side-by-side-chart" style="display: flex; flex-direction: row; width: 100%; height: 100%">
                 <div class="col ranking ">
                     <div class="place ranking">
                         <img class="ellipse ranking"
                             v-bind:src="photos[4] === '' ? 'src/assets/images/hashtag_default.png' : photos[4]" />
                         <div class="rectangle-place"
                             style=" width: auto; top: -22.5px; z-index: 1; padding: 2px 5px 2px 5px;">
                             <p class="number-placement">#5</p>
                         </div>
                     </div>
                     <div class="rectangle centered-container" id="rect-15">
                         <p class="text-inside-rectangle" > {{ hashtags[4] }} </p>
                     </div>
 
                 </div>
                 <div class="col ranking">
                     <div class="place ranking">
                         <img class="ellipse ranking"
                             v-bind:src="photos[1] === '' ? 'src/assets/images/hashtag_default.png' : photos[1]" />
                         <div class="rectangle-place"
                             style=" width: auto; top: -22.5px; z-index: 1; padding: 2px 5px 2px 5px;">
                             <p class="number-placement">#2</p>
                         </div>
                     </div>
                     <div class="rectangle centered-container" id="rect-12">
                         <p class="text-inside-rectangle" > {{ hashtags[1] }} </p>
                     </div>
                 </div>
                 <div class="col ranking">
                     <div class="place ranking">
                         <img class="ellipse ranking"
                             v-bind:src="photos[0] === '' ? 'src/assets/images/hashtag_default.png' : photos[0]" />
                         <div class="rectangle-place"
                             style=" width: auto; top: -22.5px; z-index: 1; padding: 2px 5px 2px 5px;">
                             <p class="number-placement">#1</p>
                         </div>
                     </div>
                     <div class="rectangle centered-container" id="rect-11">
                         <p class="text-inside-rectangle" > {{ hashtags[0] }} </p>
                     </div>
                 </div>
                 <div class="col ranking">
                     <div class="place ranking">
                         <img class="ellipse ranking"
                             v-bind:src="photos[2] === '' ? 'src/assets/images/hashtag_default.png' : photos[2]" />
                         <div class="rectangle-place"
                             style=" width: auto; top: -22.5px; z-index: 1; padding: 2px 5px 2px 5px;">
                             <p class="number-placement">#3</p>
                         </div>
                     </div>
                     <div class="rectangle centered-container" id="rect-13">
                         <p class="text-inside-rectangle">
                             {{ hashtags[2] }} </p>
                     </div>
                 </div>
                 <div class="col ranking">
                     <div class="place ranking">
                         <img class="ellipse ranking"
                             v-bind:src="photos[3] === '' ? 'src/assets/images/hashtag_default.png' : photos[3]" />
                         <div class="rectangle-place"
                             style=" width: auto; top: -22.5px; z-index: 1; padding: 2px 5px 2px 5px;">
                             <p class="number-placement">#4</p>
                         </div>
                     </div>
                     <div class="rectangle centered-container" id="rect-14">
                         <p class="text-inside-rectangle" > {{ hashtags[3] }} </p>
                     </div>
                 </div>
 
 
             </div>
         </div>
     </div>
 </template>
 
 
 <style>
 .rectangle {
     width: 100%;
     overflow: hidden;
     top: 30px;
     border-radius: 30px 30px 0px 0px;
 }
 
 #rect-11 {
     background: #25f4ee;
     position: relative;
     height: 528px;
     animation: growup-11 5s;
 }
 
 #rect-12 {
     background: #fe2c55;
     position: relative;
     height: 450px;
     animation: growup-12 5s;
 }
 
 #rect-13 {
     background: #f7ec59;
     position: relative;
     height: 379px;
     animation: growup-13 5s;
 }
 
 #rect-14 {
     background: #b14aed;
     position: relative;
     height: 316px;
     animation: growup-14 5s;
 }
 
 #rect-15 {
     background: #454ade;
     position: relative;
     height: 272px;
     animation: growup-15 5s;
 }
 
 @keyframes growup-11 {
     0% {
         height: 0px;
     }
 
     100% {
         height: 528px;
     }
 }
 
 @keyframes growup-12 {
     0% {
         height: 0px;
     }
 
     100% {
         height: 450px;
     }
 }
 
 @keyframes growup-13 {
     0% {
         height: 0px;
     }
 
     100% {
         height: 379px;
     }
 }
 
 @keyframes growup-14 {
     0% {
         height: 0px;
     }
 
     100% {
         height: 316px;
     }
 }
 
 
 @keyframes growup-15 {
     0% {
         height: 0px;
     }
 
     100% {
         height: 272px;
     }
 }
 </style>

<script>
import axios from 'axios'
import { defineComponent } from 'vue'

export default defineComponent({
 name: 'TopHashtags',
 data() {
   return {
    hashtags: [],
    photos: []
   }
 },
 methods: {
 },
 async beforeMount() {
   await axios.get("http://localhost:8000/top-hashtag")
     .then((response) => {
       console.log(response.data)
       this.hashtags = Object.values(response.data['Hashtag']);
       this.photos = Object.values(response.data['Photo']);
     })
     .catch((error) => {
       console.log(error)
     })
 }
})
</script>