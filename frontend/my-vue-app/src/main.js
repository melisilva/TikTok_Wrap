import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

import router from './router/index.js'
/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import './assets/sass/style.scss'

const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(router)
app.mount("#app")

/*
 .trendy-sound-text-places-div {
      margin-top: -5%;
    }

    .trendy-sound-text-places-div-2 {
      margin-top: -5%;
      margin-left: 30%;
    }

    .trendy-sound-text-sounds-div {
      margin-top:2%; 
      position: absolute; 
      top: 50%; 
      transform: translateY(-50%);
    }

    .trendy-sound-text-sounds-div-2 {
      margin-top:2%; 
      position: absolute; 
      top: 50%; 
      transform: translateY(-50%);
      margin-left: 30%;
    }

    .first-sound {
      margin-left: 15%;
    }
    .third-sound {
      margin-left: 45%;
    }


    @keyframes moveHorizontalLeft {
      0% {
        transform: translateX(-100%);
      }
      50% {
        transform: translateX(0);
      }
      100% {
        transform: translateX(-100%);
      }
    }
    @keyframes moveHorizontalRight {
      0% {
        transform: translateX(100%);
      }
      50% {
        transform: translateX(0%);
      }
      100% {
        transform: translateX(100%);
      }
    }
    .horizontal-move-left {
      animation: moveHorizontalLeft 5s linear infinite;
    }
    .horizontal-move-right {
      animation: moveHorizontalRight 5s linear infinite;
    }

    .moves {
      margin-top:2%;
    }
     */