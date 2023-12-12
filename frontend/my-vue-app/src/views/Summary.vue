<template>
    <div class="page" style="width:100%;color:white; background-image: linear-gradient(to bottom, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 1) 50%, rgba(0, 0, 0, 1)), url('/images/black_tiktok_pattern.png'); padding:auto;">
        <img class="tik-tok-logo" src="../assets/images/tiktok-logo.png" /> 

        <div class="row" style="height:45%; padding-top: 30px; padding-bottom: 30px;">
            <!-- Create a white border -->
            <div style="border: 5px solid white; border-radius: 50%; width: 300px; height: 300px; margin: auto;">
                <!-- Center the image -->
                <div style="width: 100%; height: 100%; position: relative;">
                    <img :src="Photo" style="background-color:cyan;width: 300px; height: 300px; border-radius: 50%;">
                </div>
                <div style="width: 50%; height: 10%; border: 5px solid white; border-radius: 50px; position: relative; margin: auto; bottom: 7%; ">
                    <div style="width: 100%; height: 100%; background-color: black; border-radius: 50px; display:flex; align-items: center; justify-content: center;">
                        {{ username }}
                    </div>
                </div>
            </div>
        </div>

        <div class="row" style="height: 45%; font-size: large">
            <div class="row" style="height: 65%; display: flex;">
                <div class="col" style="width: 50%;">
                    <div style="font-weight: bolder;height:10%; margin-bottom: 5%">
                        Top Creators
                    </div>
                    <div v-for="creator in topCreators" style="height:10%;display: flex; justify-content: space-between; flex-direction: column;">
                        <div >
                            {{ creator }}
                        </div>
                    </div>
                </div>
                <div class="col" style="width: 50%;">
                    <div style="font-weight: bolder;height:10%; margin-bottom: 5%">
                        Top Hashtags
                    </div>
                    <div v-for="hashtag in topHashTags" style="height:10%;display: flex; justify-content: space-between; flex-direction: column;">
                        <div >
                            # {{ hashtag }}
                        </div>
                    </div>
                </div>
            </div>
            <div class="row" style="height: 35%;">
                <div style="font-weight: bolder;">
                    Minutes Watched
                </div>
                <div>
                    {{ minutesWatched }}
                </div>
            </div>
        </div>
    </div>
</template>


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
                })
                .catch((error) => {
                    console.log(error)
                })
        },
        methods: {
        }
        
    })

</script>