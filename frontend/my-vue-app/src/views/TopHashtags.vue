<template>
    <div class="page" style="background: #B7C9E2;">
         <div class="top-history-creators"> Your Top 5 Hashtags </div>
         <img class="tik-tok-logo" src="../assets/images/tiktok-logo.png" />
         <div class="side-by-side-chart" style="flex-direction: row;">
              <div class="col">
                   <div class="place" style="left:-5px;">
                        <img class="ellipse" v-bind:src="photos[4] === '' ? 'src/assets/images/hashtag_default.png' : photos[4]" />
                        <div class="rectangle-place" style=" width: auto; left: 25px; top: -90px; z-index: 1; padding: 2px 5px 2px 5px;">
                             <p style="padding: 0px; margin: 0px; font-family: 'futura-maxi-cg-bold'; color: white; ">#5</p>
                        </div>
                   </div>
                   <div class="rectangle" id="rect-15">
                        <p class="text-inside-rectangle"> {{ hashtags[4]}} </p>
                   </div>
              </div>
              <div class="col">
                   <div class="place" style="left:-5px;">
                        <img class="ellipse" v-bind:src="photos[1] === '' ? 'src/assets/images/hashtag_default.png' : photos[1]" />
                        <div class="rectangle-place" style=" width: auto; left: 25px; top: -90px; z-index: 1; padding: 2px 5px 2px 5px;">
                             <p style="padding: 0px; margin: 0px; font-family: 'futura-maxi-cg-bold'; color: white; ">#2</p>
                        </div>
                   </div>
                   <div class="rectangle" id="rect-12">
                        <p class="text-inside-rectangle"> {{ hashtags[1]}} </p>
                   </div>
              </div>
              <div class="col">
                   <div class="place">
                        <img class="ellipse" v-bind:src="photos[0] === '' ? 'src/assets/images/hashtag_default.png' : photos[0]" />
                        <div class="rectangle-place" style=" width: auto; left: 25px; top: -90px; z-index: 1; padding: 2px 5px 2px 5px;">
                             <p style="padding: 0px; margin: 0px; font-family: 'futura-maxi-cg-bold'; color: white; ">#1</p>
                        </div>
                   </div>
                   <div class="rectangle" id="rect-11">
                        <p class="text-inside-rectangle"> {{ hashtags[0]}} </p>
                   </div>
              </div>
              <div class="col">
                   <div class="place" style="left:5px;">
                        <img class="ellipse" v-bind:src="photos[2] === '' ? 'src/assets/images/hashtag_default.png' : photos[2]" />
                        <div class="rectangle-place" style=" width: auto; left: 25px; top: -90px; z-index: 1; padding: 2px 5px 2px 5px;">
                             <p style="padding: 0px; margin: 0px; font-family: 'futura-maxi-cg-bold'; color: white; ">#3</p>
                        </div>
                   </div>
                   <div class="rectangle" id="rect-13">
                        <p class="text-inside-rectangle"> {{ hashtags[2]}} </p>
                   </div>
              </div>
              <div class="col">
                   <div class="place" style="left:5px;">
                        <img class="ellipse" v-bind:src="photos[3] === '' ? 'src/assets/images/hashtag_default.png' : photos[3]" />
                        <div class="rectangle-place" style=" width: auto; left: 25px; top: -90px; z-index: 1; padding: 2px 5px 2px 5px;">
                             <p style="padding: 0px; margin: 0px; font-family: 'futura-maxi-cg-bold'; color: white; ">#4</p>
                        </div>
                   </div>
                   <div class="rectangle" id="rect-14">
                        <p class="text-inside-rectangle"> {{ hashtags[3]}} </p>
                   </div>
              </div>


         </div>

    </div>
</template>

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