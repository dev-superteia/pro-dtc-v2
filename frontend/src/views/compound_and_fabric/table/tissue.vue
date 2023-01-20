<template>
    <DataTable ref="dt" :value='props.tableValue' responsiveLayout="scroll" :paginator="true" :rows="10"
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
        <Column field="material" header="Material" sortable="true"></Column>
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
    </DataTable>
</template>
<script setup>
import { ref } from "vue";
import Column from "primevue/column";
import { useConfigStore } from '@/store/config';
import { FilterMatchMode } from 'primevue/api';
import Dropdown from 'primevue/dropdown';
const config = useConfigStore()
const props = defineProps({
    tableValue: Array
})
const changeFixed = () => {
    config.setFixed(4)
}
const dt = ref();
const fixed = ref();
const filters = ref({
    'global': { value: null, matchMode: FilterMatchMode.CONTAINS },
});

const exportCSV = () => {
    dt.value.exportCSV();
};       
</script>