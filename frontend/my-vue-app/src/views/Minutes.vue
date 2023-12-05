<template>
    <div>
      <img class="tik-tok-logo" src="../assets/images/tiktok-logo.png" />
      <div class="general-text">
        You watched...
      </div>

      <div class="general-text">
        ...{{ totalMinutes }} minutes
      </div>

      <div class="quote-text">
        {{ quote }}
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