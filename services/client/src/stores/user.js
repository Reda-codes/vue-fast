import { defineStore } from 'pinia';

export const useUser = defineStore('user', {
    state: () => ({
        user: {},
    }),

    getters: {
        getUser: (state) => state.user,
        getStatus: (state) => state.status,
    },

    actions: {
        setUser(data) {
            this.user = data
        },
        resetUser() {
            this.user = {}
        }
    },
})