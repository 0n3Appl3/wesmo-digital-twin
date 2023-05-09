<script lang="ts">
export default {
    props: {
        currentValue: {
            type: Number,
            default: 0,
        },
        maxValue: {
			type: Number,
			default: 1,
		}
    },
    data() {
        return {
            container: 'bar__container',
            value: 'bar__value',
        }
    },
    computed: {
		setProgress() {
			return 0;
		},
	},
};
</script>

<template>
    <div :class="container">
        <span :class="value"></span>
    </div>
</template>

<style scoped>
.bar__container {
    position: relative;
    height: 1.5rem;
    padding: 0.5rem;
    color: #ddd;
}

.bar__value {
    color: #26e35b;
}
</style>