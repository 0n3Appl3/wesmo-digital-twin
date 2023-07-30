<script setup lang="ts">
import { onMounted, ref } from 'vue'
import BarVisual from '../visualisations/BarVisual.vue';
import NumberVisual from '../visualisations/NumberVisual.vue';
import PieVisual from '../visualisations/PieVisual.vue';
import StatusVisual from '../visualisations/StatusVisual.vue';
import ComplicationTemplate from './ComplicationTemplate.vue';

const bar = ref({
    text: 'Test Component',
    current: 0.47,
    max: 1,
})
const number = ref({
    text: 'Test Component',
    value: 1234,
    suffix: 'test',
})
const status = ref({
    text: 'Test Component',
    status: 'Normal',
    state: 1, 
})
const pie = ref({
    text: 'Test Component',
    current: 37,
    max: 100,
    suffix: '%',  
})

const redBkg = ref('#d54646')
const greyBkgDark = ref('#555555')
const greyBkgDim = ref('#d3d3d3')
const greyBkgLight = ref('#e8e8e8')

/*
 * Note: Polling interval is 60,000 milliseconds (1 minute). Not an ideal scenario for an application that
 * needs to be as close to real-time as possible. Might consider looking into other options later.
 * Alternative solution: WebSockets
 */
const pollingDelay = ref(60000)
let placeholder = ref('placeholder')

onMounted(() => {
    checkForNewData()
})

/*
 * Note: setTimeout is better than setInterval because if the server happens to be slow, I could
 * have multiple pending requests because setInterval executes after a set amount of time has elapsed
 * whether the previous calls have been fulfilled or not.
 */
const checkForNewData = () => {
    setTimeout(async () => {
        const response = await fetch(import.meta.env.VITE_BACKEND_URL + '/api/v1/test')
        switch(response.status) {
            case 200:
                placeholder.value = await response.json()
                break;
            case 204:
                break;
            default:
                break;
        }
        checkForNewData()
    }, pollingDelay.value)
}
</script>

<template>
    <p>{{ placeholder }}</p>
    <div class="grid__container">
        <div class="grid">
            <ComplicationTemplate :size="1" :bkg="redBkg" :light-text="true">
                <BarVisual :text-value="bar.text" :current-value="bar.current" :max-value="bar.max"/>
            </ComplicationTemplate>
            <ComplicationTemplate :size="1" :bkg="greyBkgDim">
                <NumberVisual :text-value="number.text" :number-value="number.value" :text-suffix="number.suffix"/>
            </ComplicationTemplate>
            <ComplicationTemplate :size="1" :bkg="greyBkgDark" :light-text="true">
                <StatusVisual :text-value="status.text" :status-value="status.status" :state-value="status.state"/>
            </ComplicationTemplate>
            <ComplicationTemplate :size="1" :bkg="greyBkgDim">
                <PieVisual :text-value="pie.text" :current-value="pie.current" :max-value="pie.max" :text-suffix="pie.suffix" :bkg="greyBkgDim"/>
            </ComplicationTemplate>
            <ComplicationTemplate :size="2" :bkg="greyBkgLight">
                <PieVisual :text-value="pie.text" :current-value="pie.current" :max-value="pie.max" :text-suffix="pie.suffix" :bkg="greyBkgLight"/>
                <BarVisual :text-value="bar.text" :current-value="bar.current" :max-value="bar.max"/>
            </ComplicationTemplate>
            <ComplicationTemplate :size="2" :bkg="greyBkgLight">
                <NumberVisual :text-value="number.text" :number-value="number.value" :text-suffix="number.suffix"/>
                <NumberVisual :text-value="number.text" :number-value="number.value" :text-suffix="number.suffix"/>
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