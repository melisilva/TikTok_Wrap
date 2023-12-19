<template>
    <div class="page" 
        style="color:white; background-image: linear-gradient(to bottom, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 1) 50%, rgba(0, 0, 0, 1)), url('/images/black_tiktok_pattern.png'); padding:auto; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh;"> 
        <img class="tik-tok-logo" src="../assets/images/tiktok-logo.png" /> 
        <router-link to="/trend-sounds">
            <img class="arrow-left" src="../assets/images/arrow-left-solid.svg" alt="Previous Page" />
        </router-link>
        <router-link to="/top-creator-overall">
            <img class="arrow-right" src="../assets/images/arrow-right-solid.svg" alt="Next Page" />
        </router-link>
        <div class="row" style="height:45%; padding-top: 10px; padding-bottom: 55px;">
            <!-- Create a white border -->
            <div style="border: 5px solid white; border-radius: 50%; width: 250px; height: 250px; margin: auto;">
                <!-- Center the image -->
                <div style="width: 100%; height: 100%; position: relative;">
                    <img src='../assets/images/41NzLv-KoEL.jpg' style="background-color:cyan;width: 250px; height: 250px; border-radius: 50%;">
                </div>
            </div>
        <div class="general-text" style="color: #fe2c55; padding-top: 5%;">
            Trends
        </div>
    </div>
    <div class="trends" v-for="trend in trendsList" :key="trend" style="margin-top: -2%;">
            {{ trend }}<br/>
    </div>

    <div class="row" >
        <div class="general-text" style="text-align: center; font-size: 100%;">
                You have watched...
        </div>
        <div class="general-text" style="text-align: center; font-size: 100%; padding-top: 10%; color: #fe2c55;">
                {{ seenTrends }}
        </div>
        <div class="general-text" style="padding-top: 10%;font-size: 100%;">
                ...out of <span style="color: #fe2c55;"> {{ totalTrends }}</span> trends!
        </div>
    </div>
    </div>

</template>

<script>
import axios from 'axios'
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'Trends',
  data() {
    return {
     trendsList: [],
     totalTrends: 0,
     seenTrends: 0,
    }
  },
  methods: {
  },
  async beforeMount() {
    await axios.get("http://localhost:8000/tiktok-trend")
      .then((response) => {
        console.log(response.data)
        this.trendsList = Object.values(response.data['Trends']);
        this.totalTrends = response.data['Total Trends'];
        this.seenTrends = response.data['Seen Trends'];
      })
      .catch((error) => {
        console.log(error)
      })
  }
})
</script>