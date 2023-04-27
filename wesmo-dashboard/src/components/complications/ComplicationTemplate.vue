<script lang="ts">
export default {
    props: {
        size: Number,
    },
    data() {
        return {
            container: 'container',
        }
    },
};
</script>

<template>
    <div :class="container">
        <p>Insert complication information<br/>Size: {{ size }}</p>
    </div>
</template>

<style scoped>
.container {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	padding: 1rem;
	width: 15rem;
	height: 15rem;
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
</style>