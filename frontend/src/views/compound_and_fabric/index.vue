<template>
<h3>Compound and Fabric</h3>
<div class="grid p-fluid">
    <div class="col-12">
        <h3>{{$t('dtc.plant')}}</h3>
        <div class="p-inputgroup">
            <Dropdown optionLabel="text" v-model="plantSelected" :options="plant" placeholder="Select a plant"  @click="getPlant"/>
        </div>
    </div>
    <div class="col-12">
        <h3>{{$t('dtc.material')}}</h3>
        <div class="p-inputgroup">
            <Dropdown editable optionLabel="text" placeholder="Select a Material" v-model="materialSelected" :options="material" @click="getMaterial"/>
        </div>
    </div>
    <div class="col-12">
        <h3>{{$t('dtc.year')}}</h3>
        <div class="p-inputgroup">
            <InputText placeholder="Year" v-model="year"/>
        </div>
    </div>
    <div class="col-12">
        <h3>{{$t('dtc.type')}}</h3>
        <div class="p-inputgroup">
            <Dropdown optionLabel="text" placeholder="Select a Type" v-model="selectMaterialBreakdown" :options="itemsMaterialBreakdown" selectOnFocus="true"/>
        </div>
    </div>
    <div class="col-2 mt-3">
        <Button :label="$t('message.search')" @click="getComponents" icon="pi pi-send" iconPos="right" ></Button>
    </div>
    <div class="col-12">
        <TableCuston :tableValue=table></TableCuston>
    </div>    
</div>

</template>
<script setup>
import Dropdown from 'primevue/dropdown';
import axios from "axios";
import { useDtcStore } from '../../store/dtc';
import { ref, onMounted } from "vue";
import TableCuston from './table/mass.vue'
const dtc = useDtcStore()
const plant = ref([]);
const material = ref([]);
const plantSelected = ref([]);
const materialSelected = ref([]);
const year = ref([]);
const selectMaterialBreakdown= ref({ id: 1, text: 'Without Recycle' })
const itemsMaterialBreakdown = ref([{ id: 1, text: 'Without Recycle' }, { id: 2, text: 'With Recycle (no explosion)' }, { id: 3, text: 'With Recycle (explosion)' }])
const table = ref([]);

const getPlant = async () => {
  plant.value = await dtc.setPlant()
  
};
const getMassAll = async () => {
    await dtc.setMassAll()
    material.value = dtc.mass_all 
};
const getComponents = async () => {
    const response = await axios.get('http://localhost:8000/api/v1/compound_and_fabric?plant=' +plantSelected.value.value + '&material=' + materialSelected.value.value + '&year=' + year.value + '&type=' + selectMaterialBreakdown.value.id)
    console.log(response.data)
    table.value = response.data

};

onMounted(async () => {
    getPlant()
    getMassAll()
    const d = new Date()
    year.value = d.getFullYear()
})
</script>