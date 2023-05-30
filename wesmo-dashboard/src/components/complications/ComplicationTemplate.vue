<script lang="ts">
export default {
    props: {
        size: {
			type: Number,
			default: 1,
		}
    },
    data() {
        return {
			wrapper: 'wrapper',
            container: 'complication__container',
        }
    },
	computed: {
		setGridState() {
			if (this.size == 1) return;
			return this.size == 2 ? 'medium-grid-size' : 'large-grid-size';
		}
	},
	methods: {
		// Testing REST API
		test() {
			alert('test: ' + import.meta.env.VITE_TEST)
			fetch('http://127.0.0.1:3000/test')
			.then(response => {
				return response.json()
			})
			.then(data => {
				// Testing response
				alert(data.test)
				console.log(data)
			})
		}
	},
};
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