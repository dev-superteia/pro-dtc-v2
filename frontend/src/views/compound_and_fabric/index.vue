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
        <Button v-if="!progress" :label="$t('message.search')" @click="getComponents()" icon="pi pi-send" iconPos="right" ></Button>
        <ProgressSpinner v-if="progress" style="width:50px;height:50px" strokeWidth="8" fill="var(--surface-ground)"
                animationDuration=".5s" aria-label="Custom ProgressSpinner" />
    </div>
    <div class="col-12">
        <TableCuston :tableValue=table></TableCuston>
    </div>    
</div>
<Toast />
</template>
<script setup>
import Dropdown from 'primevue/dropdown';
import axios from "axios";
import { useDtcStore } from '../../store/dtc';
import { ref, onMounted } from "vue";
import { useToast } from "primevue/usetoast";
import TableCuston from './table/mass.vue'
import ProgressSpinner from 'primevue/progressspinner';
import Toast from 'primevue/toast';
const dtc = useDtcStore()
const plant = ref([]);
const toast = useToast();
const material = ref([]);
const plantSelected = ref([]);
const materialSelected = ref([]);
const year = ref([]);
const progress = ref(false)
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
    progress.value = true
    const response = await axios.get('http://localhost:8000/api/v1/compound_and_fabric?plant=' +plantSelected.value.value + '&material=' + materialSelected.value.value + '&year=' + year.value + '&type=' + selectMaterialBreakdown.value.id)
    console.log(response.data)
    table.value = response.data
    toast.add({severity:'success', summary: 'Atualizado conforme solicitado', detail:'Permissoes atualizadas para a regra', life: 3000});
    progress.value = false
};

onMounted(async () => {
    getPlant()
    getMassAll()
    const d = new Date()
    year.value = d.getFullYear()
})
</script>