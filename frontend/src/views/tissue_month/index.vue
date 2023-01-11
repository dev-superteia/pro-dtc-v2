<template>
<h3>Tissue Month</h3>
<div class="grid p-fluid">
    <div class="col-12">
        <h3>{{$t('dtc.plant')}}</h3>
        <div class="p-inputgroup">
            <Dropdown optionLabel="text" v-model="plantSelected" :options="plant" :placeholder="$t('dtc.plant')"  @click="getPlant"/>
        </div>
    </div>
    <div class="col-12">
        <h3>{{$t('dtc.year')}}</h3>
        <div class="p-inputgroup">
            <InputText :placeholder="$t('dtc.year')" v-model="year"/>
        </div>
    </div>
    <div class="col-2 mt-3">
        <Button v-if="!progress" :label="$t('message.search')" @click="submit()" icon="pi pi-send" iconPos="right" ></Button>
        <ProgressSpinner v-if="progress" style="width:50px;height:50px" strokeWidth="8" fill="var(--surface-ground)" animationDuration=".5s" aria-label="Custom ProgressSpinner" />
    </div>


    <div>
        <DataTable :value="table" responsiveLayout="scroll">
            <Column field="material" header="Code"></Column>
        </DataTable>
    </div>

    
</div>
</template>
<script setup>
import Dropdown from 'primevue/dropdown';
import Column from "primevue/column";
import ProgressSpinner from 'primevue/progressspinner';
import axios from "axios";
import { useDtcStore } from '../../store/dtc';
import { ref, onMounted } from "vue";
const dtc = useDtcStore()
const plant = ref([]);
const plantSelected = ref([]);
const year = ref([]);
const table = ref([])
const progress = ref(false)
const getPlant = async () => {
  plant.value = await dtc.setPlant()
};
onMounted(async () => {
    getPlant()
    const d = new Date()
    year.value = d.getFullYear()
})
const submit = async () =>{
    progress.value = !progress.value 
    const response = await axios.get("http://localhost:8000/api/v1/multselect/raw");    
    console.log(response)          
    table = response.data
    progress.value = !progress.value 
}
</script>