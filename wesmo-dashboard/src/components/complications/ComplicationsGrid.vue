<script setup lang="ts">
import { onMounted, ref } from 'vue'
import BarVisual from '../visualisations/BarVisual.vue';
import NumberVisual from '../visualisations/NumberVisual.vue';
import PieVisual from '../visualisations/PieVisual.vue';
import StatusVisual from '../visualisations/StatusVisual.vue';
import ComplicationTemplate from './ComplicationTemplate.vue';
import RefreshButton from '../RefreshButton.vue';

const battery = ref({
    status: {
        text: 'Battery Condition',
        status: 'Normal',
        state: 1,  
    },
    soc: {
        text: 'State of Charge (SOC)',
        current: 0.47,
        max: 1,
    },
    predictedSoc : {
        text: 'Predicted SOC in the next minute',
        current: 0.44,
        max: 1,
    },
    soh: {
        text: 'State of Health (SOH)',
        current: 95,
        max: 100,
        suffix: '%',  
    },
    ampHour: {
        text: 'Battery Amp-Hour',
        value: 1000,
        unit: 'Ah',
    },
    dischargeRate: {
        text: 'Discharge Rate',
        value: 12.3,
        unit: 'A',
    },
    avgTemp: {
        text: 'Average Temperature',
        current: 37.5,
        max: 100,
        suffix: '˚C',  
    },
    packVoltage: {
        text: 'Pack Voltage',
        value: 12.3,
        unit: 'V',
    },
    packCurrent: {
        text: 'Pack Current',
        value: 12.3,
        unit: 'A',
    },
    lowestTemp: {
        text: 'Lowest Temperature',
        value: 12.3,
        unit: '˚C',
    },
    highestTemp: {
        text: 'Highest Temperature',
        value: 12.3,
        unit: '˚C',
    },
})

const lastUpdated = ref('')

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
    lastUpdated.value = new Date().toLocaleTimeString()
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
                lastUpdated.value = new Date().toLocaleTimeString()
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
    <div class="grid__container-outer">
        <div class="control__container">
            <!-- <RefreshButton /> -->
            <p>test</p>
            <p>Last Updated &bullet; {{ lastUpdated }}</p>
        </div>
        <div class="grid__container">
            <div class="grid">
                <ComplicationTemplate :size="1" :bkg="redBkg" :light-text="true">
                    <BarVisual :text-value="battery.soc.text" 
                            :current-value="battery.soc.current"
                            :max-value="battery.soc.max"/>
                </ComplicationTemplate>
                <ComplicationTemplate :size="1" :bkg="greyBkgDim">
                    <NumberVisual :parameter-one="battery.ampHour"
                                :parameter-two="battery.dischargeRate"/>
                </ComplicationTemplate>
                <ComplicationTemplate :size="1" :bkg="greyBkgDark" :light-text="true">
                    <StatusVisual :text-value="battery.status.text" 
                                :status-value="battery.status.status" 
                                :state-value="battery.status.state"/>
                </ComplicationTemplate>
                <ComplicationTemplate :size="1" :bkg="greyBkgDim">
                    <PieVisual :text-value="battery.avgTemp.text"
                            :current-value="battery.avgTemp.current" 
                            :max-value="battery.avgTemp.max" 
                            :text-suffix="battery.avgTemp.suffix" 
                            :bkg="greyBkgDim"/>
                </ComplicationTemplate>
                <ComplicationTemplate :size="2" :bkg="greyBkgLight">
                    <PieVisual :text-value="battery.soh.text"
                            :current-value="battery.soh.current" 
                            :max-value="battery.soh.max" 
                            :text-suffix="battery.soh.suffix"
                            :bkg="greyBkgLight"/>
                    <BarVisual :text-value="battery.predictedSoc.text" 
                            :current-value="battery.predictedSoc.current" 
                            :max-value="battery.predictedSoc.max"/>
                </ComplicationTemplate>
                <ComplicationTemplate :size="2" :bkg="greyBkgLight">
                    <NumberVisual :parameter-one="battery.packVoltage"
                                :parameter-two="battery.packCurrent"/>
                    <NumberVisual :parameter-one="battery.lowestTemp"
                                :parameter-two="battery.highestTemp"/>
                </ComplicationTemplate>
            </div>
        </div>
    </div>
</template>

<style scoped>
.grid__container-outer {
    max-width: 1280px;
    margin: 0 auto;
}
.grid__container {
    display: flex;
    /* max-width: 1280px; */
    justify-content: space-around;
}
.grid {
    display: grid;
    grid-template-columns: repeat(4, 15rem);
    grid-auto-rows: 15rem;
    grid-gap: 1.5rem 1.5rem;
    grid-auto-flow: row dense;
}
.control__container {
    display: flex;
    justify-content: space-between;
    padding-bottom: 1.5rem;
}
</style>