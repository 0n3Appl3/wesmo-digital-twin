<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { io } from 'socket.io-client'
import SplashScreen from './components/SplashScreen.vue';
import TitleBar from './components/TitleBar.vue';
import ComplicationsGrid from './components/complications/ComplicationsGrid.vue';

const loading = ref(true)
const error = ref(false)
const splashScreenWaitTime = ref(1)
const battery = ref()
const errorMessage = ref('')
const results = ref()

const socket = io(import.meta.env.VITE_BACKEND_URL);

socket.on('error', (error) => {
	errorMessage.value = error + '\n';
})
socket.on("connect_error", (err) => {
  console.log(`connect_error due to ${err.message}`);
});
socket.on('connect', () => {
	socket.emit('join-room')
})
socket.on('receive-battery-data', (arg: any) => {
	battery.value = arg
})
socket.on('receive-twin-results', (arg: any) => {
	results.value = JSON.parse(arg)
})

onMounted(() => {
	setTimeout(async () => {
		await fetch(import.meta.env.VITE_SEQUELIZE_URL + '/api/v1/test').then(() => {
			loading.value = false;
		}).catch((error) => {
			errorMessage.value = error;
			error.value = true;
		})
	}, splashScreenWaitTime.value * 1000)
})
</script>

<template>
	<SplashScreen :loading="loading" :error="error" :error-message="errorMessage"/>
	<TitleBar />
	<ComplicationsGrid :data="battery" :twin="results"/>
</template>

<style scoped>

</style>