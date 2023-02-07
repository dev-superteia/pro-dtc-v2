<template>
    <div class="flex align-items-center justify-content-between">
        <div class="flex">
        <h1 class="page-title">{{$t('dtc.tissue_month')}}</h1>       
        </div>
        <div><Breadcrumb :home="home" :model="items" /></div>
    </div>
    <div class="grid p-fluid">
        <div class="col-12">
            <h3>{{$t('dtc.plant')}}</h3>
            <div class="p-inputgroup">
                <Dropdown optionLabel="text" v-model="plantSelected" :options="plant" :placeholder="$t('dtc.plant')"
                    @click="getPlant" />
            </div>
        </div>
        <div class="col-12">
            <h3>{{$t('dtc.year')}}</h3>
            <div class="p-inputgroup">
                <InputText :placeholder="$t('dtc.year')" v-model="year" />
            </div>
        </div>
        <div class="col-2 mt-3">
            <Button v-if="!progress" :label="$t('message.search')" @click="submit()" icon="pi pi-send"
                iconPos="right"></Button>
            <ProgressSpinner v-if="progress" style="width:50px;height:50px" strokeWidth="8" fill="var(--surface-ground)"
                animationDuration=".5s" aria-label="Custom ProgressSpinner" />
        </div>
        <div class="col-12">
    <DataTable ref="dt" :value='table' responsiveLayout="scroll" :paginator="true" :rows="10"
        :rowsPerPageOptions="[-1,10, 20, 50]" :filters="filters">
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
        <Column field="material" header="Material" :sortable="true"></Column>
        <Column field="mat_desc" :header="$t('dtc.description')"></Column>
        <Column field="plant" :header="$t('dtc.plant')" :sortable="true"></Column>
        <Column field="comp" :header="$t('dtc.mass')" :sortable="true"></Column>
        <Column field="raw" :header="$t('dtc.raw_material')" :sortable="true"></Column>
        <Column field="value" :header="$t('dtc.values')" style="min-width: 150px">
            <template #body="slotProps">
                <tr>
                    <td>STD</td>
                </tr>
                <tr>
                    <td>{{$t('dtc.raw_material')}}</td>
                </tr>
                <tr>
                    <td>{{$t('dtc.mass')}}</td>
                </tr>
            </template>
        </Column>
        <Column field="value" header="PDG">
            <template #body="slotProps">
                <tr>
                    <td>{{
                        slotProps.data.array_agg[0][3] != '-' ? parseFloat(slotProps.data.array_agg[0][3] +
                            slotProps.data.array_agg[0][4]).toFixed(fixed.value) : '-'
                    }}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[0][1] != '-' ? slotProps.data.array_agg[0][1].toFixed(fixed.value) : '-' }}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[0][2] != '-' ? slotProps.data.array_agg[0][2].toFixed(fixed.value) : '-' }}</td>
                </tr>
            </template>
        </Column>
        <Column field="value" header="JAN">
            <template #body="slotProps">
                <tr>
                    <td>{{
                        slotProps.data.array_agg[1][5] != '-' ? parseFloat(slotProps.data.array_agg[1][5] + slotProps.data.array_agg[1][6]).toFixed(fixed.value) : '-'
                    }}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[1][1] != '-' ? slotProps.data.array_agg[1][1].toFixed(fixed.value) : '-' }}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[1][2] != '-' ? slotProps.data.array_agg[1][2].toFixed(fixed.value) : '-' }}</td>
                </tr>
            </template>
        </Column>
        <Column field="value" header="FEB">
            <template #body="slotProps">
                <tr>
                    <td>{{
                        slotProps.data.array_agg[2][5] != '-' ? parseFloat(slotProps.data.array_agg[2][5] + slotProps.data.array_agg[2][6]).toFixed(fixed.value) : '-'
                    }}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[2][1] != '-' ? slotProps.data.array_agg[2][1].toFixed(fixed.value) : '-' }}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[2][2] != '-' ? slotProps.data.array_agg[2][2].toFixed(fixed.value) : '-' }}</td>
                </tr>
            </template>
        </Column>
        <Column field="value" header="MAR">
            <template #body="slotProps">
                <tr>
                    <td>{{
                        slotProps.data.array_agg[3][5] != '-' ? parseFloat(slotProps.data.array_agg[3][5] + slotProps.data.array_agg[3][6]).toFixed(fixed.value) : '-'
                    }}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[3][1] != '-' ? slotProps.data.array_agg[3][1].toFixed(fixed.value) : '-' }}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[3][2]  != '-' ? slotProps.data.array_agg[3][2].toFixed(fixed.value) : '-' }}</td>
                </tr>
            </template>
        </Column>
        <Column field="value" header="APR">
            <template #body="slotProps">
                <tr>
                    <td>{{
                        slotProps.data.array_agg[4][5] != '-' ? parseFloat(slotProps.data.array_agg[4][5] + slotProps.data.array_agg[4][6]).toFixed(fixed.value) : '-'
                    }}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[4][1] != '-' ? slotProps.data.array_agg[4][1].toFixed(fixed.value) : '-' }}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[4][2] != '-' ? slotProps.data.array_agg[4][2].toFixed(fixed.value) : '-' }}</td>
                </tr>
            </template>
        </Column>
        <Column field="value" header="MAI">
            <template #body="slotProps">
                <tr>
                    <td>{{
                        slotProps.data.array_agg[5][5] != '-' ? parseFloat(slotProps.data.array_agg[5][5] + slotProps.data.array_agg[5][6]).toFixed(fixed.value) : '-'
                    }}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[5][1] != '-' ? slotProps.data.array_agg[5][1].toFixed(fixed.value) : '-'}}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[5][2] != '-' ? slotProps.data.array_agg[5][2].toFixed(fixed.value) : '-'}}</td>
                </tr>
            </template>
        </Column>
        <Column field="value" header="JUN">
            <template #body="slotProps">
                <tr>
                    <td>{{
                        slotProps.data.array_agg[6][5] != '-' ? parseFloat(slotProps.data.array_agg[6][5] + slotProps.data.array_agg[6][6]).toFixed(fixed.value) : '-'
                    }}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[6][1] != '-' ? slotProps.data.array_agg[6][1].toFixed(fixed.value) : '-' }}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[6][2] != '-' ? slotProps.data.array_agg[6][2].toFixed(fixed.value) : '-'}}</td>
                </tr>
            </template>
        </Column>
        <Column field="value" header="JUL">
            <template #body="slotProps">
                <tr>
                    <td>{{
                        slotProps.data.array_agg[7][5] != '-' ? parseFloat(slotProps.data.array_agg[7][5] + slotProps.data.array_agg[7][6]).toFixed(fixed.value) : '-'
                    }}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[7][1] != '-' ? slotProps.data.array_agg[7][1].toFixed(fixed.value) : '-'}}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[7][2] != '-' ? slotProps.data.array_agg[7][2].toFixed(fixed.value) : '-'}}</td>
                </tr>
            </template>
        </Column>
        <Column field="value" header="AUG">
            <template #body="slotProps">
                <tr>
                    <td>{{
                        slotProps.data.array_agg[8][5] != '-' ? parseFloat(slotProps.data.array_agg[8][5] + slotProps.data.array_agg[8][6]).toFixed(fixed.value) : '-'
                    }}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[8][1] != '-' ? slotProps.data.array_agg[8][1].toFixed(fixed.value) : '-'}}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[8][2] != '-' ? slotProps.data.array_agg[8][2].toFixed(fixed.value) : '-'}}</td>
                </tr>
            </template>
        </Column>
        <Column field="value" header="SEP">
            <template #body="slotProps">
                <tr>
                    <td>{{
                        slotProps.data.array_agg[9][5]  != '-' ? parseFloat(slotProps.data.array_agg[9][5] + slotProps.data.array_agg[9][6]).toFixed(fixed.value) : '-'
                    }}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[9][1] != '-' ? slotProps.data.array_agg[9][1].toFixed(fixed.value) : '-'}}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[9][2] != '-' ? slotProps.data.array_agg[9][2].toFixed(fixed.value) : '-'}}</td>
                </tr>
            </template>
        </Column>
        <Column field="value" header="OCT">
            <template #body="slotProps">
                <tr>
                    <td>{{
                        slotProps.data.array_agg[10][5] != '-' ? parseFloat(slotProps.data.array_agg[10][5] + slotProps.data.array_agg[10][6]).toFixed(fixed.value) : '-'
                    }}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[10][1] != '-' ? slotProps.data.array_agg[10][1].toFixed(fixed.value) : '-'}}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[10][2] != '-' ? slotProps.data.array_agg[10][2].toFixed(fixed.value) : '-'}}</td>
                </tr>
            </template>
        </Column>
        <Column field="value" header="NOV">
            <template #body="slotProps">
                <tr>
                    <td>{{
                        slotProps.data.array_agg[11][5] != '-' ? parseFloat(slotProps.data.array_agg[11][5] + slotProps.data.array_agg[11][6]).toFixed(fixed.value) : '-'
                    }}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[11][1] != '-' ? slotProps.data.array_agg[11][1].toFixed(fixed.value) : '-'}}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[11][2] != '-' ? slotProps.data.array_agg[11][2].toFixed(fixed.value) : '-'}}</td>
                </tr>
            </template>
        </Column>
        <Column field="value" header="DEC">
            <template #body="slotProps">
                <tr>
                    <td>{{
                        slotProps.data.array_agg[12][5] != '-' ? parseFloat(slotProps.data.array_agg[12][5] + slotProps.data.array_agg[12][6]).toFixed(fixed.value) : '-'
                    }}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[12][1] != '-' ? slotProps.data.array_agg[12][1].toFixed(fixed.value) : '-'}}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.array_agg[12][2] != '-' ? slotProps.data.array_agg[12][2].toFixed(fixed.value) : '-'}}</td>
                </tr>
            </template>
        </Column>
    </DataTable>
        </div>
    </div>
    <Toast />
