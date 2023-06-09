<script setup lang="ts">
import { ref, computed } from 'vue'

const props = defineProps({
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
})

const halfPieSize = ref(50)

const setProgress = computed(() => {
    return Math.round((props.currentValue / props.maxValue) * 100);
})
const setPieColour = computed(() => {
    const progress: number = setProgress.value;
    let pieColour: string = '';
    switch(true) {
        case (progress <= props.safeThreshold):
            pieColour = '#26e35b';
            break;
        case (progress > props.safeThreshold && progress <= props.warningThreshold):
            pieColour = '#efc015';
            break;
        default:
            pieColour = '#d95243';
            break;
    }
    return pieColour;
})
const setColour = computed(() => {
    let colour: string = '';
    if (setProgress.value <= halfPieSize.value) {
        colour = '#ddd';
    } else {
        colour = setPieColour.value;
    }
    return colour;
})
const setPieSize = computed(() => {
    let rotationValue: number = 0;
    if (setProgress.value <= halfPieSize.value) {
        rotationValue = (100 - (50 - setProgress.value)) / 100 * 360 * -1;
    } else {
        rotationValue = (100 - setProgress.value) / 100 * 360;
    }
    return rotationValue + 'deg';
})
</script>

<template>
    <div class="pie__container">
        <div class="pie__wrapper pie__progress">
            <span class="pie__text-value">{{ setProgress }}<span>{{ textSuffix }}</span></span>
        </div>
        <p class="pie__text-label">{{ textValue }}</p>
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