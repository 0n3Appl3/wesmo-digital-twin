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
const test = ref()

const socket = io(import.meta.env.VITE_BACKEND_URL);

socket.on('error', (error) => {
	errorMessage.value = error + '\n';
})
socket.on('event', (arg: any) => {
	// battery.value = arg
	test.value = arg
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
	<h1>{{ test }}</h1>
	<SplashScreen :loading="loading" :error="error" :error-message="errorMessage"/>
	<TitleBar />
	<ComplicationsGrid :data="battery"/>
</template>

<style scoped>

</style>
