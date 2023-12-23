<template>
    <button @click="captureAndSave" class="tik-tok-button">Save Image</button>

    <div id="your-component-id" class="page"
        style="width:100%;color:white; padding:auto;background-image: linear-gradient(180deg, rgba(255, 255, 255, 0.00) 0%,rgba(255, 255, 255, 1.00) 44.79166567325592%, rgba(255, 255, 255, 1.00) 100%); ">

        <div class="scroll-parent" style="position:fixed; z-index: -1;">
            <div class="scroll-element four" style="position:fixed;">
                <img src="../assets/images/tiktok_pattern.png" />
            </div>
            <div class="scroll-element three" style="position:fixed;">
                <img src="../assets/images/tiktok_pattern.png" />
            </div>
            <div class="scroll-element two" style="position:fixed;">
                <img src="../assets/images/tiktok_pattern.png" />
            </div>
            <div class="scroll-element one" style="position:fixed;">
                <img src="../assets/images/tiktok_pattern.png" />
            </div>
        </div>

        <img class="tik-tok-logo" src="../assets/images/tiktok-logo.png" />


        <router-link to="/finale">
            <img class="arrow-left" src="../assets/images/arrow-left-solid.svg" alt="Next Page" />
        </router-link>
        <div class="row" style="height:45%; padding-top: 30px; padding-bottom: 30px;">

            <!-- Create a white border -->
            <div style="border: 5px solid black; border-radius: 50%; width: 300px; height: 300px; margin: auto;">
                <!-- Center the image -->
                <div style="width: 100%; height: 100%; position: relative;">
                    <img v-bind:src="photo === '' ? 'src/assets/images/user_default.png' : photo" style="background-color:cyan;width: 300px; height: 300px; border-radius: 50%;">
                </div>
                <div
                    style="width: 60%; height: 10%; border: 5px solid black; border-radius: 50px; position: relative; margin: auto; bottom: 7%; ">
                    <div
                        style=" font-family: 'futura-maxi-cg-bold'; width: 100%; height: 100%; background-color: black; border-radius: 50px; display:flex; align-items: center; justify-content: center;">
                        {{ username }}
                    </div>
                </div>
            </div>
        </div>

        <div class="row" style="height: 45%; font-size: large">
            <div class="row" style="height: 65%; display: flex;">
                <div class="col" style="width: 50%;">
                    <div
                        style=" font-family: 'futura-maxi-cg-bold'; color: black; font-weight: bolder;height:10%; margin-bottom: 5%">
                        Top Creators
                    </div>
                    <div v-for="creator in topCreators"
                        style="font-family: 'futura-maxi-cg-bold';height:10%; color:black; font-size:65%; display: flex; justify-content: space-between; flex-direction: column;">
                        <div>
                            {{ creator }}
                        </div>
                    </div>
                </div>
                <div class="col" style="width: 50%;">
                    <div
                        style=" font-family: 'futura-maxi-cg-bold'; color: black; font-weight: bolder;height:10%; margin-bottom: 5%">
                        Top Hashtags
                    </div>
                    <div v-for="hashtag in topHashTags"
                        style=" font-family: 'futura-maxi-cg-bold'; color:black; height:10%; font-size:65%; display: flex; justify-content: space-between; flex-direction: column;">
                        <div>
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
        <div style="height:10%; background-color: white;">

        </div>

    </div>
</template>

<style scoped lang="scss">
.scroll-parent {
    position: relative;
    width: 100%;
    height: 100%;
}

.scroll-element {
    width: inherit;
    height: inherit;
    position: absolute;
    left: 0%;
    top: 0%;
}

.one {
    animation: one 30s linear infinite;
}

.two {
    animation: two 30s linear infinite;
}

.three {
    animation: three 30s linear infinite;
}

.four {
    animation: four 30s linear infinite;
}

@keyframes one {
    from {
        left: 0px;
        top: 0px;
    }

    to {
        left: -1920px;
        top: 1080px;
    }
}

@keyframes two {
    from {
        left: 1817px;
        top: -10px;
    }

    to {
        left: -103px;
        top: 1070px;
    }
}

@keyframes three {
    from {
        left: -286px;
        top: -1069px;

    }

    to {
        left: -2206px;
        top: 11px;
    }
}

@keyframes four {
    from {
        left: 1531px;
        top: -1079px;

    }

    to {
        left: -389px;
        top: -1px;
    }
}
</style>

<script>

import axios from 'axios';
import { defineComponent } from 'vue';
import domtoimage from 'dom-to-image';

export default defineComponent({
    name: 'Summary',
    data() {
        return {
            username: "",
            topCreators: [],
            topHashTags: [],
            minutesWatched: 0,
            photo: ""
        }
    },
    methods: {
        async captureAndSave() {
            // Use dom-to-image to capture the content
            const element = document.getElementById('your-component-id'); // Replace with your component's ID

            // Capture the content as an image URL
            await domtoimage.toPng(element)
                .then((dataUrl) => {
                    // Create a download link
                    const link = document.createElement('a');
                    link.href = dataUrl;
                    link.download = 'summary.png';
                    document.body.appendChild(link);
                    // Trigger the download
                    link.click();
                    // Remove the link from the DOM
                    document.body.removeChild(link);
                })
                .catch((error) => {
                    console.error('Error capturing image:', error);
                });
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
});

</script>