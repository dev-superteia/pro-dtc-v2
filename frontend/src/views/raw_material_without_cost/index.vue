<template>
<div class="flex align-items-center justify-content-between">
        <div class="flex">
        <h1 class="page-title">{{$t('dtc.raw_material_without_cost')}}</h1>       
        </div>
        <div><Breadcrumb :home="home" :model="items" /></div>
    </div>
<div class="grid p-fluid">
    <div class="col-12">
        <h3>{{$t('dtc.plant')}}</h3>
        <div class="p-inputgroup">
            <Dropdown optionLabel="text" v-model="plantSelected" :options="plant" placeholder="Select a plant" @click="getPlant"/>
        </div>
    </div>
    <div class="col-12">
        <h3>{{$t('dtc.year')}}</h3>
        <div class="p-inputgroup">
            <InputText placeholder="Year" v-model="year"/>
        </div>
    </div>
    <div class="col-2 mt-3">
        <Button v-if="!progress" :label="$t('message.search')" @click="submit()" icon="pi pi-send"
                iconPos="right"></Button>
        <ProgressSpinner v-if="progress" style="width:50px;height:50px" strokeWidth="8" fill="var(--surface-ground)"
                animationDuration=".5s" aria-label="Custom ProgressSpinner" />
    </div>    
</div>
<DataTable ref="dt" :value="material" responsiveLayout="scroll" :rowsPerPageOptions="[10, 20, 50]" :filters="filters" :paginator="true" :rows="10">
    <template #header>
                <div class="flex justify-content-between flex-wrap">
                <div><span class="p-input-icon-left">
                        <i class="pi pi-search" />
                        <InputText v-model="filters['global'].value" placeholder="Search..."
                            style="max-width: 200px;" />
                    </span>
                </div>
                <div class="flex justify-content-between flex-wrap align-items-center gap-2">
                    <div style="text-align: left; width: 200px;">
                        <Button icon="pi pi-external-link" label="Export" @click="exportCSV($event)" />
                    </div>
                </div>
            </div>
            </template>
    <Column field="component" header="Material" :sortable="true"></Column>
    <Column field="plant" :header="$t('dtc.plant')" :sortable="true"></Column>
    <Column field="year" :header="$t('dtc.year')" :sortable="true"></Column>
</DataTable>
<Toast />
</template>
<script setup>
import Dropdown from 'primevue/dropdown';
import Column from "primevue/column";
import axios from "axios";
import { useDtcStore } from '../../store/dtc';
import { ref, onMounted } from "vue";
import { FilterMatchMode } from 'primevue/api';
import ProgressSpinner from 'primevue/progressspinner';
import Toast from 'primevue/toast';
import { useToast } from "primevue/usetoast";
import { useI18n } from 'vue-i18n'
const { t } = useI18n({})
const dt = ref();
const filters = ref({
    'global': { value: null, matchMode: FilterMatchMode.CONTAINS },
});
const exportCSV = () => {
    dt.value.exportCSV();
};

const dtc = useDtcStore()
const plant = ref([]);
const plantSelected = ref([]);
const year = ref([]);
const material = ref([]);
const progress = ref(false)
const toast = useToast();
const home = ref({
            icon: 'pi pi-home',
            to: '/',
        });
const items = ref([
    {label: 'DTC'},
    {label: t('dtc.raw_material_without_cost')},
    ]);
const getPlant = async () => {
  plant.value = await dtc.setPlant()
};

const submit = async () => {
    progress.value = true
    if (plantSelected.value.value === undefined) {
        plantSelected.value.value = ''
    }
    const response = await axios.get('http://localhost:8000/api/v1/report_raw_material_null?plant=' + plantSelected.value.value + '&year=' + year.value )
    material.value = response.data
    toast.add({severity:'success', summary: 'Atualizado conforme solicitado', detail:'Permissoes atualizadas para a regra', life: 3000});
    progress.value = false
}

onMounted(async () => {
    getPlant()
    const d = new Date();
    year.value = d.getFullYear()
})

</script>