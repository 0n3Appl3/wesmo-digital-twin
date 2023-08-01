<script setup lang="ts">

defineProps({
    parameterOne: {
        type: Object,
    },
    parameterTwo: {
        type: Object,
    }
})
</script>

<template>
    <div class="number__container">
        <p class="number__text-label">{{ parameterOne?.text }}</p>
        <p class="number__text-value">{{ parameterOne?.value }}<span>{{ parameterOne?.unit }}</span></p>
        <p class="number__text-label">{{ parameterTwo?.text }}</p>
        <p class="number__text-value">{{ parameterTwo?.value }}<span>{{ parameterTwo?.unit }}</span></p>
    </div>
</template>

<style scoped>
.number__icon {
    font-size: 1.4rem;
}
.number__text-label {
    font-size: 1rem;
}
.number__text-value {
    font-size: 3rem;
}
.number__text-value > span {
    font-size: 0.7rem;
    margin-left: 0.2rem;
}
.number__container {
    text-align: center;
}
</style>