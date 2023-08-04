<script setup lang="ts">
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
			<svg class="spinner" viewBox="0 0 50 50">
				<circle class="path" cx="25" cy="25" r="20" fill="none" stroke-width="5"></circle>
			</svg>
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
/* Spinner Animation Credit: https://codepen.io/supah/pen/BjYLdW */
.spinner {
  animation: rotate 2s linear infinite;
  z-index: 2;
  display: block;
  position: absolute;
  left: 50%;
  margin: -25px 0 0 -25px;
  width: 50px;
  height: 50px;
  
  & .path {
    stroke: #656565;
    stroke-linecap: round;
    animation: dash 1.5s ease-in-out infinite;
  }
  
}
@keyframes rotate {
  100% {
    transform: rotate(360deg);
  }
}
@keyframes dash {
  0% {
    stroke-dasharray: 1, 150;
    stroke-dashoffset: 0;
  }
  50% {
    stroke-dasharray: 90, 150;
    stroke-dashoffset: -35;
  }
  100% {
    stroke-dasharray: 90, 150;
    stroke-dashoffset: -124;
  }
}
</style>