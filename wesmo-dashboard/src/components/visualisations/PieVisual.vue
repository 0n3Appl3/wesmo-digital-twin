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
			default: 100,
		},
        textSuffix: {
            type: String,
        },
        safeThreshold: {
            type: Number,
            default: 55,
        },
        warningThreshold: {
            type: Number,
            default: 80,
        },
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
            const progress: number = this.setProgress;
            let pieColour: string = '';
            switch(true) {
                case (progress <= this.safeThreshold):
                    pieColour = '#26e35b';
                    break;
                case (progress > this.safeThreshold && progress <= this.warningThreshold):
                    pieColour = '#efc015';
                    break;
                default:
                    pieColour = '#d95243';
                    break;
            }
            return pieColour;
        },
        setColour() {
            let colour: string = '';
            if (this.setProgress <= this.halfPieSize) {
                colour = '#ddd';
            } else {
                colour = this.setPieColour;
            }
            return colour;
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
    box-shadow:  8px 8px 16px #bcbcbc,
            -8px -8px 16px #fefefe;
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
    background: linear-gradient(to right, v-bind(setPieColour) 50%, #ddd 50%);
}
.pie__wrapper.pie__progress:before {
    background: v-bind(setColour);
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