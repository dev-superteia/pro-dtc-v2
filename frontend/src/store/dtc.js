import { defineStore } from 'pinia';
import axios from "axios";
export const useDtcStore = defineStore({
    id: 'dtc',
    state: () => ({
        plant: [],
    }),
    actions: {
        async setPlant() {       
            if(this.plant.length > 0){
                console.log('elses')
                return this.plant
            } else {
                const response = await axios.get("http://localhost:8000/api/v1/multselect/plant");
                this.plant.push({ text: 'All', value: '' })
                for (let i = 0; i < response.data.length; i++) {
                    this.plant.push({ text: response.data[i].plant + ' - ' + response.data[i].plant_desc, value: response.data[i].plant })
                }
                return this.plant
            }
            
    },
    getters: {
        async getPlant() {
            console.log('dfsf')
         return this.plant
        }
    }
    }
});
