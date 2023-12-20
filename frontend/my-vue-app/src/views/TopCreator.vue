<template>
    <div class="page" 
        style="color:white; background-image: linear-gradient(to bottom, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 1) 50%, rgba(0, 0, 0, 1)); padding:auto;">
        
        <div class="scroll-parent" style="position:fixed; z-index: -1;">
			<div class="scroll-element four" style="position:fixed;">
				<img src="../assets/images/black_tiktok_pattern.png" />
			</div>
			<div class="scroll-element three" style="position:fixed;">
				<img src="../assets/images/black_tiktok_pattern.png" />
			</div>
			<div class="scroll-element two" style="position:fixed;">
				<img src="../assets/images/black_tiktok_pattern.png" />
			</div>
			<div class="scroll-element one" style="position:fixed;">
				<img src="../assets/images/black_tiktok_pattern.png" />
			</div>
		</div>
        
        <img class="tik-tok-logo" src="../assets/images/tiktok-logo.png" /> 
        <router-link to="/trends">
            <img class="arrow-left" src="../assets/images/arrow-left-solid.svg" alt="Previous Page" />
        </router-link>
        <router-link to="/summary">
            <img class="arrow-right" src="../assets/images/arrow-right-solid.svg" alt="Next Page" />
        </router-link>
        <div class="row" style="height:45%; padding-top: 10px; padding-bottom: 55px;">
            <!-- Create a white border -->
            <div style="border: 5px solid white; border-radius: 50%; width: 300px; height: 300px; margin: auto;">
                <!-- Center the image -->
                <div style="width: 100%; height: 100%; position: relative;">
                    <div style="width: 15%; height: 10%; border: 1px solid white; border-radius: 5px; position: absolute; margin: auto; top:7%; right:7%">
                        <div style=" font-family: 'futura-maxi-cg-bold';width: 100%; height: 100%; background-color: black; border-radius: 5px; display:flex; align-items: center; justify-content: center; font-weight: 1000; font-size:larger;">
                            #1
                        </div>
                    </div>
                    <img v-bind:src="topCreatorImage === '' ? 'src/assets/images/sound_default.png' : topCreatorImage" style="background-color:cyan;width: 300px; height: 300px; border-radius: 50%;">
                    <div style="width: 50%; height: 10%; border: 5px solid white; border-radius: 50px; position: relative; margin: auto; bottom: 7%; ">
                        <div style=" font-family: 'futura-maxi-cg-bold';width: 100%; height: 100%; background-color: black; border-radius: 50px; display:flex; align-items: center; justify-content: center;">
                            {{ topCreator }}
                        </div>
                    </div>
                </div>
            </div>
        </div>

        
        <div style="margin: auto; display:flex; flex-direction: column; justify-content: space-between; height:40%; font-size:large;">
            <div class="row">
                <div class="row" style=" font-family: 'futura-maxi-cg-bold';font-weight: bolder;">
                    Your Top Watched Creator
                </div>
                <div class="row" style=" font-family: 'futura-maxi-cg-bold';">
                    {{ topCreator }}
                </div>
            </div>
            <div class="row">
                <div class="row" style="font-weight: bolder; font-family: 'futura-maxi-cg-bold'; ">
                    # Tiktok Watched
                </div>
                <div class="row" style=" font-family: 'futura-maxi-cg-bold';">
                    {{ timesWatched }}
                </div>
            </div>
            <div class="row">
                <div class="row" style="font-weight: bolder; font-family: 'futura-maxi-cg-bold';">
                    # Tiktok Liked
                </div>
                <div class="row" style=" font-family: 'futura-maxi-cg-bold';">
                    {{ timesLikes }}
                </div>
            </div>
            <div class="row">
                <div class="row" style="font-weight: bolder; font-family: 'futura-maxi-cg-bold';">
                    # Tiktok Favorite
                </div>
                <div class="row" style=" font-family: 'futura-maxi-cg-bold';">
                    {{ timesFavorite }}
                </div>
            </div>
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

    export default defineComponent({
        name: 'TopCreator',
        data() {
            return {
                topCreator: "",
                topCreatorImage: "",
                timesWatched: 0,
                timesLikes: 0,
                timesFavorite: 0,
            }
        },
        async created() {
            axios.get("http://localhost:8000/top-creator-overall")
                .then((response) => {
                    console.log(response.data)
                    this.topCreator = response.data['Username']["0"];
                    this.topCreatorImage = response.data['Photo']["0"];
                    this.timesWatched = response.data['Count_History']["0"];
                    this.timesLikes = response.data['Count_Likes']['0'];
                    this.timesFavorite = response.data['Count_Favorites']['0'];
                })
                .catch((error) => {
                    console.log(error)
                })
        },
        methods: {
        }
        
    })

</script>