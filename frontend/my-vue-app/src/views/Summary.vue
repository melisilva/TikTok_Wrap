<template>
  
    <div class="page" style="width:100%;color:white; padding:auto;background-image: linear-gradient(180deg, rgba(255, 255, 255, 0.00) 0%,rgba(255, 255, 255, 1.00) 44.79166567325592%); ">

        <div class="scroll-parent" style="position:fixed; z-index: -1;">
            <div class="scroll-element primary">
                <img src="../assets/images/tiktok_pattern.png"/>
            </div>
            <div class="scroll-element secondary">
                <img src="../assets/images/tiktok_pattern.png" />
            </div>
        </div>

        <img class="tik-tok-logo" src="../assets/images/tiktok-logo.png" />

        
        <router-link to="/top-creator-overall">
            <img class="arrow-left" src="../assets/images/arrow-left-solid.svg" alt="Next Page" />
        </router-link>
        <div class="row" style="height:45%; padding-top: 30px; padding-bottom: 30px;">
            <!-- Create a white border -->
            <div style="border: 5px solid black; border-radius: 50%; width: 300px; height: 300px; margin: auto;">
                <!-- Center the image -->
                <div style="width: 100%; height: 100%; position: relative;">
                    <img v-bind:src="photo === '' ? 'src/assets/images/sound_default.png' : photo" style="background-color:cyan;width: 300px; height: 300px; border-radius: 50%;">
                </div>
                <div style="width: 60%; height: 10%; border: 5px solid black; border-radius: 50px; position: relative; margin: auto; bottom: 7%; ">
                    <div style=" font-family: 'futura-maxi-cg-bold'; width: 100%; height: 100%; background-color: black; border-radius: 50px; display:flex; align-items: center; justify-content: center;">
                        {{ username }}
                    </div>
                </div>
            </div>
        </div>

        <div class="row" style="height: 45%; font-size: large">
            <div class="row" style="height: 65%; display: flex;">
                <div class="col" style="width: 50%;">
                    <div style=" font-family: 'futura-maxi-cg-bold'; color: black; font-weight: bolder;height:10%; margin-bottom: 5%">
                        Top Creators
                    </div>
                    <div v-for="creator in topCreators" style="font-family: 'futura-maxi-cg-bold';height:10%; color:black; font-size:65%; display: flex; justify-content: space-between; flex-direction: column;">
                        <div >
                            {{ creator }}
                        </div>
                    </div>
                </div>
                <div class="col" style="width: 50%;">
                    <div style=" font-family: 'futura-maxi-cg-bold'; color: black; font-weight: bolder;height:10%; margin-bottom: 5%">
                        Top Hashtags
                    </div>
                    <div v-for="hashtag in topHashTags" style=" font-family: 'futura-maxi-cg-bold'; color:black; height:10%; font-size:65%; display: flex; justify-content: space-between; flex-direction: column;">
                        <div >
                            # {{ hashtag }}
                        </div>
                    </div>
                </div>
            </div>
            <div class="row" style="height: 35%;">
                <div style=" font-family: 'futura-maxi-cg-bold';font-weight: bolder; color:black;">
                    Minutes Watched
                </div>
                <div style=" font-family: 'futura-maxi-cg-bold'; color:black;">
                    {{ minutesWatched }}
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped lang="scss">
.scroll-parent {
  position: relative;
  width: 125vw;
  height: 125vw;
  overflow-x: hidden;
  overflow-y: hidden;
}

.scroll-element {
  width: inherit;
  height: inherit;
  position: absolute;
  left: 0%;
  top: 0%;
}
.primary {
  animation: primary 5s linear infinite;
}

.secondary {
  animation: secondary 5s linear infinite;
}

@keyframes primary {
  from {
    left: 100%;
    top: 0%;
  }
  to {
    left: 0%;
    top: 100%;
  }
}

@keyframes secondary {
  from {
    left: 0%;
    top: -100%;

  }
  to {
    left: -100%;
    top: 0%;
  }
}
</style>

<script>

    import axios from 'axios';
    import { defineComponent } from 'vue';

    export default defineComponent({
        name: 'TopCreator',
        data() {
            return {
                username: "",
                topCreators: [],
                topHashTags: [],
                minutesWatched: 0,
                photo: ""
            }
        },
        async created() {
            axios.get("http://localhost:8000/summary")
                .then((response) => {
                    this.username = response.data["Username"]
                    this.topCreators = response.data["Top Creators"]["Username"]
                    this.topHashTags = response.data["Top Hashtags"]["Hashtag"]
                    this.minutesWatched = response.data["Total Minutes"]
                    this.photo = response.data["Photo"]
                    console.log(this.username)
                    console.log(this.topCreators)
                    console.log(this.topHashTags)
                    console.log(this.minutesWatched)
                    console.log(this.photo)
                    console.log(response.data)
                })
                .catch((error) => {
                    console.log(error)
                })
        },
        methods: {
        }
        
    })

</script>