<script setup lang="ts">
const props = defineProps({
    loading: {
        type: Boolean,
        default: false,
    },
})
</script>

<template>
    <div :class="{ splash__background: true, splash__animate: !props.loading }">
        <img src="/wesmo-logo.png" alt="WESMO Logo" />
        <p>Loading...</p>
    </div>
</template>

<style scoped>
.splash__background {
    /* background-color: #63ab97; */
    bottom: 0;
    display: block;
    font-size: 32px;
    left: 0;
    overflow: hidden;
    padding-top: 10vh;
    position: fixed;
    right: 0;
    text-align: center;
    top: 0;
    z-index: 99;
}
.splash__background > img {
    width: 20rem;
}
.splash__animate {
  animation: animateout 2s forwards ease-in-out;
}

@keyframes animateout {
  to {
    opacity: 0;
    visibility: hidden;
  }
}
</style>