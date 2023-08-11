<script setup>
import {  onMounted } from 'vue'
import NavBar from './components/NavBar.vue';
import  DashBoard from './components/DashBoard.vue';
import { useData } from './stores/data';

const dataStore = useData();

onMounted(() => {
  // Fetch initial data when the component is mounted
  dataStore.fetchInitialData();
});

</script>

<template>
  <header>
    <NavBar />
  </header>

  <main>
    <DashBoard />
  </main>
</template>

<style scoped>

</style>
