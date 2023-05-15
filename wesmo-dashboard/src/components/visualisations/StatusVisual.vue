<script lang="ts">
import { Tick1, Alert2, ArrowDown } from '@iconsans/vue';
import type { CSSProperties } from 'vue';

export default {
    props: {
        textValue: {
            type: String,
        },
        statusValue: {
            type: String,
        },
        stateValue: {
            type: Number,
            default: 0,
        }
    },
    data() {
        return {
            icons: ['Tick1', 'Alert2', 'ArrowDown'],
            icon: 'status__icon',
            label: 'status__text-label',
            status: 'status__text-status',
            container: 'status__container',
        }
    },
    computed: {
        setState() {
            let icon: string = '';
            switch(this.stateValue) {
                case 1:
                    icon = this.icons[0];
                    break;
                case 3:
                    icon = this.icons[2];
                    break;
                case 2:
                default:
                    icon = this.icons[1];
                    break;
            }
            return icon;
        },
        setStateColour() {
            let colour: string = '';
            switch(this.stateValue) {
                case 1:
                    colour = '#26e35b';
                    break;
                case 3:
                    colour = '#d95243';
                    break;
                case 2:
                default:
                    colour = '#efc015';
                    break;
            }
            return colour;
        },
        setIconStyle() {
            const iconStyle: CSSProperties = {
                backgroundColor: this.setStateColour,
            }
            return iconStyle;
        },
    },
    components: { Tick1, Alert2, ArrowDown }
};
</script>

<template>
    <div :class="container">
        <component :is="setState" :class="icon" :style="setIconStyle" />
        <p :class="status">{{ statusValue }}</p>
        <p :class="label">{{ textValue }}</p>
    </div>
</template>

<style scoped>
.status__icon {
    font-size: 2.2rem;
    padding: 0.2rem;
    border-radius: 50%;
}
.status__text-label {
    font-size: 0.9rem;
}
.status__text-status {
    font-size: 2rem;
    transform: translateY(-10px);
}
.status__container {
    text-align: center;
}
</style>