<script lang="ts">
import type { CSSProperties } from 'vue';
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
			return Math.round((this.currentValue / this.maxValue) * 100);
		},
        setColour() {
            const progress: number = this.setProgress;
            let colour: string = '';
            switch(true) {
                case (progress >= 70):
                    colour = '#26e35b';
                    break;
                case (progress >= 30):
                    colour = '#efc015';
                    break;
                default:
                    colour = '#e33926';
                    break;
            }
            return colour;
        },
        setBarStyle() {
            const barStyle: CSSProperties = {
                width: this.setProgress + '%',
                backgroundColor: this.setColour,
            }
            return barStyle;
        },
	},
};
</script>

<template>
    <div>
        <p :class="label">{{ textValue }}</p>
        <p :class="value">{{ setProgress + '%' }}</p>
    </div>
    <div :class="container">
        <span :style="setBarStyle"></span>
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
    background-color: #efc015;
    border-radius: 1rem;
}
</style>