<script setup lang="ts">
import IconSpinner from './icons/IconSpinner.vue';

const props = defineProps({
    loading: {
        type: Boolean,
        default: false,
    },
    error: {
        type: Boolean,
        default: false,
    },
})
</script>

<template>
    <div :class="{ splash__background: true, splash__animate: !props.loading }">
		<div>
			<img src="/wesmo-logo.png" alt="WESMO Logo" />
			<IconSpinner />
			<p v-if="!props.error">Loading...</p>
			<p v-else>There is problem connecting to the server. Refresh the page to try again.</p>
		</div>
    </div>
</template>

<style scoped>
p {
	padding-top: 3rem;
}
.splash__background {
    /* background: var(--color-background); */
    background: linear-gradient(180deg, var(--colour-background-lighter) 0%, var(--colour-background-light) 100%);
    bottom: 0;
    display: flex;
	justify-content: center;
	align-items: center;
    font-size: 1rem;
    left: 0;
    overflow: hidden;
    position: fixed;
    right: 0;
    text-align: center;
    top: 0;
    z-index: 99;
}
.splash__background img {
    width: 25rem;
	padding-bottom: 2rem;
}
.splash__animate {
  animation: animateout 1s forwards cubic-bezier(0.165, 0.84, 0.44, 1);
}

@keyframes animateout {
  to {
    opacity: 0;
    visibility: hidden;
  }
}
</style>