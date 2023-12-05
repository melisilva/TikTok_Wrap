<template>
    <div>
      <img class="tik-tok-logo" src="../assets/images/tiktok-logo.png" />
      <div class="general-text">
        You usually do it during this time of the day...
      </div>

      <div class="general-text">
        ...{{ time }} 
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
  name: 'TimeofDay',
  data() {
    return {
        quote: "",
        time: ""
    }
  },
  methods: {
  },
  async beforeMount() {
    await axios.get("http://localhost:8000/time-of-day")
        .then((response) => {
            console.log(response.data)
            this.time = response.data['Time'];
            this.quote = response.data['Quote'];
        })
        .catch((error) => {
            console.log(error)
        })
  }
})
</script>