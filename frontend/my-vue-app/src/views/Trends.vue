<template>
	<div class="page"
		style="color:white; background-image: linear-gradient(to bottom, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 1) 50%, rgba(0, 0, 0, 1)); padding:auto; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh;">
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
		<router-link to="/trend-sounds">
			<img class="arrow-left" src="../assets/images/arrow-left-solid.svg" alt="Previous Page" />
		</router-link>
		<router-link to="/top-creator-overall">
			<img class="arrow-right" src="../assets/images/arrow-right-solid.svg" alt="Next Page" />
		</router-link>
		<div class="row" style="height:45%; padding-top: 10px; padding-bottom: 55px;">
			<!-- Create a white border -->
			<div style="border: 5px solid white; border-radius: 50%; width: 250px; height: 250px; margin: auto;">
				<!-- Center the image -->
				<div style="width: 100%; height: 100%; position: relative;">
					<img src='../assets/images/41NzLv-KoEL.jpg'
						style="background-color:cyan;width: 250px; height: 250px; border-radius: 50%;">
				</div>
			</div>
			<div class="general-text" style="color: #fe2c55; padding-top: 5%;">
				Trends
			</div>
		</div>
		<div class="trends" v-for="trend in trendsList" :key="trend" style="margin-top: -2%;">
			{{ trend }}<br />
		</div>

		<div class="row">
			<div class="general-text" style="text-align: center; font-size: 100%;">
				You have watched...
			</div>
			<div class="general-text" style="text-align: center; font-size: 100%; padding-top: 10%; color: #fe2c55;">
				{{ seenTrends }}
			</div>
			<div class="general-text" style="padding-top: 10%;font-size: 100%;">
				...out of <span style="color: #fe2c55;"> {{ totalTrends }}</span> trends!
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
import axios from 'axios'
import { defineComponent } from 'vue'

export default defineComponent({
	name: 'Trends',
	data() {
		return {
			trendsList: [],
			totalTrends: 0,
			seenTrends: 0,
		}
	},
	methods: {
	},
	async beforeMount() {
		await axios.get("http://localhost:8000/tiktok-trend")
			.then((response) => {
				console.log(response.data)
				this.trendsList = Object.values(response.data['Trends']);
				this.totalTrends = response.data['Total Trends'];
				this.seenTrends = response.data['Seen Trends'];
			})
			.catch((error) => {
				console.log(error)
			})
	}
})
</script>