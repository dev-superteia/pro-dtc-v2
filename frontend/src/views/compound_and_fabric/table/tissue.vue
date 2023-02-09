<template>
    <DataTable :value='props.tableValue' responsiveLayout="scroll">
        <template #header>
            <div class="flex justify-content-between flex-wrap">
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
                        ]" @change="changeFixed"/>
                    <div style="text-align: left; width: 200px;">
                        <Button icon="pi pi-external-link" label="Export" @click="exportCSV($event)" />
                    </div>
                </div>
            </div>
        </template>
        <div class="mb-2 flex">
            <InputSwitch v-model="showDetails" />
            <h4 style="margin: 0 10px">Show Details</h4>
        </div>
        <Column field="items" header="Value" style="min-width:200px">
            <template #body="slotProps">
                <tr>
                    <td>Compound Name</td>
                </tr>
                <tr>
                    <td>Compound Weight</td>
                </tr>
                <tr v-if="showDetails">
                    <td>Total Raw Materials</td>
                </tr>
                <tr v-if="showDetails">
                    <td>Total Cost std</td>
                </tr>
                <tr v-if="showDetails">
                    <td>Total Cost eff</td>
                </tr>
                <tr>
                    <td>Coupound Cost std</td>
                </tr>
                <tr>
                    <td>Coupound Cost eff</td>
                </tr>
                <tr>
                    <td>Fabric Name</td>
                </tr>
                <tr>
                    <td>Fabric Weight</td>
                </tr>
                <tr v-if="showDetails">
                    <td>Mp Cost Std</td>
                </tr>
                <tr v-if="showDetails">
                    <td>Mp Cost Eff</td>
                </tr>
                <tr>
                    <td>Fabric Cost std</td>
                </tr>
                <tr>
                    <td>Fabric Cost eff</td>
                </tr>
                <tr>
                    <td>Total Weight</td>
                </tr>
                <tr>
                    <td>Total Cost std</td>
                </tr>
                <tr>
                    <td>Total Cost eff</td>
                </tr>
            </template>
        </Column>
        <Column header="STD">
            <template #body="slotProps">
                <tr>
                    <td @click="showContent(slotProps.data[0].card.compound_name, 0, 0)">
                        {{ (slotProps.data[0].card.compound_name ? (slotProps.data[0].card.compound_name) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[0].card.compound_weight ? (slotProps.data[0].card.compound_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[0].card.me_total_raw_materials ? (slotProps.data[0].card.me_total_raw_materials).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[0].card.me_total_cost_std ? (slotProps.data[0].card.me_total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[0].card.me_total_cost_eff ? (slotProps.data[0].card.me_total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[0].card.coupound_cost_std ? (slotProps.data[0].card.coupound_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[0].card.coupound_cost_eff ? (slotProps.data[0].card.coupound_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[0].card.fabric_name ? (slotProps.data[0].card.fabric_name).slice(0, -2) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[0].card.fabric_weight ? (slotProps.data[0].card.fabric_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[0].card.mat_mp_cost_std ? (slotProps.data[0].card.mat_mp_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[0].card.mat_mp_cost_eff ? (slotProps.data[0].card.mat_mp_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[0].card.fabric_cost_std ? (slotProps.data[0].card.fabric_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[0].card.fabric_cost_eff ? (slotProps.data[0].card.fabric_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[0].card.total_weight ? (slotProps.data[0].card.total_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[0].card.total_cost_std ? (slotProps.data[0].card.total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[0].card.total_cost_eff ? (slotProps.data[0].card.total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
            </template>
        </Column>
        <Column header="Jan">
            <template #body="slotProps">
                <tr>
                    <td @click="showContent(slotProps.data[1].card.compound_name, 1, 0)">
                        {{ (slotProps.data[1].card.compound_name ? (slotProps.data[1].card.compound_name) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[1].card.compound_weight ? (slotProps.data[1].card.compound_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[1].card.me_total_raw_materials ? (slotProps.data[1].card.me_total_raw_materials).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[1].card.me_total_cost_std ? (slotProps.data[1].card.me_total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[1].card.me_total_cost_eff ? (slotProps.data[1].card.me_total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[1].card.coupound_cost_std ? (slotProps.data[1].card.coupound_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[1].card.coupound_cost_eff ? (slotProps.data[1].card.coupound_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[1].card.fabric_name ? (slotProps.data[1].card.fabric_name).slice(0, -2) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[1].card.fabric_weight ? (slotProps.data[1].card.fabric_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[1].card.mat_mp_cost_std ? (slotProps.data[1].card.mat_mp_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[1].card.mat_mp_cost_eff ? (slotProps.data[1].card.mat_mp_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[1].card.fabric_cost_std ? (slotProps.data[1].card.fabric_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[1].card.fabric_cost_eff ? (slotProps.data[1].card.fabric_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[1].card.total_weight ? (slotProps.data[1].card.total_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[1].card.total_cost_std ? (slotProps.data[1].card.total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[1].card.total_cost_eff ? (slotProps.data[1].card.total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
            </template>
        </Column>
        <Column header="Feb">
            <template #body="slotProps">
                <tr>
                    <td @click="showContent(slotProps.data[2].card.compound_name, 2, 0)">
                        {{ (slotProps.data[2].card.compound_name ? (slotProps.data[2].card.compound_name) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[2].card.compound_weight ? (slotProps.data[2].card.compound_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[2].card.me_total_raw_materials ? (slotProps.data[2].card.me_total_raw_materials).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[2].card.me_total_cost_std ? (slotProps.data[2].card.me_total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[2].card.me_total_cost_eff ? (slotProps.data[2].card.me_total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[2].card.coupound_cost_std ? (slotProps.data[2].card.coupound_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[2].card.coupound_cost_eff ? (slotProps.data[2].card.coupound_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[2].card.fabric_name ? (slotProps.data[2].card.fabric_name).slice(0, -2) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[2].card.fabric_weight ? (slotProps.data[2].card.fabric_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[2].card.mat_mp_cost_std ? (slotProps.data[2].card.mat_mp_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[2].card.mat_mp_cost_eff ? (slotProps.data[2].card.mat_mp_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[2].card.fabric_cost_std ? (slotProps.data[2].card.fabric_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[2].card.fabric_cost_eff ? (slotProps.data[2].card.fabric_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[2].card.total_weight ? (slotProps.data[2].card.total_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[2].card.total_cost_std ? (slotProps.data[2].card.total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[2].card.total_cost_eff ? (slotProps.data[2].card.total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
            </template>
        </Column>
        <Column header="Mar">
            <template #body="slotProps">
                <tr>
                    <td @click="showContent(slotProps.data[3].card.compound_name, 3, 0)">
                        {{ (slotProps.data[3].card.compound_name ? (slotProps.data[3].card.compound_name) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[3].card.compound_weight ? (slotProps.data[3].card.compound_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[3].card.me_total_raw_materials ? (slotProps.data[3].card.me_total_raw_materials).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[3].card.me_total_cost_std ? (slotProps.data[3].card.me_total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[3].card.me_total_cost_eff ? (slotProps.data[3].card.me_total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[3].card.coupound_cost_std ? (slotProps.data[3].card.coupound_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[3].card.coupound_cost_eff ? (slotProps.data[3].card.coupound_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[3].card.fabric_name ? (slotProps.data[3].card.fabric_name).slice(0, -2) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[3].card.fabric_weight ? (slotProps.data[3].card.fabric_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[3].card.mat_mp_cost_std ? (slotProps.data[3].card.mat_mp_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[3].card.mat_mp_cost_eff ? (slotProps.data[3].card.mat_mp_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[3].card.fabric_cost_std ? (slotProps.data[3].card.fabric_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[3].card.fabric_cost_eff ? (slotProps.data[3].card.fabric_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[3].card.total_weight ? (slotProps.data[3].card.total_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[3].card.total_cost_std ? (slotProps.data[3].card.total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[3].card.total_cost_eff ? (slotProps.data[3].card.total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
            </template>
        </Column>
        <Column header="Apr">
            <template #body="slotProps">
                <tr>
                    <td @click="showContent(slotProps.data[4].card.compound_name, 4, 0)">
                        {{ (slotProps.data[4].card.compound_name ? (slotProps.data[4].card.compound_name) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[4].card.compound_weight ? (slotProps.data[4].card.compound_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[4].card.me_total_raw_materials ? (slotProps.data[4].card.me_total_raw_materials).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[4].card.me_total_cost_std ? (slotProps.data[4].card.me_total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[4].card.me_total_cost_eff ? (slotProps.data[4].card.me_total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[4].card.coupound_cost_std ? (slotProps.data[4].card.coupound_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[4].card.coupound_cost_eff ? (slotProps.data[4].card.coupound_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[4].card.fabric_name ? (slotProps.data[4].card.fabric_name).slice(0, -2) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[4].card.fabric_weight ? (slotProps.data[4].card.fabric_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[4].card.mat_mp_cost_std ? (slotProps.data[4].card.mat_mp_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[4].card.mat_mp_cost_eff ? (slotProps.data[4].card.mat_mp_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[4].card.fabric_cost_std ? (slotProps.data[4].card.fabric_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[4].card.fabric_cost_eff ? (slotProps.data[4].card.fabric_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[4].card.total_weight ? (slotProps.data[4].card.total_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[4].card.total_cost_std ? (slotProps.data[4].card.total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[4].card.total_cost_eff ? (slotProps.data[4].card.total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
            </template>
        </Column>
        <Column header="May">
            <template #body="slotProps">
                <tr>
                    <td @click="showContent(slotProps.data[5].card.compound_name, 5, 0)">
                        {{ (slotProps.data[5].card.compound_name ? (slotProps.data[5].card.compound_name) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[5].card.compound_weight ? (slotProps.data[5].card.compound_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[5].card.me_total_raw_materials ? (slotProps.data[5].card.me_total_raw_materials).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[5].card.me_total_cost_std ? (slotProps.data[5].card.me_total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[5].card.me_total_cost_eff ? (slotProps.data[5].card.me_total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[5].card.coupound_cost_std ? (slotProps.data[5].card.coupound_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[5].card.coupound_cost_eff ? (slotProps.data[5].card.coupound_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[5].card.fabric_name ? (slotProps.data[5].card.fabric_name).slice(0, -2) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[5].card.fabric_weight ? (slotProps.data[5].card.fabric_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[5].card.mat_mp_cost_std ? (slotProps.data[5].card.mat_mp_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[5].card.mat_mp_cost_eff ? (slotProps.data[5].card.mat_mp_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[5].card.fabric_cost_std ? (slotProps.data[5].card.fabric_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[5].card.fabric_cost_eff ? (slotProps.data[5].card.fabric_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[5].card.total_weight ? (slotProps.data[5].card.total_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[5].card.total_cost_std ? (slotProps.data[5].card.total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[5].card.total_cost_eff ? (slotProps.data[5].card.total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
            </template>
        </Column>
        <Column header="Jun">
            <template #body="slotProps">
                <tr>
                    <td @click="showContent(slotProps.data[6].card.compound_name, 6, 0)">
                        {{ (slotProps.data[6].card.compound_name ? (slotProps.data[6].card.compound_name) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[6].card.compound_weight ? (slotProps.data[6].card.compound_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[6].card.me_total_raw_materials ? (slotProps.data[6].card.me_total_raw_materials).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[6].card.me_total_cost_std ? (slotProps.data[6].card.me_total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[6].card.me_total_cost_eff ? (slotProps.data[6].card.me_total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[6].card.coupound_cost_std ? (slotProps.data[6].card.coupound_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[6].card.coupound_cost_eff ? (slotProps.data[6].card.coupound_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[6].card.fabric_name ? (slotProps.data[6].card.fabric_name).slice(0, -2) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[6].card.fabric_weight ? (slotProps.data[6].card.fabric_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[6].card.mat_mp_cost_std ? (slotProps.data[6].card.mat_mp_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[6].card.mat_mp_cost_eff ? (slotProps.data[6].card.mat_mp_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[6].card.fabric_cost_std ? (slotProps.data[6].card.fabric_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[6].card.fabric_cost_eff ? (slotProps.data[6].card.fabric_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[6].card.total_weight ? (slotProps.data[6].card.total_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[6].card.total_cost_std ? (slotProps.data[6].card.total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[6].card.total_cost_eff ? (slotProps.data[6].card.total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
            </template>
        </Column>
        <Column header="Jul">
            <template #body="slotProps">
                <tr>
                    <td @click="showContent(slotProps.data[7].card.compound_name, 7, 0)">
                        {{ (slotProps.data[7].card.compound_name ? (slotProps.data[7].card.compound_name) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[7].card.compound_weight ? (slotProps.data[7].card.compound_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[7].card.me_total_raw_materials ? (slotProps.data[7].card.me_total_raw_materials).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[7].card.me_total_cost_std ? (slotProps.data[7].card.me_total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[7].card.me_total_cost_eff ? (slotProps.data[7].card.me_total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[7].card.coupound_cost_std ? (slotProps.data[7].card.coupound_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[7].card.coupound_cost_eff ? (slotProps.data[7].card.coupound_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[7].card.fabric_name ? (slotProps.data[7].card.fabric_name).slice(0, -2) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[7].card.fabric_weight ? (slotProps.data[7].card.fabric_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[7].card.mat_mp_cost_std ? (slotProps.data[7].card.mat_mp_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[7].card.mat_mp_cost_eff ? (slotProps.data[7].card.mat_mp_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[7].card.fabric_cost_std ? (slotProps.data[7].card.fabric_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[7].card.fabric_cost_eff ? (slotProps.data[7].card.fabric_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[7].card.total_weight ? (slotProps.data[7].card.total_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[7].card.total_cost_std ? (slotProps.data[7].card.total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[7].card.total_cost_eff ? (slotProps.data[7].card.total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
            </template>
        </Column>
        <Column header="Aug">
            <template #body="slotProps">
                <tr>
                    <td @click="showContent(slotProps.data[8].card.compound_name, 8, 0)">
                        {{ (slotProps.data[8].card.compound_name ? (slotProps.data[8].card.compound_name) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[8].card.compound_weight ? (slotProps.data[8].card.compound_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[8].card.me_total_raw_materials ? (slotProps.data[8].card.me_total_raw_materials).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[8].card.me_total_cost_std ? (slotProps.data[8].card.me_total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[8].card.me_total_cost_eff ? (slotProps.data[8].card.me_total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[8].card.coupound_cost_std ? (slotProps.data[8].card.coupound_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[8].card.coupound_cost_eff ? (slotProps.data[8].card.coupound_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[8].card.fabric_name ? (slotProps.data[8].card.fabric_name).slice(0, -2) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[8].card.fabric_weight ? (slotProps.data[8].card.fabric_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[8].card.mat_mp_cost_std ? (slotProps.data[8].card.mat_mp_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[8].card.mat_mp_cost_eff ? (slotProps.data[8].card.mat_mp_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[8].card.fabric_cost_std ? (slotProps.data[8].card.fabric_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[8].card.fabric_cost_eff ? (slotProps.data[8].card.fabric_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[8].card.total_weight ? (slotProps.data[8].card.total_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[8].card.total_cost_std ? (slotProps.data[8].card.total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[8].card.total_cost_eff ? (slotProps.data[8].card.total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
            </template>
        </Column>
        <Column header="Sep">
            <template #body="slotProps">
                <tr>
                    <td @click="showContent(slotProps.data[9].card.compound_name, 9, 0)">
                        {{ (slotProps.data[9].card.compound_name ? (slotProps.data[9].card.compound_name) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[9].card.compound_weight ? (slotProps.data[9].card.compound_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[9].card.me_total_raw_materials ? (slotProps.data[9].card.me_total_raw_materials).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[9].card.me_total_cost_std ? (slotProps.data[9].card.me_total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[9].card.me_total_cost_eff ? (slotProps.data[9].card.me_total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[9].card.coupound_cost_std ? (slotProps.data[9].card.coupound_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[9].card.coupound_cost_eff ? (slotProps.data[9].card.coupound_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[9].card.fabric_name ? (slotProps.data[9].card.fabric_name).slice(0, -2) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[9].card.fabric_weight ? (slotProps.data[9].card.fabric_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[9].card.mat_mp_cost_std ? (slotProps.data[9].card.mat_mp_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[9].card.mat_mp_cost_eff ? (slotProps.data[9].card.mat_mp_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[9].card.fabric_cost_std ? (slotProps.data[9].card.fabric_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[9].card.fabric_cost_eff ? (slotProps.data[9].card.fabric_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[9].card.total_weight ? (slotProps.data[9].card.total_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[9].card.total_cost_std ? (slotProps.data[9].card.total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[9].card.total_cost_eff ? (slotProps.data[9].card.total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
            </template>
        </Column>
        <Column header="OCt">
            <template #body="slotProps">
                <tr>
                    <td @click="showContent(slotProps.data[10].card.compound_name, 10, 0)">
                        {{ (slotProps.data[10].card.compound_name ? (slotProps.data[10].card.compound_name) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[10].card.compound_weight ? (slotProps.data[10].card.compound_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[10].card.me_total_raw_materials ? (slotProps.data[10].card.me_total_raw_materials).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[10].card.me_total_cost_std ? (slotProps.data[10].card.me_total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[10].card.me_total_cost_eff ? (slotProps.data[10].card.me_total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[10].card.coupound_cost_std ? (slotProps.data[10].card.coupound_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[10].card.coupound_cost_eff ? (slotProps.data[10].card.coupound_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[10].card.fabric_name ? (slotProps.data[10].card.fabric_name).slice(0, -2) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[10].card.fabric_weight ? (slotProps.data[10].card.fabric_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[10].card.mat_mp_cost_std ? (slotProps.data[10].card.mat_mp_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[10].card.mat_mp_cost_eff ? (slotProps.data[10].card.mat_mp_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[10].card.fabric_cost_std ? (slotProps.data[10].card.fabric_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[10].card.fabric_cost_eff ? (slotProps.data[10].card.fabric_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[10].card.total_weight ? (slotProps.data[10].card.total_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[10].card.total_cost_std ? (slotProps.data[10].card.total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[10].card.total_cost_eff ? (slotProps.data[10].card.total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
            </template>
        </Column>
        <Column header="Nov">
            <template #body="slotProps">
                <tr>
                    <td @click="showContent(slotProps.data[11].card.compound_name, 11, 0)">
                        {{ (slotProps.data[11].card.compound_name ? (slotProps.data[11].card.compound_name) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[11].card.compound_weight ? (slotProps.data[11].card.compound_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[11].card.me_total_raw_materials ? (slotProps.data[11].card.me_total_raw_materials).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[11].card.me_total_cost_std ? (slotProps.data[11].card.me_total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[11].card.me_total_cost_eff ? (slotProps.data[11].card.me_total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[11].card.coupound_cost_std ? (slotProps.data[11].card.coupound_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[11].card.coupound_cost_eff ? (slotProps.data[11].card.coupound_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[11].card.fabric_name ? (slotProps.data[11].card.fabric_name).slice(0, -2) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[11].card.fabric_weight ? (slotProps.data[11].card.fabric_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[11].card.mat_mp_cost_std ? (slotProps.data[11].card.mat_mp_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[11].card.mat_mp_cost_eff ? (slotProps.data[11].card.mat_mp_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[11].card.fabric_cost_std ? (slotProps.data[11].card.fabric_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[11].card.fabric_cost_eff ? (slotProps.data[11].card.fabric_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[11].card.total_weight ? (slotProps.data[11].card.total_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[11].card.total_cost_std ? (slotProps.data[11].card.total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[11].card.total_cost_eff ? (slotProps.data[11].card.total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
            </template>
        </Column>
        <Column header="Dec">
            <template #body="slotProps">
                <tr>
                    <td @click="showContent(slotProps.data[12].card.compound_name, 12, 0)">
                        {{ (slotProps.data[12].card.compound_name ? (slotProps.data[12].card.compound_name) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[12].card.compound_weight ? (slotProps.data[12].card.compound_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[12].card.me_total_raw_materials ? (slotProps.data[12].card.me_total_raw_materials).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[12].card.me_total_cost_std ? (slotProps.data[12].card.me_total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[12].card.me_total_cost_eff ? (slotProps.data[12].card.me_total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[12].card.coupound_cost_std ? (slotProps.data[12].card.coupound_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[12].card.coupound_cost_eff ? (slotProps.data[12].card.coupound_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[12].card.fabric_name ? (slotProps.data[12].card.fabric_name).slice(0, -2) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[12].card.fabric_weight ? (slotProps.data[12].card.fabric_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[12].card.mat_mp_cost_std ? (slotProps.data[12].card.mat_mp_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr v-if="showDetails">
                    <td>
                        {{ (slotProps.data[12].card.mat_mp_cost_eff ? (slotProps.data[12].card.mat_mp_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[12].card.fabric_cost_std ? (slotProps.data[12].card.fabric_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[12].card.fabric_cost_eff ? (slotProps.data[12].card.fabric_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[12].card.total_weight ? (slotProps.data[12].card.total_weight).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[12].card.total_cost_std ? (slotProps.data[12].card.total_cost_std).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
                <tr>
                    <td>
                        {{ (slotProps.data[12].card.total_cost_eff ? (slotProps.data[12].card.total_cost_eff).toFixed(fixed.value) : '-') }}
                    </td>
                </tr>
            </template>
        </Column>
    </DataTable>
    <Dialog :modal="true" v-model:visible="display">
            <template #header>
                <h3>Material Breakdown in Material {{ mat }}</h3>
            </template>
            <DataTable :value="modalTable" responsiveLayout="scroll">
                <Column>
                    <template #body="slotProps">
                        <Card>
                            <template #title> Total Cost </template>
                            <template #content>
                                <tr>
                                    <td>Total Cost Std</td>
                                    <td>{{ (slotProps.data.card.totalCostStd.toFixed(fixed.value)) }}</td>
                                </tr>
                                <tr>
                                    <td>Total Cost Eff</td>
                                    <td>{{ (slotProps.data.card.totalCostEff.toFixed(fixed.value)) }}</td>
                                </tr>
                            </template>
                        </Card>
                    </template>
                </Column>
                <Column>
                    <template #body="slotProps">
                        <Card>
                            <template #title> Cost per KG </template>
                            <template #content>
                                <tr>
                                    <td>Cost per KG Std</td>
                                    <td>{{ (slotProps.data.card.costPerKgStd.toFixed(fixed.value)) }}</td>
                                </tr>
                                <tr>
                                    <td>Cost per KG Eff</td>
                                    <td>{{ (slotProps.data.card.costPerKgEff.toFixed(fixed.value)) }}</td>
                                </tr>
                            </template>
                        </Card>
                    </template>
                </Column>
                <Column>
                    <template #body="slotProps">
                        <Card>
                            <template #title> Cost per Liters </template>
                            <template #content>
                                <tr>
                                    <td>Cost per Liter Std</td>
                                    <td>{{ (slotProps.data.card.costPerLiterStd.toFixed(fixed.value)) }}</td>
                                </tr>
                                <tr>
                                    <td>Cost per Liter Eff</td>
                                    <td>{{ (slotProps.data.card.costPerLiterEff.toFixed(fixed.value)) }}</td>
                                </tr>
                            </template>
                        </Card>
                    </template>
                </Column>
                <Column>
                    <template #body="slotProps">
                        <Card>
                            <template #title> Total </template>
                            <template #content>
                                <tr>
                                    <td>Total</td>
                                    <td>{{ (slotProps.data.card.totalRawMaterials.toFixed(fixed.value)) }}</td>
                                </tr>
                                <tr>
                                    <td>Density</td>
                                    <td>{{ (slotProps.data.card.density.toFixed(fixed.value)) }}</td>
                                </tr>
                            </template>
                        </Card>
                    </template>
                </Column>
            </DataTable>
            <DataTable :value="modalTable" responsiveLayout="scroll">
                <template #header>
                    <div class="flex justify-content-between flex-wrap">
                        <div class="flex justify-content-between flex-wrap align-items-center gap-2">
                            <Dropdown optionLabel="text" v-model="fixed" placeholder="Precission value"
                                style="max-width: 200px; float: right" :options="[
                                    { value: 0, text: '0 - precision' },
                                    { value: 1, text: '1 - precision' },
                                    { value: 2, text: '2 - precision' },
                                    { value: 3, text: '3 - precision' },
                                    { value: 4, text: '4 - precision' },
                                    { value: 5, text: '5 - precision' },
                                    { value: 6, text: '6 - precision' },
                                    { value: 7, text: '7 - precision' },
                                ]" />
                                
                            <Dropdown optionLabel="text" v-model="recycleFilter" placeholder="Without Recycle"
                                style="min-width: 250px; float: right" :options="[
                                    { value: 0, text: 'Without Recycle' },
                                    { value: 1, text: 'Without Recycle (No Explosion)' },
                                    { value: 2, text: 'Without Recycle (Explosion)' },
                                ]" @update:model-value="recycleContent(modalPlant, mat, recycleFilter.value, month, modalYear)"/>
                        </div>
                    </div>
                </template>
                <Column header="#">
                    <template #body="slotProps">
                        <tr v-for="(el, index) in slotProps.data.table" :key="index">
                            <td>{{ el.number_material[0] }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Raw Material">
                    <template #body="slotProps">
                        <tr v-for="(el, index) in slotProps.data.table" :key="index">
                            <td>{{ el.raw_material }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Unit">
                    <template #body="slotProps">
                        <tr v-for="(el, index) in slotProps.data.table" :key="index">
                            <td>KG</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Cost per Unit (STD)">
                    <template #body="slotProps">
                        <tr v-for="(el, index) in slotProps.data.table" :key="index">
                            <td>{{ (el.cost_per_unit_std).toFixed(fixed.value) }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Cost per Unit (EFF)">
                    <template #body="slotProps">
                        <tr v-for="(el, index) in slotProps.data.table" :key="index">
                            <td>{{ (el.cost_per_unit_eff).toFixed(fixed.value) }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Raw Weight">
                    <template #body="slotProps">
                        <tr v-for="(el, index) in slotProps.data.table" :key="index">
                            <td>{{ (el.raw_weight).toFixed(fixed.value) }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Raw Weight %">
                    <template #body="slotProps">
                        <tr v-for="(el, index) in slotProps.data.table" :key="index">
                            <td>{{ (el.raw_weight_percent).toFixed(fixed.value) }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Total Cost (STD)">
                    <template #body="slotProps">
                        <tr v-for="(el, index) in slotProps.data.table" :key="index">
                            <td>{{ (el.total_cost_std).toFixed(fixed.value) }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Total Cost (EFF)">
                    <template #body="slotProps">
                        <tr v-for="(el, index) in slotProps.data.table" :key="index">
                            <td>{{ (el.total_cost_eff).toFixed(fixed.value) }}</td>
                        </tr>
                    </template>
                </Column>
            </DataTable>
    </Dialog>
</template>
<script setup>
import { ref, onMounted, computed } from "vue";
import Column from "primevue/column";
import axios from "axios";
import Chip from 'primevue/chip';
import Dialog from 'primevue/dialog'
import { useConfigStore } from '@/store/config';
import { FilterMatchMode } from 'primevue/api';
import InputSwitch from "primevue/inputswitch";
import Dropdown from 'primevue/dropdown';
import TableRaw from '@/layout/components/arrow-table/index.vue'
const display = ref(false)

let modalTable = ref([]);
let mat = ref("");
let month = ref(0);
let recycleFilter = ref(0)
let modalPlant = ref("")
let modalYear = ref()


const config = useConfigStore()
const props = defineProps(['tableValue', 'plantSelected', 'year'])
const changeFixed = () => {
    config.setFixed(props)
}

const showContent = async (rawMaterial, mo) => {


    recycleFilter.value = 0
    modalTable.value = []
    display.value = true;
    mat.value = rawMaterial;
    month.value = mo;
    modalPlant = props.plantSelected.value
    modalYear = props.year
    const response = await axios.get(
        "http://localhost:8000/api/v1/report_raw_material_breakdown/?plant=" +
        props.plantSelected.value +
        "&product=" +
        mat.value +
        "&filter=" +
        recycleFilter.value +
        "&month=" +
        month.value +
        "&year=" +
        props.year
    );
    modalTable.value = response.data;
    recycleFilter.value = 0
};

const recycleContent = async (plant, rawMaterial, filter, mo, year) => {
    modalTable.value = []
    const response = await axios.get(
        "http://localhost:8000/api/v1/report_raw_material_breakdown/?plant=" +
        plant +
        "&product=" +
        rawMaterial +
        "&filter=" +
        filter +
        "&month=" +
        mo +
        "&year=" +
        year
    );
    modalTable.value = response.data;
    recycleFilter.value = 0
    console.log(modalTable.value);
};

const showDetails = ref(false)
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
<style>
.p-dialog-mask.p-component-overlay.p-component-overlay-enter {
    z-index: 999 !important;
}
</style>