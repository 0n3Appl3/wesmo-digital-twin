<script lang="ts">
import ComplicationTemplate from './ComplicationTemplate.vue';

export default {
    data() {
        return {
            grid: 'grid',
        }
    },
    components: { ComplicationTemplate }
};
</script>

<template>
    <div :class="grid">
        <ComplicationTemplate :size="1" />
        <ComplicationTemplate :size="1" />
        <ComplicationTemplate :size="2" />
        <ComplicationTemplate :size="3" />
        <ComplicationTemplate :size="1" />
        <ComplicationTemplate :size="1" />
        <ComplicationTemplate :size="1" />
    </div>
</template>

<style scoped>
.grid {
    display: grid;
    grid-template-columns: repeat(4, 10rem);
    /* grid-template-rows: repeat(5, 10rem); */
    grid-auto-rows: 10rem;
    grid-gap: 1.5rem 1.5rem;
    grid-auto-flow: row dense;
    aspect-ratio: 1;
}
</style>