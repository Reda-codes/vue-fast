<script setup>
import { ref } from 'vue'
import { useUser } from '../stores/user';
import { useData } from '../stores/data';


function formatDate(dateString) {
    const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    
    const date = new Date(dateString);
    const dayOfMonth = date.getUTCDate();
    const month = months[date.getUTCMonth()];
    const year = date.getUTCFullYear();
    
    return `${dayOfMonth} ${month} ${year}`;
}

// stores for data and user
const userStore = useUser()
const dataStore = useData();

//current tab state
const view = ref('dashboard')

// Function to switch the view between dashboard and recommendations tab
const switchView = (val) => {
    view.value = val;
    console.log(userStore.getUser.notifications);
}



</script>

<template>
    <!-- Desktop view -->
    <div class="hidden md:block">
        <!-- body Header -->
        <div class="w-full flex bg-white h-16 border-2 border-b-gray-200 font-bold text-gray-400">
            <div class="w-1/4 flex ">
                <button v-if="userStore.getUser.name" class="w-10" @click="userStore.resetUser">
                    <svg  class="w-8 h-8 fill-current" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                        <path stroke-width="2" d="M13.83 19a1 1 0 0 1-.78-.37l-4.83-6a1 1 0 0 1 0-1.27l5-6a1 1 0 0 1 1.54 1.28L10.29 12l4.32 5.36a1 1 0 0 1-.78 1.64z"></path>
                    </svg>
                </button>
                <h1 v-if="userStore.getUser.name" class="text-black text-center my-auto">
                    {{ userStore.getUser.name }}
                </h1>
                <h1 v-else class="text-black text-center my-auto mx-auto">
                    Select a client
                </h1>
            </div>
            <button class="mx-5 px-2" :class="view === 'dashboard'? 'text-blue-500 border-b-2 border-b-blue-500' : ''" @click="switchView('dashboard')">Dashboard</button>
            <button class="mx-5 px-2" :class="view === 'recommendations'? 'text-blue-500 border-b-2 border-b-blue-500' : ''" @click="switchView('recommendations')">Recommendations</button>
        </div>

        <!-- Main Body -->
        <div class="flex ">
            <!-- Body Sidebar -->
            <div class="fixed w-1/4  h-[86%] bg-white  border-r-2 border-r-gray-200 overflow-y-auto">
                <!-- If user is selected -->
                <div v-if="userStore.getUser.name">
                    <div class="flex flex-col items-center justify-center">
                        
                    <!--  Customer Details  -->
                    <div class="w-full">
                        <input type="checkbox" name="panel" id="panel-1" class="hidden">
                        <label for="panel-1" class="relative bg-white text-gray-800 font-bold p-4 border-b border-grey-400 flex">
                            <svg class="w-5" viewBox="0 -256 1792 1792">
                            <g transform="matrix(1,0,0,-1,197.42373,1300.6102)">
                                <path d="M 1408,131 Q 1408,11 1335,-58.5 1262,-128 1141,-128 H 267 Q 146,-128 73,-58.5 0,11 0,131 0,184 3.5,234.5 7,285 17.5,343.5 28,402 44,452 q 16,50 43,97.5 27,47.5 62,81 35,33.5 85.5,53.5 50.5,20 111.5,20 9,0 42,-21.5 33,-21.5 74.5,-48 41.5,-26.5 108,-48 Q 637,565 704,565 q 67,0 133.5,21.5 66.5,21.5 108,48 41.5,26.5 74.5,48 33,21.5 42,21.5 61,0 111.5,-20 50.5,-20 85.5,-53.5 35,-33.5 62,-81 27,-47.5 43,-97.5 16,-50 26.5,-108.5 10.5,-58.5 14,-109 Q 1408,184 1408,131 z m -320,893 Q 1088,865 975.5,752.5 863,640 704,640 545,640 432.5,752.5 320,865 320,1024 320,1183 432.5,1295.5 545,1408 704,1408 863,1408 975.5,1295.5 1088,1183 1088,1024 z"/>
                            </g>
                            </svg>
                            <h3 class="ml-1 ">
                                Customer Details
                            </h3>
                        </label>
                        <div class="accordion__content overflow-auto bg-gray-100">
                            <div class="p-5">
                                <h3 class="pt-2 pl-2 font-bold">
                                    {{ userStore.getUser.name }}
                                </h3>
                                <a :href=" 'https://' + userStore.getUser.website " target="_blank" class="pl-2 hover:text-blue-700">
                                    {{ userStore.getUser.website }}
                                </a>
                                <h2 class="font-bold pl-2 pt-4">Contact</h2>
                                <div class="flex justify-start flex-wrap text-xs md:text-base lg:text-base xl:text-lg pl-2 pb-5">
                                    <a class="flex p-1 m-1 px-3 rounded-2xl bg-yellow-300 hover:bg-yellow-500" :href="'tel:' + userStore.getUser.phone" target="_blank">
                                        <svg class="w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none">
                                        <path d="M3 5.5C3 14.0604 9.93959 21 18.5 21C18.8862 21 19.2691 20.9859 19.6483 20.9581C20.0834 20.9262 20.3009 20.9103 20.499 20.7963C20.663 20.7019 20.8185 20.5345 20.9007 20.364C21 20.1582 21 19.9181 21 19.438V16.6207C21 16.2169 21 16.015 20.9335 15.842C20.8749 15.6891 20.7795 15.553 20.6559 15.4456C20.516 15.324 20.3262 15.255 19.9468 15.117L16.74 13.9509C16.2985 13.7904 16.0777 13.7101 15.8683 13.7237C15.6836 13.7357 15.5059 13.7988 15.3549 13.9058C15.1837 14.0271 15.0629 14.2285 14.8212 14.6314L14 16C11.3501 14.7999 9.2019 12.6489 8 10L9.36863 9.17882C9.77145 8.93713 9.97286 8.81628 10.0942 8.64506C10.2012 8.49408 10.2643 8.31637 10.2763 8.1317C10.2899 7.92227 10.2096 7.70153 10.0491 7.26005L8.88299 4.05321C8.745 3.67376 8.67601 3.48403 8.55442 3.3441C8.44701 3.22049 8.31089 3.12515 8.15802 3.06645C7.98496 3 7.78308 3 7.37932 3H4.56201C4.08188 3 3.84181 3 3.63598 3.09925C3.4655 3.18146 3.29814 3.33701 3.2037 3.50103C3.08968 3.69907 3.07375 3.91662 3.04189 4.35173C3.01413 4.73086 3 5.11378 3 5.5Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                        </svg>
                                        <span class="pl-1"> Call </span>
                                    </a>
                                    <a class="flex p-1 m-1 px-3 rounded-2xl bg-yellow-300 hover:bg-yellow-500" :href="'mailto:' + userStore.getUser.email" target="_blank">
                                        <svg class="w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none">
                                        <path d="M4 7.00005L10.2 11.65C11.2667 12.45 12.7333 12.45 13.8 11.65L20 7" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                        <rect x="3" y="5" width="18" height="14" rx="2" stroke="#000000" stroke-width="2" stroke-linecap="round"/>
                                        </svg>
                                        <span class="pl-1"> Email </span>
                                    </a>
                                    <a class="flex p-1 m-1 px-3 rounded-2xl bg-yellow-300 hover:bg-yellow-500" :href="'https://www.google.com/maps/place/' + userStore.getUser.location[0] + ',' + userStore.getUser.location[1]" target="_blank">
                                        <svg class="w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none">
                                        <path d="M5.7 15C4.03377 15.6353 3 16.5205 3 17.4997C3 19.4329 7.02944 21 12 21C16.9706 21 21 19.4329 21 17.4997C21 16.5205 19.9662 15.6353 18.3 15M12 9H12.01M18 9C18 13.0637 13.5 15 12 18C10.5 15 6 13.0637 6 9C6 5.68629 8.68629 3 12 3C15.3137 3 18 5.68629 18 9ZM13 9C13 9.55228 12.5523 10 12 10C11.4477 10 11 9.55228 11 9C11 8.44772 11.4477 8 12 8C12.5523 8 13 8.44772 13 9Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                        </svg>
                                        <span class="pl-1"> Map </span>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- Call Notes -->
                    <div class="w-full">
                        <input type="checkbox" name="panel" id="panel-2" class="hidden">
                        <label for="panel-2" class="relative block bg-white text-gray-800 font-bold p-4 border-b border-grey-400">User Notes</label>
                        <div class="accordion__content overflow-auto bg-gray-100">
                            <div v-if="!userStore.getUser.notes[0]">
                                <h3 class="p-2 text-center">
                                    The user has not left any notes
                                </h3>
                            </div>
                            <div v-for="(item, index) in userStore.getUser.notes" :key="index" class="p-2 border-b-2 border-gray-300">
                                <h3 class="font-bold">
                                    {{  item.type }}
                                </h3>
                                <h3>
                                    {{ item.message }}
                                </h3>
                            </div>
                        </div>
                    </div>
                    <!--  Panel 3  -->
                    <div class="w-full">
                        <input type="checkbox" name="panel" id="panel-3" class="hidden">
                        <label for="panel-3" class="relative block bg-white text-gray-800 font-bold p-4 border-b border-grey-400">Panel 3</label>
                        <div class="accordion__content overflow-auto bg-gray-100">
                        <p class="accordion__body p-4">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iusto possimus at a cum saepe molestias modi illo facere ducimus voluptatibus praesentium deleniti fugiat ab error quia sit perspiciatis velit necessitatibus.Lorem ipsum dolor sit amet, consectetur
                            adipisicing elit. </p>
                        </div>
                    </div>
                </div>
                </div>
                <!-- when no user is selected -->
                <div v-else class="p-2 pt-4">
                    <div v-for="(item, index) in dataStore.getData.customers" :key="index" class="w-11/12 mx-auto rounded-xl p-2 border-2 mb-4">
                        <h1 class="text-gray-800 font-bold cursor-pointer m-1 hover:text-blue-700 text-base md:text-base lg:text-base xl:text-lg" @click="userStore.setUser(item)"> {{ item.name}} </h1>
                        <a :href=" 'https://' + item.website " target="_blank" class="text-gray-800 m-1"> {{ item.website}} </a>
                    </div>
                </div>
            </div>
            <!-- Body recommendation section -->
            <div v-if="view !== 'dashboard'" class=" fixed w-3/4 h-[86%] bg-gray-100 left-1/4 pt-64">
                <h1 class=" block text-3xl text-center">
                    So you want my recommendations!
                </h1>
                <p class="text-center">I recommend that you take a break, book a flight to Japan, and visit Nago island.</p>
            </div>
            <!-- Body dashboard section -->
            <div v-else-if="userStore.getUser.name" class=" fixed flex justify-around w-3/4 p-6 bg-gray-100 h-[86%] overflow-scroll left-1/4">
                <!-- Sales play Section -->
                <div class="w-5/12 h-full p-5 overflow-y-auto">
                    <h1 class="text-gray-600 text-lg font-bold" >Sales Plays</h1>
                    <div>
                        <div v-for="(item, index) in userStore.getUser.notifications" :key="index" class="p-5">
                            <div class="border-2 border-gray-300 bg-white w-full p-5">
                                <div v-if="item.type === 'feedback'" class="p-2">
                                    <h3 class="font-semibold">{{  item.title }}</h3>
                                </div>
                                <div v-else class="p-2">
                                    <h3 class="font-semibold">{{  item.title }}</h3>
                                </div>
                                
                                <div class="lg:flex">
                                    <img v-if="item.type === 'feedback'" src="https://placehold.co/50x70/" alt="" class="w-1/3 mr-3">
                                    <div v-if="item.type === 'feedback'" class="pt-5">
                                        <h3 class="text-sm lg:text-base font-bold lg:pb-2">{{ item.product.name }}</h3>
                                        <h3 class="text-sm ">{{'Viewed ' + formatDate(item.date) }}</h3>
                                        <button class="mt-5 p-2 bg-yellow-500 rounded-2xl text-sm lg:text-sm">
                                            Add to Order
                                        </button>
                                    </div>
                                    <div v-else>
                                        <h3 class="font-semibold text-2xl mb-4 ml-2">{{ "$" + item.amount.current }}</h3>
                                        <h3 class="m-2 font-semibold text-sm">{{ item.message }}</h3>
                                        <div class="flex m-2">
                                            <svg class="w-5 mr-2 text-orange-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none">
                                            <path opacity="0.1" d="M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" fill="rgb(234 88 12)"/>
                                            <path d="M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" stroke="rgb(234 88 12)" stroke-width="2"/>
                                            <path d="M12 8L12 13" stroke="rgb(234 88 12)" stroke-width="2" stroke-linecap="round"/>
                                            <path d="M12 16V15.9888" stroke="rgb(234 88 12)" stroke-width="2" stroke-linecap="round"/>
                                            </svg>
                                            <h2 class="text-sm lg:text-base"> 
                                                {{ item.note }}
                                            </h2>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Feed Section -->
                <div class="w-1/2 h-full p-5 overflow-y-auto">
                    <h1 class="text-gray-600 text-lg font-bold">Activity Feed</h1>
                    <div>
                        <div v-for="(item, index) in userStore.getUser.activity" :key="index" class="p-5 flex">
                            <div class="flex justify-center flex-col mr-3 text-blue-500">
                                <svg class="w-16" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none">
                                <path d="M12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2ZM17.19 15.94C17.15 16.03 17.1 16.11 17.03 16.18L15.34 17.87C15.19 18.02 15 18.09 14.81 18.09C14.62 18.09 14.43 18.02 14.28 17.87C13.99 17.58 13.99 17.1 14.28 16.81L14.69 16.4H9.1C7.8 16.4 6.75 15.34 6.75 14.05V12.28C6.75 11.87 7.09 11.53 7.5 11.53C7.91 11.53 8.25 11.87 8.25 12.28V14.05C8.25 14.52 8.63 14.9 9.1 14.9H14.69L14.28 14.49C13.99 14.2 13.99 13.72 14.28 13.43C14.57 13.14 15.05 13.14 15.34 13.43L17.03 15.12C17.1 15.19 17.15 15.27 17.19 15.36C17.27 15.55 17.27 15.76 17.19 15.94ZM17.25 11.72C17.25 12.13 16.91 12.47 16.5 12.47C16.09 12.47 15.75 12.13 15.75 11.72V9.95C15.75 9.48 15.37 9.1 14.9 9.1H9.31L9.72 9.5C10.01 9.79 10.01 10.27 9.72 10.56C9.57 10.71 9.38 10.78 9.19 10.78C9 10.78 8.81 10.71 8.66 10.56L6.97 8.87C6.9 8.8 6.85 8.72 6.81 8.63C6.73 8.45 6.73 8.24 6.81 8.06C6.85 7.97 6.9 7.88 6.97 7.81L8.66 6.12C8.95 5.83 9.43 5.83 9.72 6.12C10.01 6.41 10.01 6.89 9.72 7.18L9.31 7.59H14.9C16.2 7.59 17.25 8.65 17.25 9.94V11.72Z" fill="rgb(59 130 246)"/>
                                </svg>
                            </div>
                            <div class="border-2 border-gray-300 bg-white w-full p-5">
                                <h1 class="font-semibold text-2xl mb-4">
                                    {{"$" + item.sum }}
                                </h1>
                                <h2 class="text-sm lg:text-base">
                                    {{ item.title }}
                                </h2>
                                <div class="flex m-2">
                                    <svg class="w-5 mr-2 text-orange-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none">
                                    <path opacity="0.1" d="M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" fill="rgb(234 88 12)"/>
                                    <path d="M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" stroke="rgb(234 88 12)" stroke-width="2"/>
                                    <path d="M12 8L12 13" stroke="rgb(234 88 12)" stroke-width="2" stroke-linecap="round"/>
                                    <path d="M12 16V15.9888" stroke="rgb(234 88 12)" stroke-width="2" stroke-linecap="round"/>
                                    </svg>
                                    <h2 class="text-sm lg:text-base"> 
                                        {{ item.message }}
                                    </h2>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Body dashboard No user selected -->
            <div v-else class=" fixed h-[86%]  w-3/4 bg-gray-100 left-1/4 pt-64">
                <svg class="w-40 mx-auto" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none">
                <path opacity="0.1" d="M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" fill="#323232"/>
                <path d="M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" stroke="#323232" stroke-width="2"/>
                <path d="M12 8L12 13" stroke="#323232" stroke-width="2" stroke-linecap="round"/>
                <path d="M12 16V15.9888" stroke="#323232" stroke-width="2" stroke-linecap="round"/>
                </svg>
                <h1 class=" block text-3xl font-bold text-center text-gray-700">Please select a Client</h1>
            </div>
        </div>
    </div>

    <!-- Phone View -->
    <div class="md:hidden">
        <div class="fixed w-full bg-gray-100 min-h-full border-r-2 border-r-gray-200 overflow-y-auto">
            <!-- Client Selected View -->
            <div v-if="userStore.getUser.name">
                            <div class="">
                                <h3 class="pt-4 pl-2 font-semibold mb-5 text-2xl">
                                    Contact
                                </h3>
                                <div class="flex justify-around flex-wrap text-xs md:text-base lg:text-base xl:text-lg pl-2 pb-5">
                                    <a class="flex w-1/4 p-1 px-3 rounded-2xl bg-yellow-300 hover:bg-yellow-500" :href="'tel:' + userStore.getUser.phone" target="_blank">
                                        <svg class="w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none">
                                        <path d="M3 5.5C3 14.0604 9.93959 21 18.5 21C18.8862 21 19.2691 20.9859 19.6483 20.9581C20.0834 20.9262 20.3009 20.9103 20.499 20.7963C20.663 20.7019 20.8185 20.5345 20.9007 20.364C21 20.1582 21 19.9181 21 19.438V16.6207C21 16.2169 21 16.015 20.9335 15.842C20.8749 15.6891 20.7795 15.553 20.6559 15.4456C20.516 15.324 20.3262 15.255 19.9468 15.117L16.74 13.9509C16.2985 13.7904 16.0777 13.7101 15.8683 13.7237C15.6836 13.7357 15.5059 13.7988 15.3549 13.9058C15.1837 14.0271 15.0629 14.2285 14.8212 14.6314L14 16C11.3501 14.7999 9.2019 12.6489 8 10L9.36863 9.17882C9.77145 8.93713 9.97286 8.81628 10.0942 8.64506C10.2012 8.49408 10.2643 8.31637 10.2763 8.1317C10.2899 7.92227 10.2096 7.70153 10.0491 7.26005L8.88299 4.05321C8.745 3.67376 8.67601 3.48403 8.55442 3.3441C8.44701 3.22049 8.31089 3.12515 8.15802 3.06645C7.98496 3 7.78308 3 7.37932 3H4.56201C4.08188 3 3.84181 3 3.63598 3.09925C3.4655 3.18146 3.29814 3.33701 3.2037 3.50103C3.08968 3.69907 3.07375 3.91662 3.04189 4.35173C3.01413 4.73086 3 5.11378 3 5.5Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                        </svg>
                                        <span class="pl-1 mx-auto text-base"> Call </span>
                                    </a>
                                    <a class="flex w-1/4 p-1 px-3 rounded-2xl bg-yellow-300 hover:bg-yellow-500" :href="'mailto:' + userStore.getUser.email" target="_blank">
                                        <svg class="w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none">
                                        <path d="M4 7.00005L10.2 11.65C11.2667 12.45 12.7333 12.45 13.8 11.65L20 7" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                        <rect x="3" y="5" width="18" height="14" rx="2" stroke="#000000" stroke-width="2" stroke-linecap="round"/>
                                        </svg>
                                        <span class="pl-1 mx-auto text-base"> Email </span>
                                    </a>
                                    <a class="flex w-1/4 p-1 px-3 rounded-2xl bg-yellow-300 hover:bg-yellow-500" :href="'https://www.google.com/maps/place/' + userStore.getUser.location[0] + ',' + userStore.getUser.location[1]" target="_blank">
                                        <svg class="w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none">
                                        <path d="M5.7 15C4.03377 15.6353 3 16.5205 3 17.4997C3 19.4329 7.02944 21 12 21C16.9706 21 21 19.4329 21 17.4997C21 16.5205 19.9662 15.6353 18.3 15M12 9H12.01M18 9C18 13.0637 13.5 15 12 18C10.5 15 6 13.0637 6 9C6 5.68629 8.68629 3 12 3C15.3137 3 18 5.68629 18 9ZM13 9C13 9.55228 12.5523 10 12 10C11.4477 10 11 9.55228 11 9C11 8.44772 11.4477 8 12 8C12.5523 8 13 8.44772 13 9Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                        </svg>
                                        <span class="pl-1 mx-auto text-base"> Map </span>
                                    </a>
                                </div>
                                <h3 class="text-xs sm:text-base text-gray-800 ml-5 font-semibold" >Total spending (Vs Last year)</h3>
                                

                            </div>
            </div>

            <!-- Clients list View-->
            <div v-else class="p-2 flex flex-wrap">
                <div v-for="(item, index) in dataStore.getData.customers" :key="index" class="w-full sm:w-1/2 p-4">
                    <div class="w-full rounded-3xl p-2 border-2 ">
                        <h1 class="text-gray-800 font-bold cursor-pointer m-1 hover:text-blue-700" @click="userStore.setUser(item)"> {{ item.name}} </h1>
                        <a :href=" 'https://' + item.website " target="_blank" class="text-gray-800 m-1"> {{ item.website}} </a>
                    </div>
                </div>
            </div>
        </div>
    </div>


</template>

<style scoped>
label:after {
    content: '+';
    position: absolute;
    right: 1em;
    color: #3b3b3b;
}

input:checked + label:after {
    content: '-';
    line-height: .8em;
}

.accordion__content{
    max-height: 0em;
    overflow-y: auto;
    transition: all 0.4s cubic-bezier(0.865, 0.14, 0.095, 0.87);
}
input[name='panel']:checked ~ .accordion__content {
  /* Get this as close to what height you expect */
    max-height: 50em;
    overflow-y: auto;
}
</style>