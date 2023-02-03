<template>
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
        <Column field="value" :header="$t('dtc.values')" style="min-width:150px">
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
                    <td>{{ (slotProps.data.months[1].raw_weight).toFixed(fixed) }}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.months[1].raw_weight / tableValue.weights[0] }}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.months[1].cost_standard }}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.months[1].cost_effective }}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.months[1].total_cost_standard }}</td>
                </tr>
                <tr>
                    <td>{{ slotProps.data.months[1].total_cost_effective }}</td>
                </tr>
            </template>
        </Column>
        <Column field="months" header="Jan">
            <template #body="slotProps">
                <TableRaw
                    :value="{ std: slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight  : 0, eff: slotProps.data.months[2].raw_weight && slotProps.data.months[2].raw_weight != '--' ? slotProps.data.months[2].raw_weight : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ 
                        std: (slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight : 0) / (tableValue.weights[0]  || tableValue.weights[0] != '--' ? tableValue.weights[0] : 0), 
                        eff: (slotProps.data.months[2].raw_weight || slotProps.data.months[2].raw_weight != '--' ? slotProps.data.months[2].raw_weight : 0) / (tableValue.weights[1] || tableValue.weights[1]  != '--' ? tableValue.weights[1] : 0)
                        }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_standard || slotProps.data.months[1].cost_standard != '--' ? slotProps.data.months[1].cost_standard  : 0, eff: slotProps.data.months[2].cost_standard && slotProps.data.months[2].cost_standard != '--' ? slotProps.data.months[2].cost_standard : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_effective || slotProps.data.months[1].cost_effective != '--' ? slotProps.data.months[1].cost_effective  : 0, eff: slotProps.data.months[2].cost_effective && slotProps.data.months[2].cost_effective != '--' ? slotProps.data.months[2].cost_effective : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_standard || slotProps.data.months[1].total_cost_standard != '--' ? slotProps.data.months[1].total_cost_standard  : 0, eff: slotProps.data.months[2].total_cost_standard && slotProps.data.months[2].total_cost_standard != '--' ? slotProps.data.months[2].total_cost_standard : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_effective || slotProps.data.months[1].total_cost_effective != '--' ? slotProps.data.months[1].total_cost_effective  : 0, eff: slotProps.data.months[2].total_cost_effective && slotProps.data.months[2].total_cost_effective != '--' ? slotProps.data.months[2].total_cost_effective : 0 }">
                </TableRaw>
            </template>
        </Column>
        <Column field="months" header="Feb">
            <template #body="slotProps">
                <TableRaw
                    :value="{ std: slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight  : 0, eff: slotProps.data.months[3].raw_weight && slotProps.data.months[3].raw_weight != '--' ? slotProps.data.months[3].raw_weight : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ 
                        std: (slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight : 0) / (tableValue.weights[0]  || tableValue.weights[0] != '--' ? tableValue.weights[0] : 0), 
                        eff: (slotProps.data.months[3].raw_weight || slotProps.data.months[3].raw_weight != '--' ? slotProps.data.months[3].raw_weight : 0) / (tableValue.weights[2] || tableValue.weights[2]  != '--' ? tableValue.weights[2] : 0)
                        }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_standard || slotProps.data.months[1].cost_standard != '--' ? slotProps.data.months[1].cost_standard  : 0, eff: slotProps.data.months[3].cost_standard && slotProps.data.months[3].cost_standard != '--' ? slotProps.data.months[3].cost_standard : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_effective || slotProps.data.months[1].cost_effective != '--' ? slotProps.data.months[1].cost_effective  : 0, eff: slotProps.data.months[3].cost_effective && slotProps.data.months[3].cost_effective != '--' ? slotProps.data.months[3].cost_effective : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_standard || slotProps.data.months[1].total_cost_standard != '--' ? slotProps.data.months[1].total_cost_standard  : 0, eff: slotProps.data.months[3].total_cost_standard && slotProps.data.months[3].total_cost_standard != '--' ? slotProps.data.months[3].total_cost_standard : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_effective || slotProps.data.months[1].total_cost_effective != '--' ? slotProps.data.months[1].total_cost_effective  : 0, eff: slotProps.data.months[3].total_cost_effective && slotProps.data.months[3].total_cost_effective != '--' ? slotProps.data.months[3].total_cost_effective : 0 }">
                </TableRaw>
            </template>
        </Column>
        <Column field="months" header="Mar">
            <template #body="slotProps">
                <TableRaw
                    :value="{ std: slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight  : 0, eff: slotProps.data.months[4].raw_weight && slotProps.data.months[4].raw_weight != '--' ? slotProps.data.months[4].raw_weight : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ 
                        std: (slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight : 0) / (tableValue.weights[0]  || tableValue.weights[0] != '--' ? tableValue.weights[0] : 0), 
                        eff: (slotProps.data.months[4].raw_weight || slotProps.data.months[4].raw_weight != '--' ? slotProps.data.months[4].raw_weight : 0) / (tableValue.weights[3] || tableValue.weights[3]  != '--' ? tableValue.weights[3] : 0)
                        }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_standard || slotProps.data.months[1].cost_standard != '--' ? slotProps.data.months[1].cost_standard  : 0, eff: slotProps.data.months[4].cost_standard && slotProps.data.months[4].cost_standard != '--' ? slotProps.data.months[4].cost_standard : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_effective || slotProps.data.months[1].cost_effective != '--' ? slotProps.data.months[1].cost_effective  : 0, eff: slotProps.data.months[4].cost_effective && slotProps.data.months[4].cost_effective != '--' ? slotProps.data.months[4].cost_effective : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_standard || slotProps.data.months[1].total_cost_standard != '--' ? slotProps.data.months[1].total_cost_standard  : 0, eff: slotProps.data.months[4].total_cost_standard && slotProps.data.months[4].total_cost_standard != '--' ? slotProps.data.months[4].total_cost_standard : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_effective || slotProps.data.months[1].total_cost_effective != '--' ? slotProps.data.months[1].total_cost_effective  : 0, eff: slotProps.data.months[4].total_cost_effective && slotProps.data.months[4].total_cost_effective != '--' ? slotProps.data.months[4].total_cost_effective : 0 }">
                </TableRaw>
            </template>
        </Column>
        <Column field="months" header="Apr">
            <template #body="slotProps">
                <TableRaw
                    :value="{ std: slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight  : 0, eff: slotProps.data.months[5].raw_weight && slotProps.data.months[5].raw_weight != '--' ? slotProps.data.months[5].raw_weight : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ 
                        std: (slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight : 0) / (tableValue.weights[0]  || tableValue.weights[0] != '--' ? tableValue.weights[0] : 0), 
                        eff: (slotProps.data.months[5].raw_weight || slotProps.data.months[5].raw_weight != '--' ? slotProps.data.months[5].raw_weight : 0) / (tableValue.weights[4] || tableValue.weights[4]  != '--' ? tableValue.weights[4] : 0)
                        }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_standard || slotProps.data.months[1].cost_standard != '--' ? slotProps.data.months[1].cost_standard  : 0, eff: slotProps.data.months[5].cost_standard && slotProps.data.months[5].cost_standard != '--' ? slotProps.data.months[5].cost_standard : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_effective || slotProps.data.months[1].cost_effective != '--' ? slotProps.data.months[1].cost_effective  : 0, eff: slotProps.data.months[5].cost_effective && slotProps.data.months[5].cost_effective != '--' ? slotProps.data.months[5].cost_effective : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_standard || slotProps.data.months[1].total_cost_standard != '--' ? slotProps.data.months[1].total_cost_standard  : 0, eff: slotProps.data.months[5].total_cost_standard && slotProps.data.months[5].total_cost_standard != '--' ? slotProps.data.months[5].total_cost_standard : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_effective || slotProps.data.months[1].total_cost_effective != '--' ? slotProps.data.months[1].total_cost_effective  : 0, eff: slotProps.data.months[5].total_cost_effective && slotProps.data.months[5].total_cost_effective != '--' ? slotProps.data.months[5].total_cost_effective : 0 }">
                </TableRaw>
            </template>
        </Column>
        <Column field="months" header="Mai">
            <template #body="slotProps">
                <TableRaw
                    :value="{ std: slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight  : 0, eff: slotProps.data.months[6].raw_weight && slotProps.data.months[6].raw_weight != '--' ? slotProps.data.months[6].raw_weight : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ 
                        std: (slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight : 0) / (tableValue.weights[0]  || tableValue.weights[0] != '--' ? tableValue.weights[0] : 0), 
                        eff: (slotProps.data.months[6].raw_weight || slotProps.data.months[6].raw_weight != '--' ? slotProps.data.months[6].raw_weight : 0) / (tableValue.weights[5] || tableValue.weights[5]  != '--' ? tableValue.weights[5] : 0)
                        }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_standard || slotProps.data.months[1].cost_standard != '--' ? slotProps.data.months[1].cost_standard  : 0, eff: slotProps.data.months[6].cost_standard && slotProps.data.months[6].cost_standard != '--' ? slotProps.data.months[6].cost_standard : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_effective || slotProps.data.months[1].cost_effective != '--' ? slotProps.data.months[1].cost_effective  : 0, eff: slotProps.data.months[6].cost_effective && slotProps.data.months[6].cost_effective != '--' ? slotProps.data.months[6].cost_effective : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_standard || slotProps.data.months[1].total_cost_standard != '--' ? slotProps.data.months[1].total_cost_standard  : 0, eff: slotProps.data.months[6].total_cost_standard && slotProps.data.months[6].total_cost_standard != '--' ? slotProps.data.months[6].total_cost_standard : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_effective || slotProps.data.months[1].total_cost_effective != '--' ? slotProps.data.months[1].total_cost_effective  : 0, eff: slotProps.data.months[6].total_cost_effective && slotProps.data.months[6].total_cost_effective != '--' ? slotProps.data.months[6].total_cost_effective : 0 }">
                </TableRaw>
            </template>
        </Column>
        <Column field="months" header="Jun">
            <template #body="slotProps">
                <TableRaw
                    :value="{ std: slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight  : 0, eff: slotProps.data.months[7].raw_weight && slotProps.data.months[7].raw_weight != '--' ? slotProps.data.months[7].raw_weight : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ 
                        std: (slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight : 0) / (tableValue.weights[0]  || tableValue.weights[0] != '--' ? tableValue.weights[0] : 0), 
                        eff: (slotProps.data.months[7].raw_weight || slotProps.data.months[7].raw_weight != '--' ? slotProps.data.months[7].raw_weight : 0) / (tableValue.weights[6] || tableValue.weights[6]  != '--' ? tableValue.weights[6] : 0)
                        }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_standard || slotProps.data.months[1].cost_standard != '--' ? slotProps.data.months[1].cost_standard  : 0, eff: slotProps.data.months[7].cost_standard && slotProps.data.months[7].cost_standard != '--' ? slotProps.data.months[7].cost_standard : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_effective || slotProps.data.months[1].cost_effective != '--' ? slotProps.data.months[1].cost_effective  : 0, eff: slotProps.data.months[7].cost_effective && slotProps.data.months[7].cost_effective != '--' ? slotProps.data.months[7].cost_effective : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_standard || slotProps.data.months[1].total_cost_standard != '--' ? slotProps.data.months[1].total_cost_standard  : 0, eff: slotProps.data.months[7].total_cost_standard && slotProps.data.months[7].total_cost_standard != '--' ? slotProps.data.months[7].total_cost_standard : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_effective || slotProps.data.months[1].total_cost_effective != '--' ? slotProps.data.months[1].total_cost_effective  : 0, eff: slotProps.data.months[7].total_cost_effective && slotProps.data.months[7].total_cost_effective != '--' ? slotProps.data.months[7].total_cost_effective : 0 }">
                </TableRaw>
            </template>
        </Column>
        <Column field="months" header="Jul">
            <template #body="slotProps">
                <TableRaw
                    :value="{ std: slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight  : 0, eff: slotProps.data.months[8].raw_weight && slotProps.data.months[8].raw_weight != '--' ? slotProps.data.months[8].raw_weight : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ 
                        std: (slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight : 0) / (tableValue.weights[0]  || tableValue.weights[0] != '--' ? tableValue.weights[0] : 0), 
                        eff: (slotProps.data.months[8].raw_weight || slotProps.data.months[8].raw_weight != '--' ? slotProps.data.months[8].raw_weight : 0) / (tableValue.weights[7] || tableValue.weights[7]  != '--' ? tableValue.weights[7] : 0)
                        }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_standard || slotProps.data.months[1].cost_standard != '--' ? slotProps.data.months[1].cost_standard  : 0, eff: slotProps.data.months[8].cost_standard && slotProps.data.months[8].cost_standard != '--' ? slotProps.data.months[8].cost_standard : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_effective || slotProps.data.months[1].cost_effective != '--' ? slotProps.data.months[1].cost_effective  : 0, eff: slotProps.data.months[8].cost_effective && slotProps.data.months[8].cost_effective != '--' ? slotProps.data.months[8].cost_effective : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_standard || slotProps.data.months[1].total_cost_standard != '--' ? slotProps.data.months[1].total_cost_standard  : 0, eff: slotProps.data.months[8].total_cost_standard && slotProps.data.months[8].total_cost_standard != '--' ? slotProps.data.months[8].total_cost_standard : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_effective || slotProps.data.months[1].total_cost_effective != '--' ? slotProps.data.months[1].total_cost_effective  : 0, eff: slotProps.data.months[8].total_cost_effective && slotProps.data.months[8].total_cost_effective != '--' ? slotProps.data.months[8].total_cost_effective : 0 }">
                </TableRaw>
            </template>
        </Column>
        <Column field="months" header="Aug">
            <template #body="slotProps">
                <TableRaw
                    :value="{ std: slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight  : 0, eff: slotProps.data.months[9].raw_weight && slotProps.data.months[9].raw_weight != '--' ? slotProps.data.months[9].raw_weight : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ 
                        std: (slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight : 0) / (tableValue.weights[0]  || tableValue.weights[0] != '--' ? tableValue.weights[0] : 0), 
                        eff: (slotProps.data.months[9].raw_weight || slotProps.data.months[9].raw_weight != '--' ? slotProps.data.months[9].raw_weight : 0) / (tableValue.weights[8] || tableValue.weights[8]  != '--' ? tableValue.weights[8] : 0)
                        }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_standard || slotProps.data.months[1].cost_standard != '--' ? slotProps.data.months[1].cost_standard  : 0, eff: slotProps.data.months[9].cost_standard && slotProps.data.months[9].cost_standard != '--' ? slotProps.data.months[9].cost_standard : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_effective || slotProps.data.months[1].cost_effective != '--' ? slotProps.data.months[1].cost_effective  : 0, eff: slotProps.data.months[9].cost_effective && slotProps.data.months[9].cost_effective != '--' ? slotProps.data.months[9].cost_effective : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_standard || slotProps.data.months[1].total_cost_standard != '--' ? slotProps.data.months[1].total_cost_standard  : 0, eff: slotProps.data.months[9].total_cost_standard && slotProps.data.months[9].total_cost_standard != '--' ? slotProps.data.months[9].total_cost_standard : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_effective || slotProps.data.months[1].total_cost_effective != '--' ? slotProps.data.months[1].total_cost_effective  : 0, eff: slotProps.data.months[9].total_cost_effective && slotProps.data.months[9].total_cost_effective != '--' ? slotProps.data.months[9].total_cost_effective : 0 }">
                </TableRaw>
            </template>
        </Column>
        <Column field="months" header="Sep">
            <template #body="slotProps">
                <TableRaw
                    :value="{ std: slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight  : 0, eff: slotProps.data.months[10].raw_weight && slotProps.data.months[10].raw_weight != '--' ? slotProps.data.months[10].raw_weight : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ 
                        std: (slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight : 0) / (tableValue.weights[0]  || tableValue.weights[0] != '--' ? tableValue.weights[0] : 0), 
                        eff: (slotProps.data.months[10].raw_weight || slotProps.data.months[10].raw_weight != '--' ? slotProps.data.months[10].raw_weight : 0) / (tableValue.weights[9] || tableValue.weights[9]  != '--' ? tableValue.weights[9] : 0)
                        }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_standard || slotProps.data.months[1].cost_standard != '--' ? slotProps.data.months[1].cost_standard  : 0, eff: slotProps.data.months[10].cost_standard && slotProps.data.months[10].cost_standard != '--' ? slotProps.data.months[10].cost_standard : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_effective || slotProps.data.months[1].cost_effective != '--' ? slotProps.data.months[1].cost_effective  : 0, eff: slotProps.data.months[10].cost_effective && slotProps.data.months[10].cost_effective != '--' ? slotProps.data.months[10].cost_effective : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_standard || slotProps.data.months[1].total_cost_standard != '--' ? slotProps.data.months[1].total_cost_standard  : 0, eff: slotProps.data.months[10].total_cost_standard && slotProps.data.months[10].total_cost_standard != '--' ? slotProps.data.months[10].total_cost_standard : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_effective || slotProps.data.months[1].total_cost_effective != '--' ? slotProps.data.months[1].total_cost_effective  : 0, eff: slotProps.data.months[10].total_cost_effective && slotProps.data.months[10].total_cost_effective != '--' ? slotProps.data.months[10].total_cost_effective : 0 }">
                </TableRaw>
            </template>
        </Column>
        <Column field="months" header="Oct">
            <template #body="slotProps">
                <TableRaw
                    :value="{ std: slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight  : 0, eff: slotProps.data.months[11].raw_weight && slotProps.data.months[11].raw_weight != '--' ? slotProps.data.months[11].raw_weight : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ 
                        std: (slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight : 0) / (tableValue.weights[0]  || tableValue.weights[0] != '--' ? tableValue.weights[0] : 0), 
                        eff: (slotProps.data.months[11].raw_weight || slotProps.data.months[11].raw_weight != '--' ? slotProps.data.months[11].raw_weight : 0) / (tableValue.weights[10] || tableValue.weights[10]  != '--' ? tableValue.weights[10] : 0)
                        }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_standard || slotProps.data.months[1].cost_standard != '--' ? slotProps.data.months[1].cost_standard  : 0, eff: slotProps.data.months[11].cost_standard && slotProps.data.months[11].cost_standard != '--' ? slotProps.data.months[11].cost_standard : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_effective || slotProps.data.months[1].cost_effective != '--' ? slotProps.data.months[1].cost_effective  : 0, eff: slotProps.data.months[11].cost_effective && slotProps.data.months[11].cost_effective != '--' ? slotProps.data.months[11].cost_effective : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_standard || slotProps.data.months[1].total_cost_standard != '--' ? slotProps.data.months[1].total_cost_standard  : 0, eff: slotProps.data.months[11].total_cost_standard && slotProps.data.months[11].total_cost_standard != '--' ? slotProps.data.months[11].total_cost_standard : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_effective || slotProps.data.months[1].total_cost_effective != '--' ? slotProps.data.months[1].total_cost_effective  : 0, eff: slotProps.data.months[11].total_cost_effective && slotProps.data.months[11].total_cost_effective != '--' ? slotProps.data.months[11].total_cost_effective : 0 }">
                </TableRaw>
            </template>
        </Column>
        <Column field="months" header="Nov">
            <template #body="slotProps">
                <TableRaw
                    :value="{ std: slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight  : 0, eff: slotProps.data.months[12].raw_weight && slotProps.data.months[12].raw_weight != '--' ? slotProps.data.months[12].raw_weight : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ 
                        std: (slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight : 0) / (tableValue.weights[0]  || tableValue.weights[0] != '--' ? tableValue.weights[0] : 0), 
                        eff: (slotProps.data.months[12].raw_weight || slotProps.data.months[12].raw_weight != '--' ? slotProps.data.months[12].raw_weight : 0) / (tableValue.weights[11] || tableValue.weights[11]  != '--' ? tableValue.weights[11] : 0)
                        }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_standard || slotProps.data.months[1].cost_standard != '--' ? slotProps.data.months[1].cost_standard  : 0, eff: slotProps.data.months[12].cost_standard && slotProps.data.months[12].cost_standard != '--' ? slotProps.data.months[12].cost_standard : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_effective || slotProps.data.months[1].cost_effective != '--' ? slotProps.data.months[1].cost_effective  : 0, eff: slotProps.data.months[12].cost_effective && slotProps.data.months[12].cost_effective != '--' ? slotProps.data.months[12].cost_effective : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_standard || slotProps.data.months[1].total_cost_standard != '--' ? slotProps.data.months[1].total_cost_standard  : 0, eff: slotProps.data.months[12].total_cost_standard && slotProps.data.months[12].total_cost_standard != '--' ? slotProps.data.months[12].total_cost_standard : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_effective || slotProps.data.months[1].total_cost_effective != '--' ? slotProps.data.months[1].total_cost_effective  : 0, eff: slotProps.data.months[12].total_cost_effective && slotProps.data.months[12].total_cost_effective != '--' ? slotProps.data.months[12].total_cost_effective : 0 }">
                </TableRaw>
            </template>
        </Column>
        <Column field="months" header="Dec">
            <template #body="slotProps">
                <TableRaw
                    :value="{ std: slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight  : 0, eff: slotProps.data.months[13].raw_weight && slotProps.data.months[13].raw_weight != '--' ? slotProps.data.months[13].raw_weight : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ 
                        std: (slotProps.data.months[1].raw_weight || slotProps.data.months[1].raw_weight != '--' ? slotProps.data.months[1].raw_weight : 0) / (tableValue.weights[0]  || tableValue.weights[0] != '--' ? tableValue.weights[0] : 0), 
                        eff: (slotProps.data.months[13].raw_weight || slotProps.data.months[13].raw_weight != '--' ? slotProps.data.months[13].raw_weight : 0) / (tableValue.weights[12] || tableValue.weights[12]  != '--' ? tableValue.weights[12] : 0)
                        }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_standard || slotProps.data.months[1].cost_standard != '--' ? slotProps.data.months[1].cost_standard  : 0, eff: slotProps.data.months[13].cost_standard && slotProps.data.months[13].cost_standard != '--' ? slotProps.data.months[13].cost_standard : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].cost_effective || slotProps.data.months[1].cost_effective != '--' ? slotProps.data.months[1].cost_effective  : 0, eff: slotProps.data.months[13].cost_effective && slotProps.data.months[13].cost_effective != '--' ? slotProps.data.months[13].cost_effective : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_standard || slotProps.data.months[1].total_cost_standard != '--' ? slotProps.data.months[1].total_cost_standard  : 0, eff: slotProps.data.months[13].total_cost_standard && slotProps.data.months[13].total_cost_standard != '--' ? slotProps.data.months[13].total_cost_standard : 0 }">
                </TableRaw>
                <TableRaw
                    :value="{ std: slotProps.data.months[1].total_cost_effective || slotProps.data.months[1].total_cost_effective != '--' ? slotProps.data.months[1].total_cost_effective  : 0, eff: slotProps.data.months[13].total_cost_effective && slotProps.data.months[13].total_cost_effective != '--' ? slotProps.data.months[13].total_cost_effective : 0 }">
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