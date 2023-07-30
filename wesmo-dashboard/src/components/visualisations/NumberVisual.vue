<script setup lang="ts">
import { InformationSquare } from '@iconsans/vue'

defineProps({
    textValue: {
        type: String,
    },
    numberValue: {
        type: Number,
        default: 0,
    },
    textSuffix: {
        type: String,
        default: '',
    },
})
</script>

<template>
    <div class="number__container">
        <!-- <InformationSquare class="number__icon"/> -->
        <p class="number__text-label">{{ textValue }}</p>
        <p class="number__text-value">{{ numberValue }}<span>{{ textSuffix }}</span></p>
        <p class="number__text-label">{{ textValue }}</p>
        <p class="number__text-value">{{ numberValue }}<span>{{ textSuffix }}</span></p>
    </div>
</template>

<style scoped>
.number__icon {
    font-size: 1.4rem;
}
.number__text-label {
    font-size: 0.9rem;
}
.number__text-value {
    font-size: 2.2rem;
}
.number__text-value > span {
    font-size: 0.7rem;
    margin-left: 0.2rem;
}
.number__container {
    text-align: center;
}
</style>