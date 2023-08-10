<script setup>
import { ref } from 'vue'
import { onClickOutside } from '@vueuse/core'

// Search field state
const searchField = ref('all');

//menu toggle state
const hamburgerMenuStatus = ref(false);


const target = ref(null)
const ignore = ref(null)

const input = ref("");

// Function to handle the searchField change
const handleSelectChange = (event) => {
    searchField.value = event.target.value;
}

// Function to handle Menu opening and closing when clicking on a button
const handleHamburgerClick = () => {
    hamburgerMenuStatus.value = !hamburgerMenuStatus.value
    console.log(hamburgerMenuStatus.value)
}

// function to handle click outside the menu to close it
onClickOutside(
    target,
    () => {
        
        hamburgerMenuStatus.value = !hamburgerMenuStatus.value
        console.log(hamburgerMenuStatus.value)
    },
    {ignore: [ignore]})

// Function to handle search request
const searchSubmit = async () => {
    console.log({input: input.value, field: searchField.value});
}
</script>

<template>
    <div class="w-full h-16 bg-blue-950 p-3 flex md:justify-between justify-end">

        <!-- +768px view for Laptops -->
        <div class="hidden  md:flex">
            <div class="w-10 mr-5" >
                <img src="/logo.png" alt="WebsiteLogo">
            </div>
            <form class="flex" @submit.prevent="searchSubmit">
                <input v-model="input" type="text" class="rounded-l-md bg-white w-64 pl-4 overflow-clip" placeholder="Search customers and products">
                <div class="rounded-r-md bg-white p-2 border-l-gray-200 border-l-2">
                    <select v-model="searchField" class="align-middle pr-2" :class="searchField === 'all' ? 'text-gray-400' : 'text-gray-800'" @change="handleSelectChange">
                        <option value="all" selected class="text-gray-800">All fields</option>
                        <option value="costumers" class="text-gray-800">Costumers</option>
                        <option value="products" class="text-gray-800">Products</option>
                        <option value="services" class="text-gray-800">Services</option>
                    </select>
                </div>
            </form>
        </div>

        <!-- From 425px to 768px view for Tablets -->
        <div class="md:hidden w-full flex justify-between">
            <div class="w-10 mr-5" >
                <img src="/logo.png" alt="WebsiteLogo">
            </div>
            <!-- button to return to clients -->
            <button type="button" class="items-center  w-15 h-15 text-white rounded-lg hidden" @click="close">
                <svg class="w-8 h-8 fill-current" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path stroke-width="2" d="M13.83 19a1 1 0 0 1-.78-.37l-4.83-6a1 1 0 0 1 0-1.27l5-6a1 1 0 0 1 1.54 1.28L10.29 12l4.32 5.36a1 1 0 0 1-.78 1.64z"></path>
                </svg>
            </button>
            
            <!-- Hamburger Button -->
            <button ref="ignore" type="button" class="items-center p-2 w-10 w- h-10 text-white rounded-lg md:hidden" @click="handleHamburgerClick">
                <svg class="w-6 h-6" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 17 14">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 1h15M1 7h15M1 13h15"/>
                </svg>
            </button>

            <div v-if="hamburgerMenuStatus" ref="target"  class="fixed z-20 top-0 left-0 bg-gray-800 w-2/3 sm:w-1/2 h-full mx-auto p-5">
                <div class="flex justify-between mb-10">
                    <div class="w-10 mr-5" >
                        <img src="/logo.png" alt="WebsiteLogo">
                    </div>
                    <button ref="ignore" type="button" class="block ml-auto text-white font-bold rounded-xl text-xl w-8 h-8 " @click="handleHamburgerClick">
                        X
                    </button>
                </div>

                <form class="" @submit.prevent="searchSubmit">
                    <input type="text" class=" block rounded-md bg-white w-11/12 p-1 mx-auto mb-5 text-xs sm:text-xs md:text-base" placeholder="Search customers & products">
                    <div class="flex justify-around">
                    <button type="submit" class="w-2/5 bg-white rounded-md">
                        Search
                    </button>
                    <select v-model="searchField" class="w-2/5 bg-white rounded-md p-1 align-middle text-xs sm:text-base" :class="searchField === 'all' ? 'text-gray-400' : 'text-gray-800'" @change="handleSelectChange">
                            <option value="all" class="text-gray-800" selected>All fields</option>
                            <option value="costumers" class="text-gray-800 bg-white">Costumers</option>
                            <option value="products" class="text-gray-800">Products</option>
                            <option value="services" class="text-gray-800">Services</option>
                        </select>
                    </div>

                </form>
            </div>
        </div>

        <!-- gray shade when the menu opens -->
        <div v-if="hamburgerMenuStatus" class="fixed top-0 left-0 w-full h-full bg-gray-700 z-10 opacity-50 md:hidden"></div>
    </div>
</template>

<style scoped>

</style>