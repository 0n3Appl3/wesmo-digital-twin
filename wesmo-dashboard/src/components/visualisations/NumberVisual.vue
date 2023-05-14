<script lang="ts">
import { InformationSquare } from '@iconsans/vue'

export default {
    props: {
        textValue: {
            type: String,
        },
        numberValue: {
            type: Number,
            default: 0,
        },
        textSuffix: {
            type: String,
            default: '',
        }
    },
    data() {
        return {
            icon: 'number__icon',
            label: 'number__text-label',
            value: 'number__text-value',
            container: 'number__container',
        }
    },
    components: { InformationSquare }
};
</script>

<template>
    <div :class="container">
        <InformationSquare :class="icon"/>
        <p :class="value">{{ numberValue }}<span>{{ textSuffix }}</span></p>
        <p :class="label">{{ textValue }}</p>
    </div>
</template>

<style scoped>
.number__icon {
    font-size: 1.4rem;
}
.number__text-label {
    font-size: 0.9rem;
}
.number__text-value {
    font-size: 2.2rem;
}
.number__text-value > span {
    font-size: 0.7rem;
    margin-left: 0.2rem;
}
.number__container {
    text-align: center;
}
</style>