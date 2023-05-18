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
            wrapper: 'pie__wrapper',
            label: 'bar__text-label',
            value: 'bar__text-value',
            container: 'pie__container',
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
    <div :class="container">
        <div class="pie__wrapper progress45">
        </div>
        <p :class="label">{{ textValue }}</p>
    </div>
</template>

<style scoped>
*:before {
    box-sizing: border-box;
}
.pie__wrapper {
    position: relative;
    border-radius: 50%;
    width: 80%;
    aspect-ratio: 1;
    margin: auto;
    margin-bottom: 0.5rem;
    overflow: hidden;
}
.pie__wrapper:before {
    content: '';
    display: block;
    transform-origin: left;
    margin-left: 50%;
    height: 100%;
}
.pie__wrapper.progress45 {
    background: linear-gradient(to right, #227ded 50%, #ddd 50%);
    /* transform: rotate(95 / 100 * 360deg * -1); */
}
.pie__wrapper.progress45:before {
    background: #ddd;
    transform: rotate(-5.96902604rad);
}
.bar__text-label {
    font-size: 0.9rem;
}
.bar__text-value {
    font-size: 2rem;
}
.pie__container {
    text-align: center;
}
</style>