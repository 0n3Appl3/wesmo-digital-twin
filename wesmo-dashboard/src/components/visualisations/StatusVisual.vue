<script lang="ts">
import { ArrowUp } from '@iconsans/vue'

export default {
    props: {
        textValue: {
            type: String,
        },
        statusValue: {
            type: String,
        },
    },
    data() {
        return {
            icon: 'status__icon',
            label: 'status__text-label',
            status: 'status__text-status',
            container: 'status__container',
        }
    },
    components: { ArrowUp }
};
</script>

<template>
    <div :class="container">
        <ArrowUp :class="icon"/>
        <p :class="status">{{ statusValue }}</p>
        <p :class="label">{{ textValue }}</p>
    </div>
</template>

<style scoped>
.status__icon {
    font-size: 2.2rem;
    background-color: greenyellow; /* placeholder colour */
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