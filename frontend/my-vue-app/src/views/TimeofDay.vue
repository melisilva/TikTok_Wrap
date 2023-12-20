<template>
	<div class="page"
		style="background-image: linear-gradient(to top, rgba(245, 246, 252, 0.52), #fadadd); text-align: center;">
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
		<router-link to="/minutes">
			<img class="arrow-left" src="../assets/images/arrow-left-solid.svg" alt="Previous Page" />
		</router-link>
		<router-link to="/ads-message">
			<img class="arrow-right" src="../assets/images/arrow-right-solid.svg" alt="Next Page" />
		</router-link>
		<div style="display: flex; flex-direction: column; justify-content: center; align-items: middle;">
			<div class="row">
				<div class="general-text" style="padding-top: 15%; color: black;">
					You usually do it during this time of the day...
				</div>
			</div>

			<div class="row">
				<div class="general-text" style="margin-top:5%; color: black;">
					...{{ time }}
				</div>
			</div>

			<div class="row" style="display: flex; flex-direction: row; justify-content: center;">
				<div class="quote-text" style="color: black;">
					{{ quote }}
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