<template>
    <img class="tik-tok-logo" src="../assets/images/tiktok-logo.png" />
    <router-link to="/trends-message">
        <img class="arrow-left" src="../assets/images/arrow-left-solid.svg" alt="Previous Page" />
    </router-link>
    <router-link to="/trends">
        <img class="arrow-right" src="../assets/images/arrow-right-solid.svg" alt="Next Page" />
    </router-link>
    <div class="page"
        style="background-image: linear-gradient(to top, rgba(245, 246, 252, 0.52), #B4B5DB), url('/images/tiktok_pattern.png'); text-align: center;">
        <div class="row">
            <div
                style="padding-top:2%; font-family: futura-maxi-cg-bold;font-size: 20px;line-height: 24px; font-weight: 400;">
                Your Top 5 Trendy Sounds</div>
        </div>

        <!-- First pair -->
        <div class="trendy-rec-1">
            <div class="scroll-parent">
                <div class="scroll-element one">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                </div>
                <div class="scroll-element two">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                </div>
                <div class="scroll-element three">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                </div>
            </div>
            <div class="trendy-sound-text-sounds-div">
                <p class="trendy-sound-text" style="font-size: 20px;">#1</p>
            </div>
            <div class="trendy-sound-text-sounds-div">
                <p class="trendy-sound-text" style="font-size: 16px;"> {{ sounds[0] }}</p>
            </div>

            <img class="photo-sound" v-bind:src="photos[0] === '' ? 'src/assets/images/user_default.png' : photos[0]"
                style="position: absolute; right: 0; top: 50%; transform: translateY(-50%);" />
        </div>

        <div class="trendy-rec-2">

            <div class="scroll-parent">
                <div class="scroll-element one-inverse">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                </div>
                <div class="scroll-element three-inverse">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                </div>
            </div>
            <div class="trendy-sound-text-sounds-div-2">
                <p class="trendy-sound-text" style="text-align: right; font-size: 20px;">#2</p>
            </div>
            <div class="trendy-sound-text-sounds-div-2">
                <p class="trendy-sound-text" style="text-align: right; font-size: 16px;">{{ sounds[1] }}</p>
            </div>
            <img class="photo-sound" v-bind:src="photos[1] === '' ? 'src/assets/images/user_default.png' : photos[1]"
                style="position: absolute; left: 0; top: 50%; transform: translateY(-50%);" />
        </div>

        <!-- Second pair -->
        <div class="trendy-rec-1">
            <div class="scroll-parent">
                <div class="scroll-element one">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                </div>
                <div class="scroll-element two">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                </div>
                <div class="scroll-element three">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                </div>
            </div>
            <div class="trendy-sound-text-sounds-div">
                <p class="trendy-sound-text" style="font-size: 20px;">#3</p>
            </div>
            <div class="trendy-sound-text-sounds-div">
                <p class="trendy-sound-text" style="font-size: 16px;">{{ sounds[2] }}</p>
            </div>

            <img class="photo-sound" v-bind:src="photos[2] === '' ? 'src/assets/images/user_default.png' : photos[2]"
                style="position: absolute; right: 0; top: 50%; transform: translateY(-50%);" />
        </div>

        <div class="trendy-rec-2">
            <div class="scroll-parent">
                <div class="scroll-element one-inverse">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                </div>
                <div class="scroll-element three-inverse">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                </div>
            </div>
            <div class="trendy-sound-text-sounds-div-2">
                <p class="trendy-sound-text" style="text-align: right; font-size: 20px;">#4</p>
            </div>
            <div class="trendy-sound-text-sounds-div-2">
                <p class="trendy-sound-text" style="text-align: right; font-size: 16px;">{{ sounds[3] }}</p>
            </div>
            <img class="photo-sound" v-bind:src="photos[3] === '' ? 'src/assets/images/user_default.png' : photos[3]"
                style="position: absolute; left: 0; top: 50%; transform: translateY(-50%);" />
        </div>

        <!-- Third pair -->
        <div class="trendy-rec-1">
            <div class="scroll-parent">
                <div class="scroll-element one">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                </div>
                <div class="scroll-element two">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                </div>
                <div class="scroll-element three">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                    <img src="../assets/images/fourth.svg">
                    <img src="../assets/images/first.svg">
                    <img src="../assets/images/second.svg">
                    <img src="../assets/images/third.svg">
                </div>
            </div>
            
            <div class="trendy-sound-text-sounds-div">
                <p class="trendy-sound-text" style="font-size: 20px;">#5</p>
            </div>
            <div class="trendy-sound-text-sounds-div fifth-sound">
                <p class="trendy-sound-text" style="font-size: 16px;">{{ sounds[4] }}</p>
            </div>
            

            <img class="photo-sound" v-bind:src="photos[4] === '' ? 'src/assets/images/user_default.png' : photos[4]"
                style="position: absolute; right: 0; top: 50%; transform: translateY(-50%);" />
        </div>

        <div style="color: black; font-family: 'futura-maxi-cg-bold'; padding-top: 5%;">
            You listened to <span style="color: #fe2c55;">{{ seenTrends }}</span> of the <span style="color: #fe2c55;">{{
                totalTrends }}</span> trending sounds.
        </div>
    </div>
</template>

<style scoped lang="scss">
.scroll-parent {
    position: relative;
    width: 100%;
    height: 30%;
}

.scroll-element {
    display: flex;
    height: 100%;
    width: inherit;
    height: inherit;
    position: absolute;
    left: 0%;
    top: 0%;
}

.one {
    height:100%;
    animation: one 10s linear infinite;
}

.one-inverse {
    height: 100%;
    animation: one-inverse 10s linear infinite;
}

.two {
    height: 100%;
    animation: two 10s linear infinite;
}

.two-inverse {
    height: 100%;
    animation: two-inverse 10s linear infinite;
}

.three {
    height:100%;
    animation: three 10s linear infinite;
}



.three-inverse {
    height:100%;
    animation: three-inverse 10s linear infinite;
}

@keyframes one {
    from {
        left: 0%;
    }

    to {
        left: 100%;
    }
}

@keyframes two {
    from {
        left: 112%;
    }

    to {
        left: 212%;
    }
}

@keyframes three {
    from {
        left: -100%;
    }

    to {
        left: 0%;
    }
}


@keyframes one-inverse {
    from {
        left: 100%;
    }

    to {
        left: 0%;
    }
}

@keyframes three-inverse {
    from {
        left: 0%;
    }

    to {
        left: -100%;
    }
}
</style>


<script>
import axios from 'axios'
import { defineComponent } from 'vue'

export default defineComponent({
    name: 'TrendSounds',
    data() {
        return {
            sounds: [],
            photos: [],
            totalTrends: 0,
            seenTrends: 0,
        }
    },
    methods: {
    },
    async beforeMount() {
        await axios.get("http://localhost:8000/sound-trend")
            .then((response) => {
                console.log(response.data)
                this.sounds = Object.values(response.data['Trends']['Sound Name']);
                this.photos = Object.values(response.data['Trends']['Photo']);
                this.totalTrends = response.data['Total Trends'];
                this.seenTrends = response.data['Seen Trends'];
            })
            .catch((error) => {
                console.log(error)
            })
    }
})
</script>