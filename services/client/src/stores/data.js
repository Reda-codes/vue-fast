import { defineStore } from 'pinia';

export const useData = defineStore('data', {
    state: () => ({
        data: {},
        status: false
    }),

    getters: {
        getData: (state) => state.data,
        getCostumers: (state) => state.data?.costumers,
        getStatus: (state) => state.status,
    },

    actions: {
        async fetchInitialData() {
            try {
                // Requesting initial data from the api
                const response = await fetch(import.meta.env.VITE_API_URL);
                const data = await response.json();
                this.data = {...data};
                this.status = true;
            }
            catch (error) {
                alert("An error was encountered while fetching the data please check the console")
                console.log(error)
            }
        },
    },
})