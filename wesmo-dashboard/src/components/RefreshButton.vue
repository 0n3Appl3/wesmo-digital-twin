<script setup lang="ts">
import { RotateRight } from '@iconsans/vue';

const clicked = () => {
    alert('test')
}
</script>

<template>
    <button @click="clicked">
        <RotateRight class="refresh__icon"/>
        <span>Refresh</span>
    </button>
</template>

<style scoped>
button {
    display: flex;
    border: none;
    border-radius: 10rem;
    padding: 0.5rem 0.7rem;
    background-color: #373737;
    color: #ededed;
    justify-items:center;
}
span {
    padding-left: 0.3rem;
}
.refresh__icon {
    font-size: 1.2rem;
}
</style>