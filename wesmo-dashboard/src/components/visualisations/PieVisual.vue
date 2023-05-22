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
		},
        textSuffix: {
            type: String,
        }
    },
    data() {
        return {
            wrapper: 'pie__wrapper',
            progress: 'pie__progress',
            label: 'pie__text-label',
            value: 'pie__text-value',
            container: 'pie__container',
            halfPieSize: 50,
        }
    },
    computed: {
		setProgress() {
			return Math.round((this.currentValue / this.maxValue) * 100);
		},
        setPieColour() {
            let pieColour: string = '';
            if (this.setProgress <= this.halfPieSize) {
                pieColour = '#ddd';
            } else {
                pieColour = '#227ded';
            }
            return pieColour;
        },
        setPieSize() {
            let rotationValue: number = 0;
            if (this.setProgress <= this.halfPieSize) {
                rotationValue = (100 - (50 - this.setProgress)) / 100 * 360 * -1;
            } else {
                rotationValue = (100 - this.setProgress) / 100 * 360;
            }
            return rotationValue + 'deg';
        },
	},
};
</script>

<template>
    <div :class="container">
        <div :class="[wrapper, progress]">
            <span :class="value">{{ setProgress }}<span>{{ textSuffix }}</span></span>
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
.pie__wrapper.pie__progress {
    background: linear-gradient(to right, #227ded 50%, #ddd 50%);
}
.pie__wrapper.pie__progress:before {
    background: v-bind(setPieColour);
    transform: rotate(v-bind(setPieSize));
}
.pie__text-label {
    font-size: 0.9rem;
}
.pie__text-value {
    display: block;
    font-size: 2rem;
    text-align: center;
    transform: translateY(-90px);
}
.pie__text-value > span {
    font-size: 1rem;
}
.pie__container {
    text-align: center;
}
</style>