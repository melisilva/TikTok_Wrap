<template>
    <div class="page" 
    style="background:linear-gradient(to bottom right, #FE2C55, #25F4EE);text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh;"> 
        <img class="tik-tok-logo" src="../assets/images/tiktok-logo.png" />  
        <router-link to="/creators-message">
            <img class="arrow-right" src="../assets/images/arrow-right-solid.svg" alt="Next Page" />
        </router-link>
        <div class="row">
            <div class="general-text" style="text-align: center;width: 100%;">
                Hello, {{ name }}!
            </div>
            <div class="general-text" style="padding-left:10%; padding-top: 20%;width: 80%;">
               Ready to see a recap of your year on TikTok?
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { defineComponent } from 'vue'

export default 
defineComponent({
  name: 'Opening',
  data() {
    return {
     name: ""
    }
  },
  methods: {
  },
  async beforeMount() {
    await axios.get("http://localhost:8000/user-name")
      .then((response) => {
        console.log(response.data)
        this.name = response.data['Username']
      })
      .catch((error) => {
        console.log(error)
      })
  }
})
</script>