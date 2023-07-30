<script setup lang="ts">
import { computed } from 'vue'
import type { CSSProperties } from 'vue';

const props = defineProps({
    textValue: {
        type: String,
    },
    currentValue: {
        type: Number,
        default: 0,
    },
    maxValue: {
        type: Number,
        default: 1,
    },
})

const setProgress = computed(() => {
    return Math.round((props.currentValue / props.maxValue) * 100);
})
const setColour = computed(() => {
    const progress: number = setProgress.value;
    let colour: string = '';
    switch(true) {
        case (progress >= 70):
            colour = '#15efa1';
            break;
        case (progress >= 30):
            colour = '#ffcc68';
            break;
        default:
            colour = '#ff7272';
            break;
    }
    return colour;
})
const setBarStyle = computed(() => {
    const barStyle: CSSProperties = {
        width: setProgress.value + '%',
        backgroundColor: setColour.value,
    }
    return barStyle;
})
</script>

<template>
    <div>
        <p class="bar__text-label">{{ textValue }}</p>
        <p class="bar__text-value">{{ setProgress + '%' }}</p>
    </div>
    <div class="bar__container">
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
    background-color: #ffcc68;
    border-radius: 1rem;
}
</style>