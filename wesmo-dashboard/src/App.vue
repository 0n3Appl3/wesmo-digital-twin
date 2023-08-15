<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { io } from 'socket.io-client'
import SplashScreen from './components/SplashScreen.vue';
import TitleBar from './components/TitleBar.vue';
import ComplicationsGrid from './components/complications/ComplicationsGrid.vue';

const loading = ref(true)
const error = ref(false)
const splashScreenWaitTime = ref(1)
const testValue = ref()

const socket = io(import.meta.env.VITE_BACKEND_URL);

socket.on('event', (arg: any) => {
	console.log(arg)
	testValue.value = arg
})

onMounted(() => {
	setTimeout(async () => {
		await fetch(import.meta.env.VITE_BACKEND_URL + '/api/v1/test').then(() => {
			loading.value = false;
		}).catch(() => {
			error.value = true;
		})
	}, splashScreenWaitTime.value * 1000)
})
</script>

<template>
	<SplashScreen :loading="loading" :error="error"/>
	<TitleBar />
	<ComplicationsGrid :data="testValue"/>
</template>

<style scoped>

</style>
