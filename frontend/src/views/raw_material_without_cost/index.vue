<template>
<h3>Raw Material Without Cost</h3>
<div class="grid p-fluid">
    <div class="col-12">
        <h3>{{$t('dtc.plant')}}</h3>
        <div class="p-inputgroup">
            <Dropdown optionLabel="text" v-model="plantSelected" :options="plant" placeholder="Select a plant" @click="getPlant"/>
        </div>
    </div>
    <div class="col-12">
        <h3>Year</h3>
        <div class="p-inputgroup">
            <InputText placeholder="Year" v-model="year"/>
        </div>
    </div>
    <div class="col-2 mt-3">
        <Button label="Enviar" @click="getResult" icon="pi pi-send" iconPos="right" ></Button>
    </div>    
</div>
<DataTable :value="material" responsiveLayout="scroll">
    <Column field="component" header="Material"></Column>
    <Column field="plant" header="Plant"></Column>
    <Column field="year" header="Year"></Column>
</DataTable>
</template>
<script setup>
import Dropdown from 'primevue/dropdown';
import Column from "primevue/column";
import axios from "axios";
import { useDtcStore } from '../../store/dtc';
import { ref, onMounted } from "vue";
const dtc = useDtcStore()
const plant = ref([]);
const plantSelected = ref([]);
const year = ref([]);
const material = ref([]);

const getPlant = async () => {
  plant.value = await dtc.setPlant()
};

const getResult = async () => {
    const response = await axios.get('http://localhost:8000/api/v1/report_raw_material_null/report_raw_material_null?plant=' + plantSelected.value.value + '&year=' + year.value )
    material.value = response.data
}

onMounted(async () => {
    getPlant()
    const d = new Date();
    year.value = d.getFullYear()
})

</script>