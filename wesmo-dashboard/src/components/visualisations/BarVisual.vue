<script lang="ts">
export default {
    props: {
        textValue: {
            type: String
        },
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
            label: 'bar__text-label',
            value: 'bar__text-value',
            container: 'bar__container',
        }
    },
    computed: {
		setProgress() {
			return Math.round((this.currentValue / this.maxValue) * 100) + '%';
		},
	},
};
</script>

<template>
    <div>
        <p :class="label">{{ textValue }}</p>
        <p :class="value">{{ setProgress }}</p>
    </div>
    <div :class="container">
        <span :style="{ width: setProgress }"></span>
    </div>
</template>

<style scoped>
.bar__text-label {
    font-size: 0.9rem;
}
.bar__text-value {
    font-size: 2rem;
}
.bar__container {
    box-sizing: content-box;
    position: relative;
    overflow: hidden;
    height: 1.3rem;
    border-radius: 1rem;
    background-color: #ddd;
}
.bar__container > span {
    display: block;
    position: relative;
    overflow: hidden;
    height: 100%;
    background-color: #26e35b;
    border-radius: 1rem;
}
</style>