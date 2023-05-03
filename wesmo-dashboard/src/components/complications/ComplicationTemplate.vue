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
            container: 'container',
        }
    },
	computed: {
		setGridState() {
			if (this.size == 1) return;
			return this.size == 2 ? 'medium-grid-size' : 'large-grid-size';
		}
	},
};
</script>

<template>
    <div :class="[container, setGridState]">
        <p>Size: {{ size }}</p>
		<slot />
    </div>
</template>

<style scoped>
.container {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	padding: 1rem;
	border-radius: 2rem;
	background: var(--colour-background);
	box-shadow: 10px 10px 30px var(--white-box-shadow-1),
				-10px -10px 30px var(--white-box-shadow-2);
}

.container:hover {
	box-shadow: inset 10px 10px 30px var(--white-box-shadow-1),
				inset -10px -10px 30px var(--white-box-shadow-2);
	cursor: pointer;
}

.medium-grid-size {
	grid-column: auto / span 2;
}

.large-grid-size {
	grid-column: auto / span 3;
	grid-row: auto / span 2;
}
</style>