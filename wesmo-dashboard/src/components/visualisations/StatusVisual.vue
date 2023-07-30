<script setup lang="ts">
import { computed, shallowRef } from 'vue'
import { Tick1, Alert2, ArrowDown } from '@iconsans/vue';
import type { CSSProperties, Component } from 'vue';

const props = defineProps({
    textValue: {
        type: String,
    },
    statusValue: {
        type: String,
    },
    stateValue: {
        type: Number,
        default: 0,
    },
})

const icons = shallowRef([
    Tick1,
    Alert2,
    ArrowDown,
])

const setState = computed(() => {
    let icon: Component;
    switch(props.stateValue) {
        case 1:
            icon = icons.value[0];
            break;
        case 3:
            icon = icons.value[2];
            break;
        case 2:
        default:
            icon = icons.value[1];
            break;
    }
    return icon;
})
const setStateColour = computed(() => {
    let colour: string = '';
    switch(props.stateValue) {
        case 1:
            colour = '#15efa1';
            break;
        case 3:
            colour = '#ffcc68';
            break;
        case 2:
        default:
            colour = '#ff7272';
            break;
    }
    return colour;
})
const setIconStyle = computed(() => {
    const iconStyle: CSSProperties = {
        backgroundColor: setStateColour.value,
    }
    return iconStyle;
})
</script>

<template>
    <div class="status__container">
        <component :is="setState" class="status__icon" :style="setIconStyle" />
        <p class="status__text-status">{{ statusValue }}</p>
        <p class="status__text-label">{{ textValue }}</p>
    </div>
</template>

<style scoped>
.status__icon {
    color: var(--color-text);
    font-size: 2.2rem;
    padding: 0.2rem;
    border-radius: 50%;
}
.status__text-label {
    font-size: 0.9rem;
}
.status__text-status {
    font-size: 2rem;
    transform: translateY(-10px);
}
.status__container {
    text-align: center;
}
</style>