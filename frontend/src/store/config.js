import { defineStore } from 'pinia';
import store from 'store'

export const useConfigStore = defineStore({
    id: 'configure',
    state: () => ({
        config: store.get('accessToken') !== undefined,
        toolbar: store.get('toolbar') !== true,
        fixed: 3,
    }),
    actions: {
        async setLocation() {            
            store.set('accessToken', 'teste')
    },
    async setToolbar() {  
        console.log(this.toolbar)              
        store.set('toolbar', !this.toolbar)
        this.toolbar = store.get('toolbar')
    },
    async setFixed(value) {  
        this.fixed = value
    },
    getters: {
        async getLocation() {
         return this.config
        }
    }
    }
});
