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
			containerSizeValue: this.size * 10,
			containerSize: this.containerSizeValue + 'rem',
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
        <p>Complication<br/>Size: {{ size }}</p>
    </div>
</template>

<style scoped>
.container {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	padding: 1rem;
	width: v-bind(containerSize);
	height: v-bind(containerSize);
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
	grid-row: auto / span 2;
}

.large-grid-size {
	grid-column: auto / span 3;
	grid-row: auto / span 3;
}
</style>