<template>
    <DataTable ref="dt" :value='props.tableValue.total' responsiveLayout="scroll">
        <Column>
            <template #body="slotProps">
                <tr>
                    <td>Total</td>
                </tr>
            </template>
        </Column>
        <Column field="value" :header="$t('dtc.values')" style="min-width:200px">
            <template #body="slotProps">
                <tr>
                    <td>Weight</td>
                </tr>
                <tr>
                    <td>Weight %</td>
                </tr>
                <tr>
                    <td>Cost per Unit Std</td>
                </tr>
                <tr>
                    <td>Cost per Unit Eff</td>
                </tr>
                <tr>
                    <td>Total Cost Std</td>
                </tr>
                <tr>
                    <td>Total Cost Eff</td>
                </tr>
            </template>
        </Column>
        <Column header="Jan">
            <template #body="slotProps">
                <tr>
                    <td>{{ (slotProps.data[0].raw_weight).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[0].raw_weight / tableValue.weights[1]).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (tableValue.density).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[0].cost_standard).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[0].cost_effective).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[0].total_cost_standard).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[0].total_cost_effective).toFixed(fixed.value) }}</td>
                </tr>
            </template>
        </Column>
        <Column header="Fev">
            <template #body="slotProps">
                <tr>
                    <td>{{ (slotProps.data[1].raw_weight).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[1].raw_weight / tableValue.weights[2]).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (tableValue.density).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[1].cost_standard).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[1].cost_effective).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[1].total_cost_standard).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[1].total_cost_effective).toFixed(fixed.value) }}</td>
                </tr>
            </template>
        </Column>
        <Column header="Mar">
            <template #body="slotProps">
                <tr>
                    <td>{{ (slotProps.data[2].raw_weight).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[2].raw_weight / tableValue.weights[3]).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (tableValue.density).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[2].cost_standard).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[2].cost_effective).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[2].total_cost_standard).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[2].total_cost_effective).toFixed(fixed.value) }}</td>
                </tr>
            </template>
        </Column>
        <Column header="Apr">
            <template #body="slotProps">
                <tr>
                    <td>{{ (slotProps.data[3].raw_weight).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[3].raw_weight / tableValue.weights[4]).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (tableValue.density).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[3].cost_standard).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[3].cost_effective).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[3].total_cost_standard).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[3].total_cost_effective).toFixed(fixed.value) }}</td>
                </tr>
            </template>
        </Column>
        <Column header="May">
            <template #body="slotProps">
                <tr>
                    <td>{{ (slotProps.data[4].raw_weight).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[4].raw_weight / tableValue.weights[5]).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (tableValue.density).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[4].cost_standard).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[4].cost_effective).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[4].total_cost_standard).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[4].total_cost_effective).toFixed(fixed.value) }}</td>
                </tr>
            </template>
        </Column>
        <Column header="Jun">
            <template #body="slotProps">
                <tr>
                    <td>{{ (slotProps.data[5].raw_weight).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[5].raw_weight / tableValue.weights[6]).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (tableValue.density).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[5].cost_standard).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[5].cost_effective).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[5].total_cost_standard).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[5].total_cost_effective).toFixed(fixed.value) }}</td>
                </tr>
            </template>
        </Column>
        <Column header="Jul">
            <template #body="slotProps">
                <tr>
                    <td>{{ (slotProps.data[6].raw_weight).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[6].raw_weight / tableValue.weights[7]).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (tableValue.density).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[6].cost_standard).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[6].cost_effective).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[6].total_cost_standard).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[6].total_cost_effective).toFixed(fixed.value) }}</td>
                </tr>
            </template>
        </Column>
        <Column header="Aug">
            <template #body="slotProps">
                <tr>
                    <td>{{ (slotProps.data[7].raw_weight).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[7].raw_weight / tableValue.weights[8]).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (tableValue.density).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[7].cost_standard).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[7].cost_effective).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[7].total_cost_standard).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[7].total_cost_effective).toFixed(fixed.value) }}</td>
                </tr>
            </template>
        </Column>
        <Column header="Sep">
            <template #body="slotProps">
                <tr>
                    <td>{{ (slotProps.data[8].raw_weight).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[8].raw_weight / tableValue.weights[9]).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (tableValue.density).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[8].cost_standard).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[8].cost_effective).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[8].total_cost_standard).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[8].total_cost_effective).toFixed(fixed.value) }}</td>
                </tr>
            </template>
        </Column>
        <Column header="Out">
            <template #body="slotProps">
                <tr>
                    <td>{{ (slotProps.data[9].raw_weight).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[9].raw_weight / tableValue.weights[10]).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (tableValue.density).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[9].cost_standard).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[9].cost_effective).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[9].total_cost_standard).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[9].total_cost_effective).toFixed(fixed.value) }}</td>
                </tr>
            </template>
        </Column>
        <Column header="Nov">
            <template #body="slotProps">
                <tr>
                    <td>{{ (slotProps.data[10].raw_weight).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[10].raw_weight / tableValue.weights[11]).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (tableValue.density).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[10].cost_standard).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[10].cost_effective).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[10].total_cost_standard).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[10].total_cost_effective).toFixed(fixed.value) }}</td>
                </tr>
            </template>
        </Column>
        <Column header="Dez">
            <template #body="slotProps">
                <tr>
                    <td>{{ (slotProps.data[11].raw_weight).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[11].raw_weight / tableValue.weights[12]).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (tableValue.density).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[11].cost_standard).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[11].cost_effective).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[11].total_cost_standard).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data[11].total_cost_effective).toFixed(fixed.value) }}</td>
                </tr>
            </template>
        </Column>
    </DataTable>

    <DataTable ref="dt" :value='props.tableValue.table' responsiveLayout="scroll" :paginator="true" :rows="10"
        :rowsPerPageOptions="[-1, 10, 20, 50]" :filters="filters">
        <template #header>
            <div class="flex justify-content-between flex-wrap">
                <div><span class="p-input-icon-left">
                        <i class="pi pi-search" />
                        <InputText v-model="filters['global'].value" placeholder="Search..."
                            style="max-width: 200px;" />
                    </span>
                </div>
                <div class="flex justify-content-between flex-wrap align-items-center gap-2">
                    <Dropdown optionLabel="text" v-model="fixed" placeholder="Precission value"
                        style="max-width: 200px; float: right;" :options="[
                            { value: 0, text: '0 - precision' },
                            { value: 1, text: '1 - precision' },
                            { value: 2, text: '2 - precision' },
                            { value: 3, text: '3 - precision' },
                            { value: 4, text: '4 - precision' },
                            { value: 5, text: '5 - precision' },
                            { value: 6, text: '6 - precision' },
                            { value: 7, text: '7 - precision' }
                        ]" @change="changeFixed"/>
                    <div style="text-align: left; width: 200px;">
                        <Button icon="pi pi-external-link" label="Export" @click="exportCSV($event)" />
                    </div>
                    {{ fixed.value }}

                </div>
            </div>
        </template>
        <Column field="rawmaterial" header="Material" :sortable="true"></Column>
        <Column field="value" :header="$t('dtc.values')" style="min-width:200px">
            <template #body="slotProps">
                <tr>
                    <td>Weight</td>
                </tr>
                <tr>
                    <td>Weight %</td>
                </tr>
                <tr>
                    <td>Cost per Unit Std</td>
                </tr>
                <tr>
                    <td>Cost per Unit Eff</td>
                </tr>
                <tr>
                    <td>Total Cost Std</td>
                </tr>
                <tr>
                    <td>Total Cost Eff</td>
                </tr>
            </template>
        </Column>
        <Column field="months" :header="$t('dtc.values')">
            <template #body="slotProps">
                <tr>
                    <td>{{ (slotProps.data.months[1].raw_weight !== "--" ? (slotProps.data.months[1].raw_weight).toFixed(fixed) : "--") }}</td>
                    <!-- <td>{{ (slotProps.data.months[1].raw_weight).toFixed(fixed) }}</td> -->
                </tr>
                <tr>
                    <td>{{ (slotProps.data.months[1].raw_weight / tableValue.weights[0]).toFixed(fixed.value) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data.months[1].cost_standard !== '--' ? (slotProps.data.months[1].cost_standard).toFixed(fixed.value) : 0) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data.months[1].cost_effective !== '--' ? (slotProps.data.months[1].cost_effective).toFixed(fixed.value) : 0) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data.months[1].total_cost_standard !== '--' ? (slotProps.data.months[1].total_cost_standard).toFixed(fixed.value) : 0) }}</td>
                </tr>
                <tr>
                    <td>{{ (slotProps.data.months[1].total_cost_effective !== '--' ? (slotProps.data.months[1].total_cost_effective).toFixed(fixed.value) : 0) }}</td>
                </tr>
            </template>
        </Column>
        <Column field="months" header="Jan" style="min-width:200px">
            <template #body="slotProps">
                <TableRaw
                    :value="{ std: slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight  : 0, eff: slotProps.data.months[2].raw_weight && slotProps.data.months[2].raw_weight != '--' ? (slotProps.data.months[2].raw_weight).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ 
                        std: (slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight : 0) / (tableValue.weights[0]  || tableValue.weights[0] != '--' ? tableValue.weights[0] : 0), 
                        eff: ((slotProps.data.months[2].raw_weight || slotProps.data.months[2].raw_weight != '--' ? slotProps.data.months[2].raw_weight : 0) / (tableValue.weights[1] || tableValue.weights[1]  != '--' ? tableValue.weights[1] : 0)).toFixed(fixed.value)
                        }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_standard || slotProps.data.months[1].cost_standard != '--' ? slotProps.data.months[1].cost_standard  : 0, eff: slotProps.data.months[2].cost_standard && slotProps.data.months[2].cost_standard != '--' ? (slotProps.data.months[2].cost_standard).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_effective || slotProps.data.months[1].cost_effective != '--' ? slotProps.data.months[1].cost_effective  : 0, eff: slotProps.data.months[2].cost_effective && slotProps.data.months[2].cost_effective != '--' ? (slotProps.data.months[2].cost_effective).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_standard || slotProps.data.months[1].total_cost_standard != '--' ? slotProps.data.months[1].total_cost_standard  : 0, eff: slotProps.data.months[2].total_cost_standard && slotProps.data.months[2].total_cost_standard != '--' ? (slotProps.data.months[2].total_cost_standard).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_effective || slotProps.data.months[1].total_cost_effective != '--' ? slotProps.data.months[1].total_cost_effective  : 0, eff: slotProps.data.months[2].total_cost_effective && slotProps.data.months[2].total_cost_effective != '--' ? (slotProps.data.months[2].total_cost_effective).toFixed(fixed.value) : 0 }">
                </TableRaw>
            </template>
        </Column>
        <Column field="months" header="Feb" style="min-width:200px">
            <template #body="slotProps">
                <TableRaw
                    :value="{ std: slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight  : 0, eff: slotProps.data.months[3].raw_weight && slotProps.data.months[3].raw_weight != '--' ? (slotProps.data.months[3].raw_weight).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ 
                        std: (slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight : 0) / (tableValue.weights[0]  || tableValue.weights[0] != '--' ? tableValue.weights[0] : 0), 
                        eff: ((slotProps.data.months[3].raw_weight || slotProps.data.months[3].raw_weight != '--' ? slotProps.data.months[3].raw_weight : 0) / (tableValue.weights[2] || tableValue.weights[2]  != '--' ? tableValue.weights[2] : 0)).toFixed(fixed.value)
                        }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_standard || slotProps.data.months[1].cost_standard != '--' ? slotProps.data.months[1].cost_standard  : 0, eff: slotProps.data.months[3].cost_standard && slotProps.data.months[3].cost_standard != '--' ? (slotProps.data.months[3].cost_standard).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_effective || slotProps.data.months[1].cost_effective != '--' ? slotProps.data.months[1].cost_effective  : 0, eff: slotProps.data.months[3].cost_effective && slotProps.data.months[3].cost_effective != '--' ? (slotProps.data.months[3].cost_effective).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_standard || slotProps.data.months[1].total_cost_standard != '--' ? slotProps.data.months[1].total_cost_standard  : 0, eff: slotProps.data.months[3].total_cost_standard && slotProps.data.months[3].total_cost_standard != '--' ? (slotProps.data.months[3].total_cost_standard).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_effective || slotProps.data.months[1].total_cost_effective != '--' ? slotProps.data.months[1].total_cost_effective  : 0, eff: slotProps.data.months[3].total_cost_effective && slotProps.data.months[3].total_cost_effective != '--' ? (slotProps.data.months[3].total_cost_effective).toFixed(fixed.value) : 0 }">
                </TableRaw>
            </template>
        </Column>
        <Column field="months" header="Mar" style="min-width:200px">
            <template #body="slotProps">
                <TableRaw
                    :value="{ std: slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight  : 0, eff: slotProps.data.months[4].raw_weight && slotProps.data.months[4].raw_weight != '--' ? (slotProps.data.months[4].raw_weight).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ 
                        std: (slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight : 0) / (tableValue.weights[0]  || tableValue.weights[0] != '--' ? tableValue.weights[0] : 0), 
                        eff: ((slotProps.data.months[4].raw_weight || slotProps.data.months[4].raw_weight != '--' ? slotProps.data.months[4].raw_weight : 0) / (tableValue.weights[3] || tableValue.weights[3]  != '--' ? tableValue.weights[3] : 0)).toFixed(fixed.value)
                        }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_standard || slotProps.data.months[1].cost_standard != '--' ? slotProps.data.months[1].cost_standard  : 0, eff: slotProps.data.months[4].cost_standard && slotProps.data.months[4].cost_standard != '--' ? (slotProps.data.months[4].cost_standard).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_effective || slotProps.data.months[1].cost_effective != '--' ? slotProps.data.months[1].cost_effective  : 0, eff: slotProps.data.months[4].cost_effective && slotProps.data.months[4].cost_effective != '--' ? (slotProps.data.months[4].cost_effective).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_standard || slotProps.data.months[1].total_cost_standard != '--' ? slotProps.data.months[1].total_cost_standard  : 0, eff: slotProps.data.months[4].total_cost_standard && slotProps.data.months[4].total_cost_standard != '--' ? (slotProps.data.months[4].total_cost_standard).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_effective || slotProps.data.months[1].total_cost_effective != '--' ? slotProps.data.months[1].total_cost_effective  : 0, eff: slotProps.data.months[4].total_cost_effective && slotProps.data.months[4].total_cost_effective != '--' ? (slotProps.data.months[4].total_cost_effective).toFixed(fixed.value) : 0 }">
                </TableRaw>
            </template>
        </Column>
        <Column field="months" header="Apr" style="min-width:200px">
            <template #body="slotProps">
                <TableRaw
                    :value="{ std: slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight  : 0, eff: slotProps.data.months[5].raw_weight && slotProps.data.months[5].raw_weight != '--' ? (slotProps.data.months[5].raw_weight).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ 
                        std: (slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight : 0) / (tableValue.weights[0]  || tableValue.weights[0] != '--' ? tableValue.weights[0] : 0), 
                        eff: ((slotProps.data.months[5].raw_weight || slotProps.data.months[5].raw_weight != '--' ? slotProps.data.months[5].raw_weight : 0) / (tableValue.weights[4] || tableValue.weights[4]  != '--' ? tableValue.weights[4] : 0)).toFixed(fixed.value)
                        }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_standard || slotProps.data.months[1].cost_standard != '--' ? slotProps.data.months[1].cost_standard  : 0, eff: slotProps.data.months[5].cost_standard && slotProps.data.months[5].cost_standard != '--' ? (slotProps.data.months[5].cost_standard).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_effective || slotProps.data.months[1].cost_effective != '--' ? slotProps.data.months[1].cost_effective  : 0, eff: slotProps.data.months[5].cost_effective && slotProps.data.months[5].cost_effective != '--' ? (slotProps.data.months[5].cost_effective).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_standard || slotProps.data.months[1].total_cost_standard != '--' ? slotProps.data.months[1].total_cost_standard  : 0, eff: slotProps.data.months[5].total_cost_standard && slotProps.data.months[5].total_cost_standard != '--' ? (slotProps.data.months[5].total_cost_standard).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_effective || slotProps.data.months[1].total_cost_effective != '--' ? slotProps.data.months[1].total_cost_effective  : 0, eff: slotProps.data.months[5].total_cost_effective && slotProps.data.months[5].total_cost_effective != '--' ? (slotProps.data.months[5].total_cost_effective).toFixed(fixed.value) : 0 }">
                </TableRaw>
            </template>
        </Column>
        <Column field="months" header="Mai" style="min-width:200px">
            <template #body="slotProps">
                <TableRaw
                    :value="{ std: slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight  : 0, eff: slotProps.data.months[6].raw_weight && slotProps.data.months[6].raw_weight != '--' ? (slotProps.data.months[6].raw_weight).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ 
                        std: (slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight : 0) / (tableValue.weights[0]  || tableValue.weights[0] != '--' ? tableValue.weights[0] : 0), 
                        eff: ((slotProps.data.months[6].raw_weight || slotProps.data.months[6].raw_weight != '--' ? slotProps.data.months[6].raw_weight : 0) / (tableValue.weights[5] || tableValue.weights[5]  != '--' ? tableValue.weights[5] : 0)).toFixed(fixed.value)
                        }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_standard || slotProps.data.months[1].cost_standard != '--' ? slotProps.data.months[1].cost_standard  : 0, eff: slotProps.data.months[6].cost_standard && slotProps.data.months[6].cost_standard != '--' ? (slotProps.data.months[6].cost_standard).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_effective || slotProps.data.months[1].cost_effective != '--' ? slotProps.data.months[1].cost_effective  : 0, eff: slotProps.data.months[6].cost_effective && slotProps.data.months[6].cost_effective != '--' ? (slotProps.data.months[6].cost_effective).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_standard || slotProps.data.months[1].total_cost_standard != '--' ? slotProps.data.months[1].total_cost_standard  : 0, eff: slotProps.data.months[6].total_cost_standard && slotProps.data.months[6].total_cost_standard != '--' ? (slotProps.data.months[6].total_cost_standard).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_effective || slotProps.data.months[1].total_cost_effective != '--' ? slotProps.data.months[1].total_cost_effective  : 0, eff: slotProps.data.months[6].total_cost_effective && slotProps.data.months[6].total_cost_effective != '--' ? (slotProps.data.months[6].total_cost_effective).toFixed(fixed.value) : 0 }">
                </TableRaw>
            </template>
        </Column>
        <Column field="months" header="Jun" style="min-width:200px">
            <template #body="slotProps">
                <TableRaw
                    :value="{ std: slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight  : 0, eff: slotProps.data.months[7].raw_weight && slotProps.data.months[7].raw_weight != '--' ? (slotProps.data.months[7].raw_weight).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ 
                        std: (slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight : 0) / (tableValue.weights[0]  || tableValue.weights[0] != '--' ? tableValue.weights[0] : 0), 
                        eff: ((slotProps.data.months[7].raw_weight || slotProps.data.months[7].raw_weight != '--' ? slotProps.data.months[7].raw_weight : 0) / (tableValue.weights[6] || tableValue.weights[6]  != '--' ? tableValue.weights[6] : 0)).toFixed(fixed.value)
                        }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_standard || slotProps.data.months[1].cost_standard != '--' ? slotProps.data.months[1].cost_standard  : 0, eff: slotProps.data.months[7].cost_standard && slotProps.data.months[7].cost_standard != '--' ? (slotProps.data.months[7].cost_standard).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_effective || slotProps.data.months[1].cost_effective != '--' ? slotProps.data.months[1].cost_effective  : 0, eff: slotProps.data.months[7].cost_effective && slotProps.data.months[7].cost_effective != '--' ? (slotProps.data.months[7].cost_effective).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_standard || slotProps.data.months[1].total_cost_standard != '--' ? slotProps.data.months[1].total_cost_standard  : 0, eff: slotProps.data.months[7].total_cost_standard && slotProps.data.months[7].total_cost_standard != '--' ? (slotProps.data.months[7].total_cost_standard).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_effective || slotProps.data.months[1].total_cost_effective != '--' ? slotProps.data.months[1].total_cost_effective  : 0, eff: slotProps.data.months[7].total_cost_effective && slotProps.data.months[7].total_cost_effective != '--' ? (slotProps.data.months[7].total_cost_effective).toFixed(fixed.value) : 0 }">
                </TableRaw>
            </template>
        </Column>
        <Column field="months" header="Jul" style="min-width:200px">
            <template #body="slotProps">
                <TableRaw
                    :value="{ std: slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight  : 0, eff: slotProps.data.months[8].raw_weight && slotProps.data.months[8].raw_weight != '--' ? (slotProps.data.months[8].raw_weight).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ 
                        std: (slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight : 0) / (tableValue.weights[0]  || tableValue.weights[0] != '--' ? tableValue.weights[0] : 0), 
                        eff: ((slotProps.data.months[8].raw_weight || slotProps.data.months[8].raw_weight != '--' ? slotProps.data.months[8].raw_weight : 0) / (tableValue.weights[7] || tableValue.weights[7]  != '--' ? tableValue.weights[7] : 0)).toFixed(fixed.value)
                        }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_standard || slotProps.data.months[1].cost_standard != '--' ? slotProps.data.months[1].cost_standard  : 0, eff: slotProps.data.months[8].cost_standard && slotProps.data.months[8].cost_standard != '--' ? (slotProps.data.months[8].cost_standard).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_effective || slotProps.data.months[1].cost_effective != '--' ? slotProps.data.months[1].cost_effective  : 0, eff: slotProps.data.months[8].cost_effective && slotProps.data.months[8].cost_effective != '--' ? (slotProps.data.months[8].cost_effective).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_standard || slotProps.data.months[1].total_cost_standard != '--' ? slotProps.data.months[1].total_cost_standard  : 0, eff: slotProps.data.months[8].total_cost_standard && slotProps.data.months[8].total_cost_standard != '--' ? (slotProps.data.months[8].total_cost_standard).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_effective || slotProps.data.months[1].total_cost_effective != '--' ? slotProps.data.months[1].total_cost_effective  : 0, eff: slotProps.data.months[8].total_cost_effective && slotProps.data.months[8].total_cost_effective != '--' ? (slotProps.data.months[8].total_cost_effective).toFixed(fixed.value) : 0 }">
                </TableRaw>
            </template>
        </Column>
        <Column field="months" header="Aug" style="min-width:200px">
            <template #body="slotProps">
                <TableRaw
                    :value="{ std: slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight  : 0, eff: slotProps.data.months[9].raw_weight && slotProps.data.months[9].raw_weight != '--' ? (slotProps.data.months[9].raw_weight).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ 
                        std: (slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight : 0) / (tableValue.weights[0]  || tableValue.weights[0] != '--' ? tableValue.weights[0] : 0), 
                        eff: ((slotProps.data.months[9].raw_weight || slotProps.data.months[9].raw_weight != '--' ? slotProps.data.months[9].raw_weight : 0) / (tableValue.weights[8] || tableValue.weights[8]  != '--' ? tableValue.weights[8] : 0)).toFixed(fixed.value)
                        }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_standard || slotProps.data.months[1].cost_standard != '--' ? slotProps.data.months[1].cost_standard  : 0, eff: slotProps.data.months[9].cost_standard && slotProps.data.months[9].cost_standard != '--' ? (slotProps.data.months[9].cost_standard).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_effective || slotProps.data.months[1].cost_effective != '--' ? slotProps.data.months[1].cost_effective  : 0, eff: slotProps.data.months[9].cost_effective && slotProps.data.months[9].cost_effective != '--' ? (slotProps.data.months[9].cost_effective).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_standard || slotProps.data.months[1].total_cost_standard != '--' ? slotProps.data.months[1].total_cost_standard  : 0, eff: slotProps.data.months[9].total_cost_standard && slotProps.data.months[9].total_cost_standard != '--' ? (slotProps.data.months[9].total_cost_standard).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_effective || slotProps.data.months[1].total_cost_effective != '--' ? slotProps.data.months[1].total_cost_effective  : 0, eff: slotProps.data.months[9].total_cost_effective && slotProps.data.months[9].total_cost_effective != '--' ? (slotProps.data.months[9].total_cost_effective).toFixed(fixed.value) : 0 }">
                </TableRaw>
            </template>
        </Column>
        <Column field="months" header="Sep" style="min-width:200px">
            <template #body="slotProps">
                <TableRaw
                    :value="{ std: slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight  : 0, eff: slotProps.data.months[10].raw_weight && slotProps.data.months[10].raw_weight != '--' ? (slotProps.data.months[10].raw_weight).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ 
                        std: (slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight : 0) / (tableValue.weights[0]  || tableValue.weights[0] != '--' ? tableValue.weights[0] : 0), 
                        eff: ((slotProps.data.months[10].raw_weight || slotProps.data.months[10].raw_weight != '--' ? slotProps.data.months[10].raw_weight : 0) / (tableValue.weights[9] || tableValue.weights[9]  != '--' ? tableValue.weights[9] : 0)).toFixed(fixed.value)
                        }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_standard || slotProps.data.months[1].cost_standard != '--' ? slotProps.data.months[1].cost_standard  : 0, eff: slotProps.data.months[10].cost_standard && slotProps.data.months[10].cost_standard != '--' ? (slotProps.data.months[10].cost_standard).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_effective || slotProps.data.months[1].cost_effective != '--' ? slotProps.data.months[1].cost_effective  : 0, eff: slotProps.data.months[10].cost_effective && slotProps.data.months[10].cost_effective != '--' ? (slotProps.data.months[10].cost_effective).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_standard || slotProps.data.months[1].total_cost_standard != '--' ? slotProps.data.months[1].total_cost_standard  : 0, eff: slotProps.data.months[10].total_cost_standard && slotProps.data.months[10].total_cost_standard != '--' ? (slotProps.data.months[10].total_cost_standard).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_effective || slotProps.data.months[1].total_cost_effective != '--' ? slotProps.data.months[1].total_cost_effective  : 0, eff: slotProps.data.months[10].total_cost_effective && slotProps.data.months[10].total_cost_effective != '--' ? (slotProps.data.months[10].total_cost_effective).toFixed(fixed.value) : 0 }">
                </TableRaw>
            </template>
        </Column>
        <Column field="months" header="Oct" style="min-width:200px">
            <template #body="slotProps">
                <TableRaw
                    :value="{ std: slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight  : 0, eff: slotProps.data.months[11].raw_weight && slotProps.data.months[11].raw_weight != '--' ? (slotProps.data.months[11].raw_weight).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ 
                        std: (slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight : 0) / (tableValue.weights[0]  || tableValue.weights[0] != '--' ? tableValue.weights[0] : 0), 
                        eff: ((slotProps.data.months[11].raw_weight || slotProps.data.months[11].raw_weight != '--' ? slotProps.data.months[11].raw_weight : 0) / (tableValue.weights[10] || tableValue.weights[10]  != '--' ? tableValue.weights[10] : 0)).toFixed(fixed.value)
                        }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_standard || slotProps.data.months[1].cost_standard != '--' ? slotProps.data.months[1].cost_standard  : 0, eff: slotProps.data.months[11].cost_standard && slotProps.data.months[11].cost_standard != '--' ? (slotProps.data.months[11].cost_standard).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_effective || slotProps.data.months[1].cost_effective != '--' ? slotProps.data.months[1].cost_effective  : 0, eff: slotProps.data.months[11].cost_effective && slotProps.data.months[11].cost_effective != '--' ? (slotProps.data.months[11].cost_effective).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_standard || slotProps.data.months[1].total_cost_standard != '--' ? slotProps.data.months[1].total_cost_standard  : 0, eff: slotProps.data.months[11].total_cost_standard && slotProps.data.months[11].total_cost_standard != '--' ? (slotProps.data.months[11].total_cost_standard).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_effective || slotProps.data.months[1].total_cost_effective != '--' ? slotProps.data.months[1].total_cost_effective  : 0, eff: slotProps.data.months[11].total_cost_effective && slotProps.data.months[11].total_cost_effective != '--' ? (slotProps.data.months[11].total_cost_effective).toFixed(fixed.value) : 0 }">
                </TableRaw>
            </template>
        </Column>
        <Column field="months" header="Nov" style="min-width:200px">
            <template #body="slotProps">
                <TableRaw
                    :value="{ std: slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight  : 0, eff: slotProps.data.months[12].raw_weight && slotProps.data.months[12].raw_weight != '--' ? (slotProps.data.months[12].raw_weight).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ 
                        std: (slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight : 0) / (tableValue.weights[0]  || tableValue.weights[0] != '--' ? tableValue.weights[0] : 0), 
                        eff: ((slotProps.data.months[12].raw_weight || slotProps.data.months[12].raw_weight != '--' ? slotProps.data.months[12].raw_weight : 0) / (tableValue.weights[11] || tableValue.weights[11]  != '--' ? tableValue.weights[11] : 0)).toFixed(fixed.value)
                        }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_standard || slotProps.data.months[1].cost_standard != '--' ? slotProps.data.months[1].cost_standard  : 0, eff: slotProps.data.months[12].cost_standard && slotProps.data.months[12].cost_standard != '--' ? (slotProps.data.months[12].cost_standard).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_effective || slotProps.data.months[1].cost_effective != '--' ? slotProps.data.months[1].cost_effective  : 0, eff: slotProps.data.months[12].cost_effective && slotProps.data.months[12].cost_effective != '--' ? (slotProps.data.months[12].cost_effective).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_standard || slotProps.data.months[1].total_cost_standard != '--' ? slotProps.data.months[1].total_cost_standard  : 0, eff: slotProps.data.months[12].total_cost_standard && slotProps.data.months[12].total_cost_standard != '--' ? (slotProps.data.months[12].total_cost_standard).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_effective || slotProps.data.months[1].total_cost_effective != '--' ? slotProps.data.months[1].total_cost_effective  : 0, eff: slotProps.data.months[12].total_cost_effective && slotProps.data.months[12].total_cost_effective != '--' ? (slotProps.data.months[12].total_cost_effective).toFixed(fixed.value) : 0 }">
                </TableRaw>
            </template>
        </Column>
        <Column field="months" header="Dec" style="min-width:200px">
            <template #body="slotProps">
                <TableRaw
                    :value="{ std: slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight  : 0, eff: slotProps.data.months[13].raw_weight && slotProps.data.months[13].raw_weight != '--' ? (slotProps.data.months[13].raw_weight).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ 
                        std: (slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight : 0) / (tableValue.weights[0]  || tableValue.weights[0] != '--' ? tableValue.weights[0] : 0), 
                        eff: ((slotProps.data.months[13].raw_weight || slotProps.data.months[13].raw_weight != '--' ? slotProps.data.months[13].raw_weight : 0) / (tableValue.weights[12] || tableValue.weights[12]  != '--' ? tableValue.weights[12] : 0)).toFixed(fixed.value)
                        }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_standard || slotProps.data.months[1].cost_standard != '--' ? slotProps.data.months[1].cost_standard  : 0, eff: slotProps.data.months[13].cost_standard && slotProps.data.months[13].cost_standard != '--' ? (slotProps.data.months[13].cost_standard).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_effective || slotProps.data.months[1].cost_effective != '--' ? slotProps.data.months[1].cost_effective  : 0, eff: slotProps.data.months[13].cost_effective && slotProps.data.months[13].cost_effective != '--' ? (slotProps.data.months[13].cost_effective).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_standard || slotProps.data.months[1].total_cost_standard != '--' ? slotProps.data.months[1].total_cost_standard  : 0, eff: slotProps.data.months[13].total_cost_standard && slotProps.data.months[13].total_cost_standard != '--' ? (slotProps.data.months[13].total_cost_standard).toFixed(fixed.value) : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_effective || slotProps.data.months[1].total_cost_effective != '--' ? slotProps.data.months[1].total_cost_effective  : 0, eff: slotProps.data.months[13].total_cost_effective && slotProps.data.months[13].total_cost_effective != '--' ? (slotProps.data.months[13].total_cost_effective).toFixed(fixed.value) : 0 }">
                </TableRaw>
            </template>
        </Column>
    </DataTable>
</template>
<script setup>
import { ref, onMounted, computed } from "vue";
import Column from "primevue/column";
import { useConfigStore } from '@/store/config';
import { FilterMatchMode } from 'primevue/api';
import Dropdown from 'primevue/dropdown';
import TableRaw from '@/layout/components/arrow-table/index.vue'
const config = useConfigStore()
const props = defineProps(['tableValue'])
const changeFixed = () => {
    config.setFixed(props)
}
const dt = ref();
const table = ref([]);
const fixed = ref({ value: 3, text: '3 - precision' });
const filters = ref({
    'global': { value: null, matchMode: FilterMatchMode.CONTAINS },
});

const exportCSV = () => {
    dt.value.exportCSV();
};  

</script>