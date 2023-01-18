<template>   
<DataTable :value='props.tableValue' responsiveLayout="scroll" :paginator="true" :rows="10" :rowsPerPageOptions="[10,20,50]" >
    <template #header>
        <div class="grid">
            <div class="col-12 md:col-6"><span class="p-input-icon-left">
                            <i class="pi pi-search"/>
                            <InputText  style="max-width: 200px;"/>
                        </span></div>       
            <div class="col-12 md:col-6"><Dropdown optionLabel="text" placeholder="Precission value" style="max-width: 200px; float: right;"/></div>       
                </div>
    </template>
    <Column field="material" header="Material" sortable="true"></Column>
    <Column field="mat_desc" :header="$t('dtc.description')"></Column>
    <Column field="plant" :header="$t('dtc.plant')" sortable="true"></Column>
    <Column field="comp" :header="$t('dtc.mass')" sortable="true"></Column>
    <Column field="raw" :header="$t('dtc.raw_material')" sortable="true"></Column>
    <Column field="value" :header="$t('dtc.values')">
                    <template #body="slotProps">
                        <tr>
                            <td>STD</td>
                        </tr>
                        <tr>
                            <td>KG</td>
                        </tr>
                        <tr>
                            <td>MT</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="PDG">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[0][3] != '-' ? parseFloat(slotProps.data.array_agg[0][3] + slotProps.data.array_agg[0][4]).toFixed(2) : '-'}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[0][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[0][2]}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="JAN">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[1][5] + slotProps.data.array_agg[1][6]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[1][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[1][2]}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="FEB">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[2][5] + slotProps.data.array_agg[2][6]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[2][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[2][2]}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="MAR">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[3][5] + slotProps.data.array_agg[3][6]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[3][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[3][2]}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="APR">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[4][5] + slotProps.data.array_agg[4][6]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[4][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[4][2]}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="MAI">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[5][5] + slotProps.data.array_agg[5][6]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[5][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[5][2]}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="JUN">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[6][5] + slotProps.data.array_agg[6][6]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[6][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[6][2]}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="JUL">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[7][5] + slotProps.data.array_agg[7][6]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[7][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[7][2]}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="AUG">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[8][5] + slotProps.data.array_agg[8][6]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[8][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[8][2]}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="SEP">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[9][5] + slotProps.data.array_agg[9][6]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[9][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[9][2]}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="OCT">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[10][5] + slotProps.data.array_agg[10][6]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[10][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[10][2]}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="NOV">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[11][5] + slotProps.data.array_agg[11][6]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[11][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[11][2]}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="DEC">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[12][5] + slotProps.data.array_agg[12][6]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[12][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[12][2]}}</td>
                        </tr>
                    </template>
                </Column>
</DataTable>
</template>
<script setup>
import Column from "primevue/column";
import { useConfigStore } from '@/store/config';
import Dropdown from 'primevue/dropdown';
const config = useConfigStore()
const props = defineProps({
  tableValue: Array
})
const changeFixed = () => {
    config.setFixed(4)
}
</script>