<template>
    <div class="page" style="background: #f08080;">
    <img class="tik-tok-logo" src="../assets/images/tiktok-logo.png" />
    <div class="title">
        {{ percentage }}% of TikToks you watched were ads
    </div>
    <div class="subtitle">
        Top Ad Creators
    </div>

    <div style="padding-left: 10%;">

    <div class="creator-item">
        <div class="number"> #1 </div>
        <img v-bind:src="photos[0] === '' ? 'src/assets/images/user_default.png' : photos[0]" class="pfp"/>
        <div class="name"> {{ creators[0]}} </div>
    </div>

    <div class="creator-item">
        <div class="number"> #2 </div>
        <img v-bind:src="photos[1] === '' ? 'src/assets/images/user_default.png' : photos[1]" class="pfp"/>
        <div class="name"> {{ creators[1]}} </div>
    </div>

    <div class="creator-item">
        <div class="number"> #3 </div>
        <img v-bind:src="photos[2] === '' ? 'src/assets/images/user_default.png' : photos[2]" class="pfp"/>
        <div class="name"> {{ creators[2]}} </div>
    </div>

    <div class="creator-item">
        <div class="number"> #4 </div>
        <img v-bind:src="photos[3] === '' ? 'src/assets/images/user_default.png' : photos[3]" class="pfp"/>
        <div class="name"> {{ creators[3]}} </div>
    </div>

    <div class="creator-item">
        <div class="number"> #5 </div>
        <img v-bind:src="photos[4] === '' ? 'src/assets/images/user_default.png' : photos[4]" class="pfp"/>
        <div class="name"> {{ creators[4]}} </div>
    </div>
    </div>
    </div>
</template>

<script>
import axios from 'axios'
import { defineComponent } from 'vue'
//add margins all around (reflexive)

export default defineComponent({
  name: 'TopAdCreators',
  data() {
    return {
        creators: [],
        percentage: 0,
        photos: []
    }
  },
  methods: {
  },
  async beforeMount() {
    await axios.get("http://localhost:8000/ads")
        .then((response) => {
            console.log(response.data)
            this.creators = Object.values(response.data['Username']);
            this.percentage = Math.round(Object.values(response.data['Percentage'])[0]);
            this.photos = Object.values(response.data['Photo']);
        })
        .catch((error) => {
            console.log(error)
        })
  }
})
</script>