<script lang="ts">
import BarVisual from '../visualisations/BarVisual.vue';
import NumberVisual from '../visualisations/NumberVisual.vue';
import PieVisual from '../visualisations/PieVisual.vue';
import StatusVisual from '../visualisations/StatusVisual.vue';
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
            },
            number: {
                text: 'Test Component',
                value: 1234,
                suffix: 'test',
            },
            status: {
                text: 'Test Component',
                status: 'Normal',
                state: 1,
            },
            pie: {
                text: 'Test Component',
                current: 0.45,
                max: 1,
            }
        }
    },
    components: { ComplicationTemplate, BarVisual, NumberVisual, StatusVisual, PieVisual }
};
</script>

<template>
    <div :class="container">
        <div :class="grid">
            <ComplicationTemplate :size="1">
                <BarVisual :text-value="bar.text" :current-value="bar.current" :max-value="bar.max"/>
            </ComplicationTemplate>
            <ComplicationTemplate :size="1">
                <NumberVisual :text-value="number.text" :number-value="number.value" :text-suffix="number.suffix"/>
            </ComplicationTemplate>
            <ComplicationTemplate :size="2">
                <BarVisual :text-value="bar.text" :current-value="bar.current" :max-value="bar.max"/>
            </ComplicationTemplate>
            <ComplicationTemplate :size="3">
                <BarVisual :text-value="bar.text" :current-value="bar.current" :max-value="bar.max"/>
            </ComplicationTemplate>
            <ComplicationTemplate :size="1">
                <StatusVisual :text-value="status.text" :status-value="status.status" :state-value="status.state"/>
            </ComplicationTemplate>
            <ComplicationTemplate :size="1">
                <PieVisual :text-value="pie.text" :current-value="pie.current" :max-value="pie.max" />
            </ComplicationTemplate>
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
    grid-template-columns: repeat(4, 12rem);
    grid-auto-rows: 12rem;
    grid-gap: 1.5rem 1.5rem;
    grid-auto-flow: row dense;
}
</style>