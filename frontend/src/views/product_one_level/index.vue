<template>
<h3>Product One-Level</h3>
<div class="grid p-fluid">
    <div class="col-12">
        <h3>{{$t('dtc.plant')}}</h3>
        <div class="p-inputgroup">
            <Dropdown optionLabel="text" v-model="plantSelected" :options="plant" placeholder="Select a plant"/>
        </div>
    </div>
    <div class="col-12">
        <h3>{{$t('dtc.line')}}</h3>
        <div class="p-inputgroup">
            <Dropdown optionLabel="text" placeholder="Select a line" v-model="lineSelected" :options="line"/>
        </div>
    </div>
    <div class="col-12">
        <h3>{{$t('dtc.mkg')}}</h3>
        <div class="p-inputgroup">
            <Dropdown optionLabel="text" placeholder="Market Segment" v-model="mkgSelected" :options="mkg"/>
        </div>
    </div>
    <div class="col-12">
        <h3>{{$t('dtc.product')}}</h3>
        <div class="p-inputgroup">
            <Dropdown editable optionLabel="text" placeholder="Product" v-model="tireSelected" :options="tire"/>
        </div>
    </div>
    <div class="col-12">
        <h3>{{$t('dtc.year')}}</h3>
        <div class="p-inputgroup">
            <InputText placeholder="Year" v-model="year"/>
        </div>
    </div>
    <div class="col-2 mt-3">
        <Button v-if="!progress" :label="$t('message.search')" @click="submit()" icon="pi pi-send" iconPos="right" ></Button>
        <ProgressSpinner v-if="progress" style="width:50px;height:50px" strokeWidth="8" fill="var(--surface-ground)"
                animationDuration=".5s" aria-label="Custom ProgressSpinner" />
    </div>
    <div class="col-12">
        <DataTable ref="dt" :value="table" responsiveLayout="scroll" :rowsPerPageOptions="[10, 20, 50]" :filters="filters" :paginator="true" :rows="10">
            <template #header>
                <div class="flex justify-content-between flex-wrap">
                <div><span class="p-input-icon-left">
                        <i class="pi pi-search" />
                        <InputText v-model="filters['global'].value" placeholder="Search..."
                            style="max-width: 200px;" />
                    </span>
                </div>
                <div class="flex justify-content-between flex-wrap align-items-center gap-2">
                    <Dropdown optionLabel="text" v-model="fixed" placeholder="Precission value" style="max-width: 200px; float: right;"
                        :options="[
                            { value: 0, text: '0 - precision' },
                            { value: 1, text: '1 - precision' },
                            { value: 2, text: '2 - precision' },
                            { value: 3, text: '3 - precision' },
                            { value: 4, text: '4 - precision' },
                            { value: 5, text: '5 - precision' },
                            { value: 6, text: '6 - precision' },
                            { value: 7, text: '7 - precision' }
                        ]" />
                    <div style="text-align: left; width: 200px;">
                        <Button icon="pi pi-external-link" label="Export" @click="exportCSV($event)" />
                    </div>
                </div>
            </div>
            </template>
            <Column :header="$t('dtc.values')">
                <template #body="slotProps">
                    <tr>
                        <td>Amount Used</td>
                    </tr>
                    <tr>
                        <td>Cost Std</td>
                    </tr>
                    <tr>
                        <td>Cost Eff</td>
                    </tr>
                    <tr>
                        <td>DTC</td>
                    </tr>
                </template>
            </Column>            
        </DataTable>
    </div>
    <Toast />
</div>
</template>
<script setup>
import Dropdown from 'primevue/dropdown';
import Column from "primevue/column";
import ProgressSpinner from 'primevue/progressspinner';
import axios from "axios";
import Toast from 'primevue/toast';
import { useToast } from "primevue/usetoast";
import { useDtcStore } from '../../store/dtc';
import { FilterMatchMode } from 'primevue/api';
import { ref, onMounted } from "vue";

const dt = ref();
const dtc = useDtcStore()
const plant = ref([]);
const mkg = ref([]);
const line = ref([]);
const tire = ref([]);
const tireSelected = ref([]);
const plantSelected = ref([]);
const mkgSelected = ref([]);
const lineSelected = ref([]);
const year = ref([]);
const table = ref([]);
const fixed = ref();
const progress = ref(false)
const toast = useToast();

const exportCSV = () => {
    dt.value.exportCSV();
};   
const filters = ref({
    'global': { value: null, matchMode: FilterMatchMode.CONTAINS },
});
const getPlant = async () => {
  plant.value = await dtc.setPlant()
};
const getMkg = async () => {
    await dtc.setMkg()
    mkg.value = dtc.mkg
    line.value = dtc.line
};
const getLine = async () => {
    await dtc.setLine()
    line.value = dtc.line
};
const getTire = async () => {
    await dtc.setTires()
    tire.value = dtc.tires
};

const a = ref([]);

const submit = async () => {
    progress.value = true
    if (plantSelected.value.value === undefined) {
        plantSelected.value.value = ''
    }
    const response = await axios.get('http://localhost:8000/api/v1/product_one_level/?plant='+plantSelected.value.value + '&product=' +tireSelected.value.value + '&market_segment=' + mkgSelected.value.value + '&year=' + year.value + '&line=' + lineSelected)
    response.data.items
    const entries = Object.entries(response.data.items);
    console.log(entries);
    table.value = entries
    toast.add({severity:'success', summary: 'Atualizado conforme solicitado', detail:'Permissoes atualizadas para a regra', life: 3000});
    progress.value = false
};
onMounted(async () => {
    getPlant()
    getMkg()
    getLine()
    getTire()
    const d = new Date()
    year.value = d.getFullYear()
})
</script>