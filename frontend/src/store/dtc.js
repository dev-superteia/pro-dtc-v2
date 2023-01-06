import { defineStore } from 'pinia';
import axios from "axios";
export const useDtcStore = defineStore({
    id: 'dtc',
    state: () => ({
        plant: [],
        mkg: [],
        line:[],
    }),
    actions: {
        async setPlant() {       
            if(this.plant.length > 0){
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
        async setMkg() {       
            if(this.plant.length == 0){
                const response = await axios.get("http://localhost:8000/api/v1/multselect/market_segment");
                this.mkg.push({ text: 'All', value: '' })
                this.line.push({ text: 'All', value: '' })
                for (let i = 0; i < response.data.length; i++) {
                    const nome = response.data[i].denomination ? ' - ' + response.data[i].denomination : ''      
                    this.mkg.push({ text: response.data[i].line, value: response.data[i].mkg_segm })
                    this.line.push({ text: response.data[i].mkg_segm + nome, value: response.data[i].mkg_segm })
                }
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
