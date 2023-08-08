<script setup lang="ts">
import { ref } from 'vue'
import { RotateRight } from '@iconsans/vue';

const emit = defineEmits(['clicked'])
const refreshText = ref('Refresh')

const clicked = () => {
    emit('clicked')
}
</script>

<template>
    <button @click="clicked">
        <RotateRight class="refresh__icon"/>
        <span>{{ refreshText }}</span>
    </button>
</template>

<style scoped>
button {
    display: flex;
    border: 2px solid #373737;
    border-radius: 10rem;
    padding: 0.5rem 0.7rem;
    background-color: #373737;
    color: #ededed;
    justify-items: center;
    align-items: center;
    transition: all 0.2s ease-in-out;
}
button:hover {
    cursor: pointer;
    color: #373737;
    background-color: #ededed;
}
span {
    padding-left: 0.3rem;
}
.refresh__icon {
    font-size: 1.2rem;
}
</style>