</template>
<script setup>
import Column from "primevue/column";
import { FilterMatchMode } from 'primevue/api';
import Dropdown from 'primevue/dropdown';
import ProgressSpinner from 'primevue/progressspinner';
import { useDtcStore } from '../../store/dtc';
import { ref, onMounted } from "vue";
import Toast from 'primevue/toast';
import { useToast } from "primevue/usetoast";
import { useI18n } from 'vue-i18n'
const { t } = useI18n({})
const dtc = useDtcStore()
const plant = ref([]);
const plantSelected = ref([]);
const year = ref([]);
const table = ref([]);
const progress = ref(false)
const toast = useToast();
const dt = ref();
const fixed = ref({ value: 3, text: '3 - precision' });
const filters = ref({
    'global': { value: null, matchMode: FilterMatchMode.CONTAINS },
});
const home = ref({
            icon: 'pi pi-home',
            to: '/',
        });
const items = ref([
    {label: 'DTC'},
    {label: t('dtc.tissue_month')},
    ]);
const exportCSV = () => {
    dt.value.exportCSV();
};    
const getPlant = async () => {
    plant.value = await dtc.setPlant()
};
onMounted(async () => {
    getPlant()
    const d = new Date()
    year.value = d.getFullYear()
})
const submit = async () => {
    progress.value = true
    table.value = await dtc.setTissue(plantSelected.value, year.value)
    toast.add({severity:'success', summary: 'Atualizado conforme solicitado', detail:'Permissoes atualizadas para a regra', life: 3000}); 
    progress.value = false
}
</script>