<script setup lang="ts">
import { ref, computed } from 'vue'

const props = defineProps({
	size: {
		type: Number,
		default: 1,
	},
	bkg: {
		type: String,
		default: '#ffffff',
	},
	lightText: {
		type: Boolean,
		default: false,
	}
})

const container = ref('complication__container')

const setGridState = computed(() => {
	if (props.size == 1) return;
	return props.size == 2 ? 'medium-grid-size' : 'large-grid-size';
})

const setTextLight = computed(() => {
	if (!props.lightText) return;
	return 'text--light';
})

const test = () => {
	// Testing REST API
	fetch(import.meta.env.VITE_BACKEND_URL + '/api/v1/rest-test-2')
	.then(response => {
		return response.json()
	})
	.then(data => {
		// Testing response
		console.log(data)
	})
}
</script>

<template>
    <div id="test" 
		 :class="[container, setGridState, setTextLight]" 
		 :style="{ backgroundColor: bkg }" 
		 data-tilt 
		 data-tilt-glare data-tilt-max-glare="0.5"
		 data-tilt-max="20">
		<slot />
    </div>
</template>

<style scoped>
.complication__container {
	display: grid;
	grid-template-columns: auto;
	gap: 3.1rem;
	align-items: center;
	justify-items: stretch;
	padding: 0.8rem;
	border-radius: 1rem;
	box-shadow: 10px 10px 25px var(--box-shadow-black);
}
.medium-grid-size {
	grid-column: auto / span 2;
	grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
}
.large-grid-size {
	grid-column: auto / span 3;
	grid-row: auto / span 2;
}
.text--light {
	color: #ededed;
}
</style>