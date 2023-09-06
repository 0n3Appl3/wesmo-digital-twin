<script setup lang="ts">
import { onMounted, ref, reactive, watch, onBeforeUpdate } from 'vue'
import BarVisual from '../visualisations/BarVisual.vue';
import NumberVisual from '../visualisations/NumberVisual.vue';
import PieVisual from '../visualisations/PieVisual.vue';
import StatusVisual from '../visualisations/StatusVisual.vue';
import ComplicationTemplate from './ComplicationTemplate.vue';
import RefreshButton from '../RefreshButton.vue';
import IconSpinner from '../icons/IconSpinner.vue';

const props = defineProps({
    data: {
        type: Object,
    },
})

/*
 * Battery data to display on the dashboard.
 */
const battery = reactive({
    status: {
        text: 'Battery Condition',
        status: 'Normal',
        state: 1,  
    },
    soc: {
        text: 'Actual State of Charge (SOC)',
        current: 0,
        max: 1,
    },
    soh: {
        text: 'State of Health (SOH)',
        current: 0,
        max: 100,
        suffix: '%', 
        reverseSafeThreshold: true, 
    },
    ampHour: {
        text: 'Battery Amp-Hour',
        value: 0,
        unit: 'Ah',
    },
    dischargeRate: {
        text: 'Discharge Time',
        value: 0,
        unit: 'h',
    },
    avgTemp: {
        text: 'Average Temperature',
        current: 0,
        max: 100,
        suffix: '˚C',  
    },
    packVoltage: {
        text: 'Pack Voltage',
        value: 0,
        unit: 'V',
    },
    packCurrent: {
        text: 'Pack Current',
        value: 0,
        unit: 'A',
    },
    lowestTemp: {
        text: 'Lowest Temperature',
        value: 0,
        unit: '˚C',
    },
    highestTemp: {
        text: 'Highest Temperature',
        value: 0,
        unit: '˚C',
    },
    estRemDistance: {
        text: 'Estimated Remaining Distance',
        value: 0,
        unit: 'km',
    },
    estSOC: {
        text: 'Estimated SOC',
        value: 0,
        unit: '%',
    }
})

const refreshing = ref(false)
const refreshAnimationTime = ref(1)
const lastUpdated = ref('')

const redBkg = ref('#d54646')
const greyBkgDark = ref('#555555')
const greyBkgDim = ref('#d3d3d3')
const greyBkgLight = ref('#e8e8e8')

/*
 * Set last updated value on dashboard.
 */
onMounted(() => {
    lastUpdated.value = new Date().toLocaleTimeString()
})

/*
 * Updates the dashboard information as battery data is received.
 */
onBeforeUpdate(() => {
    battery.soc.current = props.data?.packSOC ?? battery.soc.current;
    battery.ampHour.value = props.data?.packAmpHour ?? battery.ampHour.value;
    battery.avgTemp.current = props.data?.avgTemp ?? battery.avgTemp.current;
    battery.soh.current = props.data?.packHealth ?? battery.soh.current;
    battery.packVoltage.value = props.data?.packVoltage ?? battery.packVoltage.value;
    battery.packCurrent.value = props.data?.packCurrent ?? battery.packCurrent.value;
    battery.lowestTemp.value = props.data?.lowTemp ?? battery.lowestTemp.value;
    battery.highestTemp.value = props.data?.highTemp ?? battery.highestTemp.value;
    battery.dischargeRate.value = Math.round((battery.ampHour.value / battery.packCurrent.value) * 10) / 10;
    battery.dischargeRate.value = Number.isNaN(battery.dischargeRate.value) ? 0 : battery.dischargeRate.value == Infinity ? 0 : battery.dischargeRate.value;
})

/*
 * Updates last updated text when battery data is received.
 */
watch(props, () => {
    lastUpdated.value = new Date().toLocaleTimeString()
})

/*
 * Checks for new battery data.
 */
const checkForNewData = async () => {
    const response = await fetch(import.meta.env.VITE_BACKEND_URL + '/api/v1/test')
    refreshing.value = true
    switch(response.status) {
        case 200:
            lastUpdated.value = new Date().toLocaleTimeString()
            break;
        case 204:
            break;
        default:
            break;
    }
    setTimeout(() => {
        refreshing.value = false
    }, refreshAnimationTime.value * 1000)
}
</script>

<template>
    <div class="grid__container-outer">
        <div class="control__container">
            <RefreshButton @clicked="checkForNewData" />
            <Transition>
                <IconSpinner v-if="refreshing" class="control__spinner"/>
            </Transition>
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
                            :bkg="greyBkgLight"
                            :reverse-safe-threshold="battery.soh.reverseSafeThreshold"/>
                    <NumberVisual :parameter-one="battery.estRemDistance"
                            :parameter-two="battery.estSOC"/>
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
    max-width: 1100px;
    margin: 0 auto;
    padding-top: 1.5rem;
}
.grid__container {
    display: flex;
    justify-content: space-around;
}
.grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-auto-rows: 1fr;
    grid-gap: 1.5rem 1.5rem;
    grid-auto-flow: row dense;
}
.control__container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 1rem;
}
.v-enter-active, .v-leave-active {
    transition: opacity 0.5s ease;
}
.v-enter-from, .v-leave-to {
    opacity: 0;
}
@media screen and (max-width: 1100px) {
    .grid {
        grid-template-columns: repeat(2, 1fr);
    }
}
@media screen and (max-width: 600px) {
    .grid {
        grid-template-columns: repeat(1, 1fr);
    }
    .control__spinner {
        position: fixed;
        top: 8rem;
    }
}
</style>