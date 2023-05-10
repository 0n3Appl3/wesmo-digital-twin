<script lang="ts">
import BarVisual from '../visualisations/BarVisual.vue';
import ComplicationTemplate from './ComplicationTemplate.vue';

export default {
    data() {
        return {
            container: 'grid__container',
            grid: 'grid',
            bar: {
                text: 'Test Component',
                current: 0.47,
                max: 1,
            }
        }
    },
    components: { ComplicationTemplate, BarVisual }
};
</script>

<template>
    <div :class="container">
        <div :class="grid">
            <ComplicationTemplate :size="1">
                <BarVisual :text-value="bar.text" :current-value="bar.current" :max-value="bar.max"/>
            </ComplicationTemplate>
            <ComplicationTemplate :size="1" />
            <ComplicationTemplate :size="2">
                <p><strong>Bold Text (font support?)</strong></p>
                <p><em>Italicised Text</em></p>
            </ComplicationTemplate>
            <ComplicationTemplate :size="3">
                <h1>Heading 1</h1>
                <p>Paragraph text</p>
            </ComplicationTemplate>
            <ComplicationTemplate :size="1" />
            <ComplicationTemplate :size="1" />
        </div>
    </div>
</template>

<style scoped>
.grid__container {
    display: flex;
    max-width: 1280px;
    justify-content: space-around;
    margin: 0 auto;
}
.grid {
    display: grid;
    grid-template-columns: repeat(4, 10rem);
    grid-auto-rows: 10rem;
    grid-gap: 1.5rem 1.5rem;
    grid-auto-flow: row dense;
    /* aspect-ratio: 1; */
}
</style>