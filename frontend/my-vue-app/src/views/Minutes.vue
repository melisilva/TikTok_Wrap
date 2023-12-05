<template>
  <div class="page"
    style="background-image: linear-gradient(to bottom, rgba(245, 246, 252, 0.52), rgba(117, 19, 93, 0.73)), url('/images/tiktok_pattern.png');">
      <img class="tik-tok-logo" src="../assets/images/tiktok-logo.png" />
      <div style="display: flex; flex-direction: column; justify-content: center; align-items: middle;">
      <div class="row">
        <div class="general-text" style="padding-top: 15%;">
        You watched...
      </div>
      </div>

      <div class="row">
        <div class="general-text" style="margin-top:5%;">
        ...{{ totalMinutes }} minutes
      </div>
      </div>

      <div class="row" style="display: flex; flex-direction: row; justify-content: center;">
      <div class="quote-text">
        {{ quote }}
      </div>
      </div>
    </div>
  </div>
  </template>
  
  <script>
  import axios from 'axios'
  import { defineComponent } from 'vue'
  
  export default defineComponent({
    name: 'Minutes',
    data() {
      return {
          quote: "",
          totalMinutes: 0
      }
    },
    methods: {
    },
    async beforeMount() {
      await axios.get("http://localhost:8000/total-minutes")
          .then((response) => {
              console.log(response.data)
              this.totalMinutes = response.data['Minutes'];
              this.quote = response.data['Quote'];
          })
          .catch((error) => {
              console.log(error)
          })
    }
  })
  </script>