<script setup>
import {  onMounted } from 'vue'
import NavBar from './components/NavBar.vue';
import { useData } from './stores/data';

const dataStore = useData();

onMounted(() => {
  // Fetch initial data when the component is mounted
  dataStore.fetchInitialData();
});

const log = () => {
  console.log(dataStore.data);
}
</script>

<template>
  <header>
    <NavBar />
  </header>

  <main>
  <div>
    <p>Hello World</p>
    <button @click="log" >Click</button>
  </div>
  </main>
</template>

<style scoped>

</style>
