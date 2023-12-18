<template>
    <img class="tik-tok-logo" src="../assets/images/tiktok-logo.png" /> 
    <div class="page" style="background-image: linear-gradient(to top, rgba(245, 246, 252, 0.52), #B4B5DB), url('/images/tiktok_pattern.png'); text-align: center;">
        <div class="row">
               <div style="padding-top:2%; font-family: futura-maxi-cg-bold;font-size: 20px;line-height: 24px; font-weight: 400;"> Your Top 5 Trendy Sounds</div>
          </div>
   
    <!-- First pair -->
    <div class="trendy-rec-1" style="display: flex; position: relative;">
        <div class="horizontal-move-left" style="margin-top: 2%;">
        <img src="../assets/images/fourth.svg">
        <img src="../assets/images/first.svg">
        <img src="../assets/images/second.svg">
        <img src="../assets/images/third.svg">
        <img src="../assets/images/fourth.svg">
        <img src="../assets/images/first.svg">
        <img src="../assets/images/second.svg">
        <img src="../assets/images/third.svg">
        <img src="../assets/images/fourth.svg">
        <img src="../assets/images/first.svg">
        </div>
        <div style="margin-top:-5%;">
            <p class="trendy-sound-text" style="font-size: 20px;">#1</p>
        </div>
        <div style="margin-top:2%; margin-left: 15%; position: absolute; top: 50%; transform: translateY(-50%);">
            <p class="trendy-sound-text" style="font-size: 16px;">{{ sounds[0] }}</p>
        </div>

          <img class="photo-sound" v-bind:src="photos[0] === '' ? 'src/assets/images/user_default.png' : photos[0]" style="position: absolute; right: 0; top: 50%; transform: translateY(-50%);" />
    </div>
    
    <div class="trendy-rec-2" style="display: flex; position: relative;">
        <div style="margin-top:-5%; margin-left: 30%;">
            <p class="trendy-sound-text" style="font-size: 20px;">#2</p>
        </div>
        <div class="horizontal-move-right" style="margin-top:2%;">
            <img src="../assets/images/second.svg">
            <img src="../assets/images/third.svg">
            <img src="../assets/images/fourth.svg">
            <img src="../assets/images/first.svg">
            <img src="../assets/images/second.svg">
            <img src="../assets/images/third.svg">
            <img src="../assets/images/fourth.svg">
            <img src="../assets/images/first.svg">
            <img src="../assets/images/second.svg">
            <img src="../assets/images/third.svg">
        </div>
        <div style="margin-top:2%;margin-left: 30%; position: absolute; top: 50%; transform: translateY(-50%);">
            <p class="trendy-sound-text" style="font-size: 16px;">{{ sounds[1] }}</p>
        </div>
        <img class="photo-sound" v-bind:src="photos[1] === '' ? 'src/assets/images/user_default.png' : photos[1]" style="position: absolute; left: 0; top: 50%; transform: translateY(-50%);" />
    </div>



    <!-- Second pair -->
    <div class="trendy-rec-1" style="display: flex; position: relative;">
        <div class="horizontal-move-left" style="margin-top: 2%;">
        <img src="../assets/images/fourth.svg">
        <img src="../assets/images/first.svg">
        <img src="../assets/images/second.svg">
        <img src="../assets/images/third.svg">
        <img src="../assets/images/fourth.svg">
        <img src="../assets/images/first.svg">
        <img src="../assets/images/second.svg">
        <img src="../assets/images/third.svg">
        <img src="../assets/images/fourth.svg">
        <img src="../assets/images/first.svg">
        </div>
        <div style="margin-top:-5%;">
            <p class="trendy-sound-text" style="font-size: 20px;">#3</p>
        </div>
        <div style="margin-top:2%;margin-left: 45%; position: absolute; top: 50%; transform: translateY(-50%);">
            <p class="trendy-sound-text" style="font-size: 16px;">{{ sounds[2] }}</p>
        </div>

          <img class="photo-sound" v-bind:src="photos[2] === '' ? 'src/assets/images/user_default.png' : photos[2]" style="position: absolute; right: 0; top: 50%; transform: translateY(-50%);" />
    </div>

    <div class="trendy-rec-2" style="display: flex; position: relative;">
        <div style="margin-top:-5%; margin-left: 30%;">
            <p class="trendy-sound-text" style="font-size: 20px;">#4</p>
        </div>
        <div class="horizontal-move-right" style="margin-top:2%;">
            <img src="../assets/images/second.svg">
            <img src="../assets/images/third.svg">
            <img src="../assets/images/fourth.svg">
            <img src="../assets/images/first.svg">
            <img src="../assets/images/second.svg">
            <img src="../assets/images/third.svg">
            <img src="../assets/images/fourth.svg">
            <img src="../assets/images/first.svg">
            <img src="../assets/images/second.svg">
            <img src="../assets/images/third.svg">
        </div>
        <div style="margin-top:2%; margin-left: 30%; position: absolute; top: 50%; transform: translateY(-50%);">
            <p class="trendy-sound-text" style="font-size: 16px;">{{ sounds[3] }}</p>
        </div>
        <img class="photo-sound" v-bind:src="photos[3] === '' ? 'src/assets/images/user_default.png' : photos[3]" style="position: absolute; left: 0; top: 50%; transform: translateY(-50%);" />
    </div>

    <!-- Third pair -->
    <div class="trendy-rec-1" style="display: flex; position: relative;">
        <div class="horizontal-move-left" style="margin-top: 2%;">
        <img src="../assets/images/fourth.svg">
        <img src="../assets/images/first.svg">
        <img src="../assets/images/second.svg">
        <img src="../assets/images/third.svg">
        <img src="../assets/images/fourth.svg">
        <img src="../assets/images/first.svg">
        <img src="../assets/images/second.svg">
        <img src="../assets/images/third.svg">
        <img src="../assets/images/fourth.svg">
        <img src="../assets/images/first.svg">
        </div>
        <div style="margin-top:-5%;">
            <p class="trendy-sound-text" style="font-size: 20px;">#5</p>
        </div>
        <div style="margin-top:2%; position: absolute; top: 50%; transform: translateY(-50%);">
            <p class="trendy-sound-text" style="font-size: 16px;">{{ sounds[4] }}</p>
        </div>

          <img class="photo-sound" v-bind:src="photos[4] === '' ? 'src/assets/images/user_default.png' : photos[4]" style="position: absolute; right: 0; top: 50%; transform: translateY(-50%);" />
    </div>

    <div style="color: black; font-family: 'futura-maxi-cg-bold'; padding-top: 5%;">
        You listened to <span style="color: #fe2c55;">{{ seenTrends }}</span> of the <span style="color: #fe2c55;">{{totalTrends}}</span> trending sounds.
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