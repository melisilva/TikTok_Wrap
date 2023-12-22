<template>
    <img class="tik-tok-logo" src="../assets/images/tiktok-logo.png" />
	<router-link to="/top-liked-creators">
		<img class="arrow-left" src="../assets/images/arrow-left-solid.svg" alt="Previous Page" />
	</router-link>
	<router-link to="/sounds-message">
		<img class="arrow-right" src="../assets/images/arrow-right-solid.svg" alt="Next Page" />
	</router-link>
    <div class="page" style="background: #b4b5db; display: flex; flex-direction: column;">
        <div class="top-history-creators" style="width: 100%; height: 10%;">
            Your Top 5 Favorite Creators
        </div>
        <br class="space-for-title"/>

        <div style="height: 80%">
            <div class="side-by-side-chart" style="display: flex; flex-direction: row; width: 100%; height: 100%">
                <div class="col ranking ">
                    <div class="place ranking">
                        <img class="ellipse ranking"
                            v-bind:src="photos[4] === '' ? 'src/assets/images/user_default.png' : photos[4]" />
                        <div class="rectangle-place"
                            style=" width: auto; top: -22.5px; z-index: 1; padding: 2px 5px 2px 5px;">
                            <p class="number-placement">#5</p>
                        </div>
                    </div>
                    <div class="rectangle" id="rect-15" :style="{ background: colors[4] }">
                        <p class="text-inside-rectangle" style="padding-right: 35%; height: 80%; padding-bottom: rect-150%;"> {{ creators[4] }} </p>
                    </div>
                </div>
                <div class="col ranking">
                    <div class="place ranking">
                        <img class="ellipse ranking"
                            v-bind:src="photos[1] === '' ? 'src/assets/images/user_default.png' : photos[1]" />
                        <div class="rectangle-place"
                            style=" width: auto; top: -22.5px; z-index: 1; padding: 2px 5px 2px 5px;">
                            <p class="number-placement">#2</p>
                        </div>
                    </div>
                    <div class="rectangle" id="rect-12" :style="{ background: colors[1] }">
                        <p class="text-inside-rectangle" style="padding-right: 40%;"> {{ creators[1] }} </p>
                    </div>
                </div>
                <div class="col ranking">
                    <div class="place ranking">
                        <img class="ellipse ranking"
                            v-bind:src="photos[0] === '' ? 'src/assets/images/user_default.png' : photos[0]" />
                        <div class="rectangle-place"
                            style=" width: auto; top: -22.5px; z-index: 1; padding: 2px 5px 2px 5px;">
                            <p class="number-placement">#1</p>
                        </div>
                    </div>
                    <div class="rectangle" id="rect-11" :style="{ background: colors[0] }">
                        <p class="text-inside-rectangle" style="padding-right: 40%;"> {{ creators[0] }} </p>
                    </div>
                </div>
                <div class="col ranking">
                    <div class="place ranking">
                        <img class="ellipse ranking"
                            v-bind:src="photos[2] === '' ? 'src/assets/images/user_default.png' : photos[2]" />
                        <div class="rectangle-place"
                            style=" width: auto; top: -22.5px; z-index: 1; padding: 2px 5px 2px 5px;">
                            <p class="number-placement">#3</p>
                        </div>
                    </div>
                    <div class="rectangle" id="rect-13" :style="{ background: colors[2] }">
                        <p class="text-inside-rectangle" style="padding-right: 30%; height: 80%; padding-bottom: 20%;">
                            {{ creators[2] }} </p>
                    </div>
                </div>
                <div class="col ranking">
                    <div class="place ranking">
                        <img class="ellipse ranking"
                            v-bind:src="photos[3] === '' ? 'src/assets/images/user_default.png' : photos[3]" />
                        <div class="rectangle-place"
                            style=" width: auto; top: -22.5px; z-index: 1; padding: 2px 5px 2px 5px;">
                            <p class="number-placement">#4</p>
                        </div>
                    </div>
                    <div class="rectangle" id="rect-14" :style="{ background: colors[3] }">
                        <p class="text-inside-rectangle" style="padding-right: 35%; height: 80%; padding-bottom: 1%;"> {{ creators[3] }} </p>
                    </div>
                </div>


            </div>
        </div>
    </div>
</template>


<style>
.rectangle {
    width: 100%;
    overflow: hidden;
    top: 30px;
    border-radius: 30px 30px 0px 0px;
}

#rect-11 {
    position: relative;
    height: 528px;
    animation: growup-11 5s;
}

#rect-12 {
    position: relative;
    height: 450px;
    animation: growup-12 5s;
}

#rect-13 {
    position: relative;
    height: 379px;
    animation: growup-13 5s;
}

#rect-14 {
    position: relative;
    height: 316px;
    animation: growup-14 5s;
}

#rect-15 {
    position: relative;
    height: 272px;
    animation: growup-15 5s;
}

@keyframes growup-11 {
    0% {
        height: 0px;
    }

    100% {
        height: 528px;
    }
}

@keyframes growup-12 {
    0% {
        height: 0px;
    }

    100% {
        height: 450px;
    }
}

@keyframes growup-13 {
    0% {
        height: 0px;
    }

    100% {
        height: 379px;
    }
}

@keyframes growup-14 {
    0% {
        height: 0px;
    }

    100% {
        height: 316px;
    }
}


@keyframes growup-15 {
    0% {
        height: 0px;
    }

    100% {
        height: 272px;
    }
}
</style>

<script>
import axios from 'axios'
import { defineComponent } from 'vue'
import html2canvas from 'html2canvas';

export default defineComponent({
    name: 'TopLikedCreators',
    data() {
        return {
            creators: [],
            photos: [],
            colors: []
        }
    },
    methods: {
        async captureAndSave() {
            // Use html2canvas to capture the content
            const element = document.getElementById('your-component-id'); // Replace with your component's ID
            const canvas = await html2canvas(element);

            // Convert canvas to image
            const image = canvas.toDataURL('image/png');

            // Create a download link
            const link = document.createElement('a');
            link.href = image;
            link.download = 'top_creators.png';
            document.body.appendChild(link);

            // Trigger the download
            link.click();

            // Remove the link from the DOM
            document.body.removeChild(link);
        },
    },
    async beforeMount() {
        await axios.get("http://localhost:8000/top-creator-favorites")
            .then((response) => {
                console.log(response.data)
                this.creators = Object.values(response.data['Username']);
                this.photos = Object.values(response.data['Photo']);
                this.colors = Object.values(response.data['Colors']);
            })
            .catch((error) => {
                console.log(error)
            })
    }
})
</script>