<template>
<h3>Raw Material Without Cost</h3>
<div class="grid p-fluid">
    <div class="col-12">
        <h3>{{$t('dtc.plant')}}</h3>
        <div class="p-inputgroup">
            <Dropdown optionLabel="text" v-model="plantSelected" :options="plant" placeholder="Select a plant"  @click="getPlant"/>
        </div>
    </div>
    <div class="col-12">
        <h3>Year</h3>
        <div class="p-inputgroup">
            <InputText placeholder="Year" v-model="year"/>
        </div>
    </div>
    <Button @click="getPlant">Testess</Button>
</div>
</template>
<script setup>
import Dropdown from 'primevue/dropdown';
import axios from "axios";
import { useDtcStore } from '../../store/dtc';
import { ref, onMounted } from "vue";
const dtc = useDtcStore()
const plant = ref([]);
const plantSelected = ref([]);
const year = ref([]);


const getPlant = async () => {
  plant.value = await dtc.setPlant()
};
onMounted(async () => {
    getPlant()
    const d = new Date();
    year.value = d.getFullYear()
})
</script>