<script setup lang="ts">
import { ref, computed } from 'vue'

const props = defineProps({
	size: {
		type: Number,
		default: 1,
	},
})

const wrapper = ref('wrapper')
const container = ref('complication__container')

const setGridState = computed(() => {
	if (props.size == 1) return;
	return props.size == 2 ? 'medium-grid-size' : 'large-grid-size';
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
    <div :class="[container, setGridState]">
		<div :class="wrapper" @click="test">
			<slot />
		</div>
    </div>
</template>

<style scoped>
.complication__container {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: left;
	padding: 0.8rem;
	border-radius: 2rem;
	box-shadow: 10px 10px 30px var(--white-box-shadow-1),
				-10px -10px 30px var(--white-box-shadow-2);
}
.complication__container:hover {
	box-shadow: inset 10px 10px 30px var(--white-box-shadow-1),
				inset -10px -10px 30px var(--white-box-shadow-2);
	cursor: pointer;
}
.complication__container:hover > .wrapper {
	transform: scale(0.97);
}
.medium-grid-size {
	grid-column: auto / span 2;
}
.large-grid-size {
	grid-column: auto / span 3;
	grid-row: auto / span 2;
}
</style>