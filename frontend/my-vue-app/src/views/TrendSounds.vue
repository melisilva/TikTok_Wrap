<template>
    <img class="tik-tok-logo" src="../assets/images/tiktok-logo.png" /> 
    <div class="page" style="background-image: linear-gradient(to top, rgba(245, 246, 252, 0.52), #B4B5DB), url('/images/tiktok_pattern.png'); text-align: center;">
        <div class="row">
               <div style="padding-top:2%; font-family: futura-maxi-cg-bold;font-size: 20px;line-height: 24px; font-weight: 400;"> Your Top 5 Trendy Sounds</div>
          </div>
    <br style="margin-bottom: 1%; "/>
    <!-- First pair -->
    <div class="trendy-rec-1">
        <div style="display: flex; align-items: center;">
          <div style="margin-left: 15%;">
              <p class="trendy-sound-text">#1</p>
              <p class="trendy-sound-text" >{{ sounds[0] }}</p>
          </div>
          <img class="photo-sound" v-bind:src="photos[0] === '' ? 'src/assets/images/user_default.png' : photos[0]" style="position: absolute; right: 0; top: 50%; transform: translateY(-50%);" />
        </div>    
    </div>
    <div class="trendy-rec-2">
        <div style="display: flex;">

          <img class="photo-sound" v-bind:src="photos[1] === '' ? 'src/assets/images/user_default.png' : photos[1]" style="position: absolute; top: 50%; transform: translateY(-50%);" />
        </div>
    </div>

    <!-- Second pair -->
    <div class="trendy-rec-1">
        <div style="display: flex; align-items: center;">

          <img class="photo-sound" v-bind:src="photos[2] === '' ? 'src/assets/images/user_default.png' : photos[2]" style="position: absolute; right: 0; top: 50%; transform: translateY(-50%);" />
        </div>    
    </div>
    <div class="trendy-rec-2">
        <div style="display: flex; align-items: center;">

          <img class="photo-sound" v-bind:src="photos[3] === '' ? 'src/assets/images/user_default.png' : photos[3]" style="position: absolute; top: 50%; transform: translateY(-50%);" />
        </div>
    </div>

    <!-- Third pair -->
    <div class="trendy-rec-1">
        <div style="display: flex; align-items: center;">

          <img class="photo-sound" v-bind:src="photos[4] === '' ? 'src/assets/images/user_default.png' : photos[4]" style="position: absolute; right: 0; top: 50%; transform: translateY(-50%);" />
        </div>    
    </div>
   </div>
  </template>

<script>
import axios from 'axios'
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'TrendSounds',
  data() {
    return {
     sounds: [],
     photos: [],
     totalTrends: 0,
     seenTrends: 0,
    }
  },
  methods: {
  },
  async beforeMount() {
    await axios.get("http://localhost:8000/sound-trend")
      .then((response) => {
        console.log(response.data)
        this.sounds = Object.values(response.data['Trends']['Sound Name']);
        this.photos = Object.values(response.data['Trends']['Photo']);
        this.totalTrends = response.data['Total Trends'];
        this.seenTrends = response.data['Seen Trends'];
      })
      .catch((error) => {
        console.log(error)
      })
  }
})
</script>