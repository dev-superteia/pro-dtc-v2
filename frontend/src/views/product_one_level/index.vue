<template>
    <h3>Product One-Level</h3>
    <div class="grid p-fluid">
        <div class="col-12">
            <h3>{{ $t("dtc.plant") }}</h3>
            <div class="p-inputgroup">
                <Dropdown optionLabel="text" v-model="plantSelected" :options="plant" placeholder="Select a plant" />
            </div>
        </div>
        <div class="col-12">
            <h3>{{ $t("dtc.line") }}</h3>
            <div class="p-inputgroup">
                <Dropdown optionLabel="text" placeholder="Select a line" v-model="lineSelected" :options="line" />
            </div>
        </div>
        <div class="col-12">
            <h3>{{ $t("dtc.mkg") }}</h3>
            <div class="p-inputgroup">
                <Dropdown optionLabel="text" placeholder="Market Segment" v-model="mkgSelected" :options="mkg" />
            </div>
        </div>
        <div class="col-12">
            <h3>{{ $t("dtc.product") }}</h3>
            <div class="p-inputgroup">
                <Dropdown editable optionLabel="text" placeholder="Product" v-model="tireSelected" :options="tire" />
            </div>
        </div>
        <div class="col-12">
            <h3>{{ $t("dtc.year") }}</h3>
            <div class="p-inputgroup">
                <InputText placeholder="Year" v-model="year" />
            </div>
        </div>
        <div class="col-2 mt-3">
            <Button v-if="!progress" :label="$t('message.search')" @click="submit()" icon="pi pi-send"
                iconPos="right"></Button>
            <ProgressSpinner v-if="progress" style="width: 50px; height: 50px" strokeWidth="8"
                fill="var(--surface-ground)" animationDuration=".5s" aria-label="Custom ProgressSpinner" />
        </div>
        <div class="col-12 mt-3">
        <Dropdown v-model="graphselected" :options="graph" optionLabel="text" placeholder="Select a graph value" @change="changeGra()"/>   
        <Chart type="line" :data="datasets" class="w-full p-5" />

        </div>
        <div class="col-12">
            <div style="display: flex; margin: 50px 0; justify-content: center">
                <div style="display: flex">
                    <InputSwitch v-model="showTotalValue" />
                    <h3 style="margin: 0 10px">Total Value</h3>
                </div>
                <div style="display: flex">
                    <InputSwitch v-model="showAmount" />
                    <h3 style="margin: 0 10px">Amount Used</h3>
                </div>
                <div style="display: flex">
                    <InputSwitch v-model="showMatCostStd" />
                    <h3 style="margin: 0 10px">Material Cost Standard</h3>
                </div>
                <div style="display: flex">
                    <InputSwitch v-model="showMatCostEff" />
                    <h3 style="margin: 0 10px">Material Cost Effective</h3>
                </div>
                <div style="display: flex">
                    <InputSwitch v-model="showTotalCostStd" />
                    <h3 style="margin: 0 10px">Total Cost Standard</h3>
                </div>
                <div style="display: flex">
                    <InputSwitch v-model="showTotalCostEff" />
                    <h3 style="margin: 0 10px">Total Cost Effective</h3>
                </div>
            </div>
            <DataTable :value="items_totais" responsiveLayout="scroll" :filters="filters" :paginator="true" :rows="-1">
                <Column :header="$t('dtc.values')" style="min-width: 200px">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td>Amount Used</td>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td>Mat. Cost Std</td>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td>Mat. Cost Eff</td>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td>Cost Std</td>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td>Cost Eff</td>
                        </tr>
                        <tr>
                            <td>DTC</td>
                        </tr>
                        <tr v-if="showTotalValue">
                            <td>Volume</td>
                        </tr>
                    </template>
                </Column>
                <Column v-if="!showTotalValue" header="Standard" style="min-width:200px">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td>{{ slotProps.data.values[0].totalWeightStd }}</td>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td>{{ slotProps.data.values[0].materialCostStd }}</td>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td>{{ slotProps.data.values[0].materialCostEff }}</td>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td>{{ slotProps.data.values[0].totalCostStd }}</td>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td>{{ slotProps.data.values[0].totalCostEff }}</td>
                        </tr>
                        <tr>
                            <td>{{ slotProps.data.values[0].dtc }}</td>
                        </tr>
                        <tr v-if="showTotalValue">
                            <td>{{ slotProps.data.values[0].volum }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Jan" style="min-width:200px">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[1].totalWeightStd *
                                        slotProps.data.values[1].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalWeightStd
                                    ? slotProps.data.values[0].totalWeightStd
                                    : 0,
                                eff: slotProps.data.values[1].totalWeightStd
                                    ? slotProps.data.values[1].totalWeightStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[1].materialCostStd *
                                        slotProps.data.values[1].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostStd
                                    ? slotProps.data.values[0].materialCostStd
                                    : 0,
                                eff: slotProps.data.values[1].materialCostStd
                                    ? slotProps.data.values[1].materialCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[1].materialCostEff *
                                        slotProps.data.values[1].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostEff
                                    ? slotProps.data.values[0].materialCostEff
                                    : 0,
                                eff: slotProps.data.values[1].materialCostEff
                                    ? slotProps.data.values[1].materialCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[1].totalCostStd *
                                        slotProps.data.values[1].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostStd
                                    ? slotProps.data.values[0].totalCostStd
                                    : 0,
                                eff: slotProps.data.values[1].totalCostStd
                                    ? slotProps.data.values[1].totalCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[1].totalCostEff *
                                        slotProps.data.values[1].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostEff
                                    ? slotProps.data.values[0].totalCostEff
                                    : 0,
                                eff: slotProps.data.values[1].totalCostEff
                                    ? slotProps.data.values[1].totalCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[1].dtc * slotProps.data.values[1].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].dtc
                                    ? slotProps.data.values[0].dtc
                                    : 0,
                                eff: slotProps.data.values[1].dtc
                                    ? slotProps.data.values[1].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalValue">
                            <td>{{ slotProps.data.values[1].volum }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Feb" style="min-width:200px">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[2].totalWeightStd *
                                        slotProps.data.values[2].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalWeightStd
                                    ? slotProps.data.values[0].totalWeightStd
                                    : 0,
                                eff: slotProps.data.values[2].totalWeightStd
                                    ? slotProps.data.values[2].totalWeightStd
                                    : 0,
                            }">
                            </TableRaw>
                            
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[2].materialCostStd *
                                        slotProps.data.values[2].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostStd
                                    ? slotProps.data.values[0].materialCostStd
                                    : 0,
                                eff: slotProps.data.values[2].materialCostStd
                                    ? slotProps.data.values[2].materialCostStd
                                    : 0,
                            }">
                            </TableRaw>

                        </tr>
                        <tr v-if="showMatCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[2].materialCostEff *
                                        slotProps.data.values[2].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostEff
                                    ? slotProps.data.values[0].materialCostEff
                                    : 0,
                                eff: slotProps.data.values[2].materialCostEff
                                    ? slotProps.data.values[2].materialCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[2].totalCostStd *
                                        slotProps.data.values[2].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostStd
                                    ? slotProps.data.values[0].totalCostStd
                                    : 0,
                                eff: slotProps.data.values[2].totalCostStd
                                    ? slotProps.data.values[2].totalCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[2].totalCostEff *
                                        slotProps.data.values[2].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostEff
                                    ? slotProps.data.values[0].totalCostEff
                                    : 0,
                                eff: slotProps.data.values[2].totalCostEff
                                    ? slotProps.data.values[2].totalCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[2].dtc * slotProps.data.values[2].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].dtc
                                    ? slotProps.data.values[0].dtc
                                    : 0,
                                eff: slotProps.data.values[2].dtc
                                    ? slotProps.data.values[2].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalValue">
                            <td>{{ slotProps.data.values[2].volum }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Mar" style="min-width:200px">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[3].totalWeightStd *
                                        slotProps.data.values[3].dtc
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalWeightStd
                                    ? slotProps.data.values[0].totalWeightStd
                                    : 0,
                                eff: slotProps.data.values[3].totalWeightStd
                                    ? slotProps.data.values[3].totalWeightStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[3].materialCostStd *
                                        slotProps.data.values[3].dtc
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostStd
                                    ? slotProps.data.values[0].materialCostStd
                                    : 0,
                                eff: slotProps.data.values[3].materialCostStd
                                    ? slotProps.data.values[3].materialCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[3].materialCostEff *
                                        slotProps.data.values[3].dtc
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostEff
                                    ? slotProps.data.values[0].materialCostEff
                                    : 0,
                                eff: slotProps.data.values[3].materialCostEff
                                    ? slotProps.data.values[3].materialCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[3].totalCostStd *
                                        slotProps.data.values[3].dtc
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostStd
                                    ? slotProps.data.values[0].totalCostStd
                                    : 0,
                                eff: slotProps.data.values[3].totalCostStd
                                    ? slotProps.data.values[3].totalCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[3].totalCostEff *
                                        slotProps.data.values[3].dtc
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostEff
                                    ? slotProps.data.values[0].totalCostEff
                                    : 0,
                                eff: slotProps.data.values[3].totalCostEff
                                    ? slotProps.data.values[3].totalCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[3].dtc * slotProps.data.values[3].dtc
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].dtc
                                    ? slotProps.data.values[0].dtc
                                    : 0,
                                eff: slotProps.data.values[3].dtc
                                    ? slotProps.data.values[3].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalValue">
                            <td>{{ slotProps.data.values[3].volum }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Apr" style="min-width:200px">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[4].totalWeightStd *
                                        slotProps.data.values[4].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalWeightStd
                                    ? slotProps.data.values[0].totalWeightStd
                                    : 0,
                                eff: slotProps.data.values[4].totalWeightStd
                                    ? slotProps.data.values[4].totalWeightStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[4].materialCostStd *
                                        slotProps.data.values[4].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostStd
                                    ? slotProps.data.values[0].materialCostStd
                                    : 0,
                                eff: slotProps.data.values[4].materialCostStd
                                    ? slotProps.data.values[4].materialCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[4].materialCostEff *
                                        slotProps.data.values[4].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostEff
                                    ? slotProps.data.values[0].materialCostEff
                                    : 0,
                                eff: slotProps.data.values[4].materialCostEff
                                    ? slotProps.data.values[4].materialCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[4].totalCostStd *
                                        slotProps.data.values[4].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostStd
                                    ? slotProps.data.values[0].totalCostStd
                                    : 0,
                                eff: slotProps.data.values[4].totalCostStd
                                    ? slotProps.data.values[4].totalCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[4].totalCostEff *
                                        slotProps.data.values[4].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostEff
                                    ? slotProps.data.values[0].totalCostEff
                                    : 0,
                                eff: slotProps.data.values[4].totalCostEff
                                    ? slotProps.data.values[4].totalCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[4].dtc * slotProps.data.values[4].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].dtc
                                    ? slotProps.data.values[0].dtc
                                    : 0,
                                eff: slotProps.data.values[4].dtc
                                    ? slotProps.data.values[4].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalValue">
                            <td>{{ slotProps.data.values[4].volum }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="May" style="min-width:200px">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[5].totalWeightStd *
                                        slotProps.data.values[5].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalWeightStd
                                    ? slotProps.data.values[0].totalWeightStd
                                    : 0,
                                eff: slotProps.data.values[5].totalWeightStd
                                    ? slotProps.data.values[5].totalWeightStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[5].materialCostStd *
                                        slotProps.data.values[5].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostStd
                                    ? slotProps.data.values[0].materialCostStd
                                    : 0,
                                eff: slotProps.data.values[5].materialCostStd
                                    ? slotProps.data.values[5].materialCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[5].materialCostEff *
                                        slotProps.data.values[5].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostEff
                                    ? slotProps.data.values[0].materialCostEff
                                    : 0,
                                eff: slotProps.data.values[5].materialCostEff
                                    ? slotProps.data.values[5].materialCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[5].totalCostStd *
                                        slotProps.data.values[5].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostStd
                                    ? slotProps.data.values[0].totalCostStd
                                    : 0,
                                eff: slotProps.data.values[5].totalCostStd
                                    ? slotProps.data.values[5].totalCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[5].totalCostEff *
                                        slotProps.data.values[5].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostEff
                                    ? slotProps.data.values[0].totalCostEff
                                    : 0,
                                eff: slotProps.data.values[5].totalCostEff
                                    ? slotProps.data.values[5].totalCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[5].dtc * slotProps.data.values[5].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].dtc
                                    ? slotProps.data.values[0].dtc
                                    : 0,
                                eff: slotProps.data.values[5].dtc
                                    ? slotProps.data.values[5].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalValue">
                            <td>{{ slotProps.data.values[5].volum }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Jun" style="min-width:200px">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[6].totalWeightStd *
                                        slotProps.data.values[6].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalWeightStd
                                    ? slotProps.data.values[0].totalWeightStd
                                    : 0,
                                eff: slotProps.data.values[6].totalWeightStd
                                    ? slotProps.data.values[6].totalWeightStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[6].materialCostStd *
                                        slotProps.data.values[6].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostStd
                                    ? slotProps.data.values[0].materialCostStd
                                    : 0,
                                eff: slotProps.data.values[6].materialCostStd
                                    ? slotProps.data.values[6].materialCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[6].materialCostEff *
                                        slotProps.data.values[6].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostEff
                                    ? slotProps.data.values[0].materialCostEff
                                    : 0,
                                eff: slotProps.data.values[6].materialCostEff
                                    ? slotProps.data.values[6].materialCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[6].totalCostStd *
                                        slotProps.data.values[6].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostStd
                                    ? slotProps.data.values[0].totalCostStd
                                    : 0,
                                eff: slotProps.data.values[6].totalCostStd
                                    ? slotProps.data.values[6].totalCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[6].totalCostEff *
                                        slotProps.data.values[6].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostEff
                                    ? slotProps.data.values[0].totalCostEff
                                    : 0,
                                eff: slotProps.data.values[6].totalCostEff
                                    ? slotProps.data.values[6].totalCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[6].dtc * slotProps.data.values[6].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].dtc
                                    ? slotProps.data.values[0].dtc
                                    : 0,
                                eff: slotProps.data.values[6].dtc
                                    ? slotProps.data.values[6].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalValue">
                            <td>{{ slotProps.data.values[6].volum }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Jul" style="min-width:200px">
                    <template #body="slotProps">
                            <tr v-if="showAmount">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[7].totalWeightStd *
                                        slotProps.data.values[7].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalWeightStd
                                    ? slotProps.data.values[0].totalWeightStd
                                    : 0,
                                eff: slotProps.data.values[7].totalWeightStd
                                    ? slotProps.data.values[7].totalWeightStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[7].materialCostStd *
                                        slotProps.data.values[7].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostStd
                                    ? slotProps.data.values[0].materialCostStd
                                    : 0,
                                eff: slotProps.data.values[7].materialCostStd
                                    ? slotProps.data.values[7].materialCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[7].materialCostEff *
                                        slotProps.data.values[7].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostEff
                                    ? slotProps.data.values[0].materialCostEff
                                    : 0,
                                eff: slotProps.data.values[7].materialCostEff
                                    ? slotProps.data.values[7].materialCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[7].totalCostStd *
                                        slotProps.data.values[7].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostStd
                                    ? slotProps.data.values[0].totalCostStd
                                    : 0,
                                eff: slotProps.data.values[7].totalCostStd
                                    ? slotProps.data.values[7].totalCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[7].totalCostEff *
                                        slotProps.data.values[7].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostEff
                                    ? slotProps.data.values[0].totalCostEff
                                    : 0,
                                eff: slotProps.data.values[7].totalCostEff
                                    ? slotProps.data.values[7].totalCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[7].dtc * slotProps.data.values[7].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].dtc
                                    ? slotProps.data.values[0].dtc
                                    : 0,
                                eff: slotProps.data.values[7].dtc
                                    ? slotProps.data.values[7].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalValue">
                            <td>{{ slotProps.data.values[7].volum }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Aug" style="min-width:200px">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[8].totalWeightStd *
                                        slotProps.data.values[8].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalWeightStd
                                    ? slotProps.data.values[0].totalWeightStd
                                    : 0,
                                eff: slotProps.data.values[8].totalWeightStd
                                    ? slotProps.data.values[8].totalWeightStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[8].materialCostStd *
                                        slotProps.data.values[8].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostStd
                                    ? slotProps.data.values[0].materialCostStd
                                    : 0,
                                eff: slotProps.data.values[8].materialCostStd
                                    ? slotProps.data.values[8].materialCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[8].materialCostEff *
                                        slotProps.data.values[8].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostEff
                                    ? slotProps.data.values[0].materialCostEff
                                    : 0,
                                eff: slotProps.data.values[8].materialCostEff
                                    ? slotProps.data.values[8].materialCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[8].totalCostStd *
                                        slotProps.data.values[8].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostStd
                                    ? slotProps.data.values[0].totalCostStd
                                    : 0,
                                eff: slotProps.data.values[8].totalCostStd
                                    ? slotProps.data.values[8].totalCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[8].totalCostEff *
                                        slotProps.data.values[8].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostEff
                                    ? slotProps.data.values[0].totalCostEff
                                    : 0,
                                eff: slotProps.data.values[8].totalCostEff
                                    ? slotProps.data.values[8].totalCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[8].dtc * slotProps.data.values[8].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].dtc
                                    ? slotProps.data.values[0].dtc
                                    : 0,
                                eff: slotProps.data.values[8].dtc
                                    ? slotProps.data.values[8].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalValue">
                            <td>{{ slotProps.data.values[8].volum }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Sep" style="min-width:200px">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[9].totalWeightStd *
                                        slotProps.data.values[9].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalWeightStd
                                    ? slotProps.data.values[0].totalWeightStd
                                    : 0,
                                eff: slotProps.data.values[9].totalWeightStd
                                    ? slotProps.data.values[9].totalWeightStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[9].materialCostStd *
                                        slotProps.data.values[9].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostStd
                                    ? slotProps.data.values[0].materialCostStd
                                    : 0,
                                eff: slotProps.data.values[9].materialCostStd
                                    ? slotProps.data.values[9].materialCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[9].materialCostEff *
                                        slotProps.data.values[9].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostEff
                                    ? slotProps.data.values[0].materialCostEff
                                    : 0,
                                eff: slotProps.data.values[9].materialCostEff
                                    ? slotProps.data.values[9].materialCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[9].totalCostStd *
                                        slotProps.data.values[9].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostStd
                                    ? slotProps.data.values[0].totalCostStd
                                    : 0,
                                eff: slotProps.data.values[9].totalCostStd
                                    ? slotProps.data.values[9].totalCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[9].totalCostEff *
                                        slotProps.data.values[9].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostEff
                                    ? slotProps.data.values[0].totalCostEff
                                    : 0,
                                eff: slotProps.data.values[9].totalCostEff
                                    ? slotProps.data.values[9].totalCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[9].dtc * slotProps.data.values[9].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].dtc
                                    ? slotProps.data.values[0].dtc
                                    : 0,
                                eff: slotProps.data.values[9].dtc
                                    ? slotProps.data.values[9].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalValue">
                            <td>{{ slotProps.data.values[9].volum }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Out" style="min-width:200px">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[10].totalWeightStd *
                                        slotProps.data.values[10].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalWeightStd
                                    ? slotProps.data.values[0].totalWeightStd
                                    : 0,
                                eff: slotProps.data.values[10].totalWeightStd
                                    ? slotProps.data.values[10].totalWeightStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[10].materialCostStd *
                                        slotProps.data.values[10].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostStd
                                    ? slotProps.data.values[0].materialCostStd
                                    : 0,
                                eff: slotProps.data.values[10].materialCostStd
                                    ? slotProps.data.values[10].materialCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[10].materialCostEff *
                                        slotProps.data.values[10].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostEff
                                    ? slotProps.data.values[0].materialCostEff
                                    : 0,
                                eff: slotProps.data.values[10].materialCostEff
                                    ? slotProps.data.values[10].materialCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[10].totalCostStd *
                                        slotProps.data.values[10].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostStd
                                    ? slotProps.data.values[0].totalCostStd
                                    : 0,
                                eff: slotProps.data.values[10].totalCostStd
                                    ? slotProps.data.values[10].totalCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[10].totalCostEff *
                                        slotProps.data.values[10].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostEff
                                    ? slotProps.data.values[0].totalCostEff
                                    : 0,
                                eff: slotProps.data.values[10].totalCostEff
                                    ? slotProps.data.values[10].totalCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[10].dtc * slotProps.data.values[10].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].dtc
                                    ? slotProps.data.values[0].dtc
                                    : 0,
                                eff: slotProps.data.values[10].dtc
                                    ? slotProps.data.values[10].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalValue">
                            <td>{{ slotProps.data.values[10].volum }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Nov" style="min-width:200px">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[11].totalWeightStd *
                                        slotProps.data.values[11].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalWeightStd
                                    ? slotProps.data.values[0].totalWeightStd
                                    : 0,
                                eff: slotProps.data.values[11].totalWeightStd
                                    ? slotProps.data.values[11].totalWeightStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[11].materialCostStd *
                                        slotProps.data.values[11].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostStd
                                    ? slotProps.data.values[0].materialCostStd
                                    : 0,
                                eff: slotProps.data.values[11].materialCostStd
                                    ? slotProps.data.values[11].materialCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[11].materialCostEff *
                                        slotProps.data.values[11].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostEff
                                    ? slotProps.data.values[0].materialCostEff
                                    : 0,
                                eff: slotProps.data.values[11].materialCostEff
                                    ? slotProps.data.values[11].materialCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[11].totalCostStd *
                                        slotProps.data.values[11].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostStd
                                    ? slotProps.data.values[0].totalCostStd
                                    : 0,
                                eff: slotProps.data.values[11].totalCostStd
                                    ? slotProps.data.values[11].totalCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[11].totalCostEff *
                                        slotProps.data.values[11].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostEff
                                    ? slotProps.data.values[0].totalCostEff
                                    : 0,
                                eff: slotProps.data.values[11].totalCostEff
                                    ? slotProps.data.values[11].totalCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[11].dtc * slotProps.data.values[11].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].dtc
                                    ? slotProps.data.values[0].dtc
                                    : 0,
                                eff: slotProps.data.values[11].dtc
                                    ? slotProps.data.values[11].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalValue">
                            <td>{{ slotProps.data.values[11].volum }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Dez" style="min-width:200px">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[12].totalWeightStd *
                                        slotProps.data.values[12].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalWeightStd
                                    ? slotProps.data.values[0].totalWeightStd
                                    : 0,
                                eff: slotProps.data.values[12].totalWeightStd
                                    ? slotProps.data.values[12].totalWeightStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[12].materialCostStd *
                                        slotProps.data.values[12].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostStd
                                    ? slotProps.data.values[0].materialCostStd
                                    : 0,
                                eff: slotProps.data.values[12].materialCostStd
                                    ? slotProps.data.values[12].materialCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[12].materialCostEff *
                                        slotProps.data.values[12].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostEff
                                    ? slotProps.data.values[0].materialCostEff
                                    : 0,
                                eff: slotProps.data.values[12].materialCostEff
                                    ? slotProps.data.values[12].materialCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[12].totalCostStd *
                                        slotProps.data.values[12].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostStd
                                    ? slotProps.data.values[0].totalCostStd
                                    : 0,
                                eff: slotProps.data.values[12].totalCostStd
                                    ? slotProps.data.values[12].totalCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[12].totalCostEff *
                                        slotProps.data.values[12].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostEff
                                    ? slotProps.data.values[0].totalCostEff
                                    : 0,
                                eff: slotProps.data.values[12].totalCostEff
                                    ? slotProps.data.values[12].totalCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[12].dtc * slotProps.data.values[12].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].dtc
                                    ? slotProps.data.values[0].dtc
                                    : 0,
                                eff: slotProps.data.values[12].dtc
                                    ? slotProps.data.values[12].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalValue">
                            <td>{{ slotProps.data.values[12].volum }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Year" style="min-width:200px">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[13].totalWeightStd *
                                        slotProps.data.values[13].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalWeightStd
                                    ? slotProps.data.values[0].totalWeightStd
                                    : 0,
                                eff: slotProps.data.values[13].totalWeightStd
                                    ? slotProps.data.values[13].totalWeightStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[13].materialCostStd *
                                        slotProps.data.values[13].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostStd
                                    ? slotProps.data.values[0].materialCostStd
                                    : 0,
                                eff: slotProps.data.values[13].materialCostStd
                                    ? slotProps.data.values[13].materialCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[13].materialCostEff *
                                        slotProps.data.values[13].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].materialCostEff
                                    ? slotProps.data.values[0].materialCostEff
                                    : 0,
                                eff: slotProps.data.values[13].materialCostEff
                                    ? slotProps.data.values[13].materialCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[13].totalCostStd *
                                        slotProps.data.values[13].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostStd
                                    ? slotProps.data.values[0].totalCostStd
                                    : 0,
                                eff: slotProps.data.values[13].totalCostStd
                                    ? slotProps.data.values[13].totalCostStd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[13].totalCostEff *
                                        slotProps.data.values[13].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].totalCostEff
                                    ? slotProps.data.values[0].totalCostEff
                                    : 0,
                                eff: slotProps.data.values[13].totalCostEff
                                    ? slotProps.data.values[13].totalCostEff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data.values[13].dtc * slotProps.data.values[13].volum
                                }}
                            </td>
                            <TableRaw v-else :value="{
                                std: slotProps.data.values[0].dtc
                                    ? slotProps.data.values[0].dtc
                                    : 0,
                                eff: slotProps.data.values[13].dtc
                                    ? slotProps.data.values[13].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalValue">
                            <td>{{ slotProps.data.values[13].volum }}</td>
                        </tr>
                    </template>
                </Column>
            </DataTable>
            <DataTable ref="dt" :value="table" responsiveLayout="scroll" :rowsPerPageOptions="[10, 20, 50]"
                :filters="filters" :paginator="true" :rows="10">
                <template #header>
                    <div class="flex justify-content-between flex-wrap">
                        <div>
                            <span class="p-input-icon-left">
                                <i class="pi pi-search" />
                                <InputText v-model="filters['global'].value" placeholder="Search..."
                                    style="max-width: 200px" />
                            </span>
                        </div>
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
                            <div style="text-align: left; width: 200px">
                                <Button icon="pi pi-external-link" label="Export" @click="exportCSV($event)" />
                            </div>
                        </div>
                    </div>
                </template>
                <Column field="0" :header="$t('dtc.raw_material')" :sortable="true"></Column>
                <Column :header="$t('dtc.values')" style="min-width: 200px">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td>Amount Used</td>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td>Mat. Cost Std</td>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td>Mat. Cost Eff</td>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td>Cost Std</td>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td>Cost Eff</td>
                        </tr>
                        <tr>
                            <td>DTC</td>
                        </tr>
                    </template>
                </Column>
                <Column v-if="!showTotalValue" header="Standard">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td @click="showContent(slotProps.data[0], 0, 0)" v-if="showAmount">
                                {{
                                    slotProps.data[1].months[0].amount_used_std
                                        ? slotProps.data[1].months[0].amount_used_std
                                        : "-"
                                }}
                            </td>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td @click="showContent(slotProps.data[0], 0, 0)">
                                {{
                                    slotProps.data[1].months[0].totalcoststd
                                        ? slotProps.data[1].months[0].totalcoststd
                                        : "-"
                                }}
                            </td>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td @click="showContent(slotProps.data[0], 0, 0)">
                                {{
                                    slotProps.data[1].months[0].totalcosteff
                                        ? slotProps.data[1].months[0].totalcosteff
                                        : "-"
                                }}
                            </td>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data[0], 0, 0)">
                                {{
                                    slotProps.data[1].months[0].material_cost_1_tire_standard
                                        ? slotProps.data[1].months[0].material_cost_1_tire_standard
                                        : "-"
                                }}
                            </td>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data[0], 0, 0)">
                                {{
                                    slotProps.data[1].months[0].material_cost_1_tire_effective
                                        ? slotProps.data[1].months[0].material_cost_1_tire_effective
                                        : "-"
                                }}
                            </td>
                        </tr>
                        <tr>
                            <td @click="showContent(slotProps.data[0], 0, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[0].dtc_volum
                                        ? slotProps.data[1].months[0].dtc_volum
                                        : "-"
                                }}
                            </td>
                            <td @click="showContent(slotProps.data[0], 0, 0)" v-else>
                                {{
                                    slotProps.data[1].months[0].dtc
                                        ? slotProps.data[1].months[0].dtc
                                        : "-"
                                }}
                            </td>
                        </tr>
                    </template>
                </Column>
                <Column header="Jan" style="min-width: 200px;">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td @click="showContent(slotProps.data[0], 1, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[1].amount_used_eff_volum
                                        ? slotProps.data[1].months[1].amount_used_eff_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 1, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].amount_used_eff
                                    ? slotProps.data[1].months[0].amount_used_eff
                                    : 0,
                                eff: slotProps.data[1].months[1].amount_used_eff
                                        ? slotProps.data[1].months[1].amount_used_eff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td @click="showContent(slotProps.data[0], 1, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[1].totalcoststd_volum
                                        ? slotProps.data[1].months[1].totalcoststd_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 1, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].totalcoststd
                                    ? slotProps.data[1].months[0].totalcoststd
                                    : 0,
                                eff: slotProps.data[1].months[1].totalcoststd
                                        ? slotProps.data[1].months[1].totalcoststd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td @click="showContent(slotProps.data[0], 1, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[1].totalcosteff_volum
                                        ? slotProps.data[1].months[1].totalcosteff_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 1, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].totalcosteff
                                    ? slotProps.data[1].months[0].totalcosteff
                                    : 0,
                                eff: slotProps.data[1].months[1].totalcosteff
                                        ? slotProps.data[1].months[1].totalcosteff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data[0], 1, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[1]
                                        .material_cost_1_tire_standard_volum
                                        ? slotProps.data[1].months[1]
                                            .material_cost_1_tire_standard_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 1, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].material_cost_1_tire_standard
                                    ? slotProps.data[1].months[0].material_cost_1_tire_standard
                                    : 0,
                                eff: slotProps.data[1].months[1].material_cost_1_tire_standard
                                        ? slotProps.data[1].months[1].material_cost_1_tire_standard
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data[0], 1, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[1]
                                        .material_cost_1_tire_effective_volum
                                        ? slotProps.data[1].months[1]
                                            .material_cost_1_tire_effective_volum
                                        : "-"
                                }}
                            </td>

                            <TableRaw @click="showContent(slotProps.data[0], 1, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].material_cost_1_tire_effective
                                    ? slotProps.data[1].months[0].material_cost_1_tire_effective
                                    : 0,
                                eff: slotProps.data[1].months[1].material_cost_1_tire_effective
                                        ? slotProps.data[1].months[1].material_cost_1_tire_effective
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td @click="showContent(slotProps.data[0], 1, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[1].dtc_volum
                                        ? slotProps.data[1].months[1].dtc_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 1, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].dtc
                                    ? slotProps.data[1].months[0].dtc
                                    : 0,
                                eff: slotProps.data[1].months[1].dtc
                                        ? slotProps.data[1].months[1].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                    </template>
                </Column>
                <Column header="Feb" style="min-width: 200px;">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td @click="showContent(slotProps.data[0], 2, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[2].amount_used_eff_volum
                                        ? slotProps.data[1].months[2].amount_used_eff_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 2, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].amount_used_eff
                                    ? slotProps.data[1].months[0].amount_used_eff
                                    : 0,
                                eff: slotProps.data[1].months[2].amount_used_eff
                                        ? slotProps.data[1].months[2].amount_used_eff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td @click="showContent(slotProps.data[0], 2, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[2].totalcoststd_volum
                                        ? slotProps.data[1].months[2].totalcoststd_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 2, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].totalcoststd
                                    ? slotProps.data[1].months[0].totalcoststd
                                    : 0,
                                eff: slotProps.data[1].months[2].totalcoststd
                                        ? slotProps.data[1].months[2].totalcoststd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td @click="showContent(slotProps.data[0], 2, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[2].totalcosteff_volum
                                        ? slotProps.data[1].months[2].totalcosteff_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 2, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].totalcosteff
                                    ? slotProps.data[1].months[0].totalcosteff
                                    : 0,
                                eff: slotProps.data[1].months[2].totalcosteff
                                        ? slotProps.data[1].months[2].totalcosteff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data[0], 2, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[2]
                                        .material_cost_1_tire_standard_volum
                                        ? slotProps.data[1].months[2]
                                            .material_cost_1_tire_standard_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 2, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].material_cost_1_tire_standard
                                    ? slotProps.data[1].months[0].material_cost_1_tire_standard
                                    : 0,
                                eff: slotProps.data[1].months[2].material_cost_1_tire_standard
                                        ? slotProps.data[1].months[2].material_cost_1_tire_standard
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data[0], 2, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[2]
                                        .material_cost_1_tire_effective_volum
                                        ? slotProps.data[1].months[2]
                                            .material_cost_1_tire_effective_volum
                                        : "-"
                                }}
                            </td>

                            <TableRaw @click="showContent(slotProps.data[0], 2, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].material_cost_1_tire_effective
                                    ? slotProps.data[1].months[0].material_cost_1_tire_effective
                                    : 0,
                                eff: slotProps.data[1].months[2].material_cost_1_tire_effective
                                        ? slotProps.data[1].months[2].material_cost_1_tire_effective
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td @click="showContent(slotProps.data[0], 2, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[2].dtc_volum
                                        ? slotProps.data[1].months[2].dtc_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 2, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].dtc
                                    ? slotProps.data[1].months[0].dtc
                                    : 0,
                                eff: slotProps.data[1].months[2].dtc
                                        ? slotProps.data[1].months[2].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                    </template>
                </Column>
                <Column header="Mar" style="min-width: 200px;">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td @click="showContent(slotProps.data[0], 3, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[3].amount_used_eff_volum
                                        ? slotProps.data[1].months[3].amount_used_eff_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 3, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].amount_used_eff
                                    ? slotProps.data[1].months[0].amount_used_eff
                                    : 0,
                                eff: slotProps.data[1].months[3].amount_used_eff
                                        ? slotProps.data[1].months[3].amount_used_eff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td @click="showContent(slotProps.data[0], 3, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[3].totalcoststd_volum
                                        ? slotProps.data[1].months[3].totalcoststd_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 3, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].totalcoststd
                                    ? slotProps.data[1].months[0].totalcoststd
                                    : 0,
                                eff: slotProps.data[1].months[3].totalcoststd
                                        ? slotProps.data[1].months[3].totalcoststd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td @click="showContent(slotProps.data[0], 3, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[3].totalcosteff_volum
                                        ? slotProps.data[1].months[3].totalcosteff_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 3, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].totalcosteff
                                    ? slotProps.data[1].months[0].totalcosteff
                                    : 0,
                                eff: slotProps.data[1].months[3].totalcosteff
                                        ? slotProps.data[1].months[3].totalcosteff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data[0], 3, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[3]
                                        .material_cost_1_tire_standard_volum
                                        ? slotProps.data[1].months[3]
                                            .material_cost_1_tire_standard_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 3, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].material_cost_1_tire_standard
                                    ? slotProps.data[1].months[0].material_cost_1_tire_standard
                                    : 0,
                                eff: slotProps.data[1].months[3].material_cost_1_tire_standard
                                        ? slotProps.data[1].months[3].material_cost_1_tire_standard
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data[0], 3, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[3]
                                        .material_cost_1_tire_effective_volum
                                        ? slotProps.data[1].months[3]
                                            .material_cost_1_tire_effective_volum
                                        : "-"
                                }}
                            </td>

                            <TableRaw @click="showContent(slotProps.data[0], 3, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].material_cost_1_tire_effective
                                    ? slotProps.data[1].months[0].material_cost_1_tire_effective
                                    : 0,
                                eff: slotProps.data[1].months[3].material_cost_1_tire_effective
                                        ? slotProps.data[1].months[3].material_cost_1_tire_effective
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td @click="showContent(slotProps.data[0], 3, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[3].dtc_volum
                                        ? slotProps.data[1].months[3].dtc_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 3, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].dtc
                                    ? slotProps.data[1].months[0].dtc
                                    : 0,
                                eff: slotProps.data[1].months[3].dtc
                                        ? slotProps.data[1].months[3].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                    </template>
                </Column>
                <Column header="Apr" style="min-width: 200px;">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td @click="showContent(slotProps.data[0], 4, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[4].amount_used_eff_volum
                                        ? slotProps.data[1].months[4].amount_used_eff_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 4, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].amount_used_eff
                                    ? slotProps.data[1].months[0].amount_used_eff
                                    : 0,
                                eff: slotProps.data[1].months[4].amount_used_eff
                                        ? slotProps.data[1].months[4].amount_used_eff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td @click="showContent(slotProps.data[0], 4, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[4].totalcoststd_volum
                                        ? slotProps.data[1].months[4].totalcoststd_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 4, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].totalcoststd
                                    ? slotProps.data[1].months[0].totalcoststd
                                    : 0,
                                eff: slotProps.data[1].months[4].totalcoststd
                                        ? slotProps.data[1].months[4].totalcoststd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td @click="showContent(slotProps.data[0], 4, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[4].totalcosteff_volum
                                        ? slotProps.data[1].months[4].totalcosteff_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 4, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].totalcosteff
                                    ? slotProps.data[1].months[0].totalcosteff
                                    : 0,
                                eff: slotProps.data[1].months[4].totalcosteff
                                        ? slotProps.data[1].months[4].totalcosteff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data[0], 4, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[4]
                                        .material_cost_1_tire_standard_volum
                                        ? slotProps.data[1].months[4]
                                            .material_cost_1_tire_standard_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 4, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].material_cost_1_tire_standard
                                    ? slotProps.data[1].months[0].material_cost_1_tire_standard
                                    : 0,
                                eff: slotProps.data[1].months[4].material_cost_1_tire_standard
                                        ? slotProps.data[1].months[4].material_cost_1_tire_standard
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data[0], 4, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[4]
                                        .material_cost_1_tire_effective_volum
                                        ? slotProps.data[1].months[4]
                                            .material_cost_1_tire_effective_volum
                                        : "-"
                                }}
                            </td>

                            <TableRaw @click="showContent(slotProps.data[0], 4, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].material_cost_1_tire_effective
                                    ? slotProps.data[1].months[0].material_cost_1_tire_effective
                                    : 0,
                                eff: slotProps.data[1].months[4].material_cost_1_tire_effective
                                        ? slotProps.data[1].months[4].material_cost_1_tire_effective
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td @click="showContent(slotProps.data[0], 4, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[4].dtc_volum
                                        ? slotProps.data[1].months[4].dtc_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 4, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].dtc
                                    ? slotProps.data[1].months[0].dtc
                                    : 0,
                                eff: slotProps.data[1].months[4].dtc
                                        ? slotProps.data[1].months[4].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                    </template>
                </Column>
                <Column header="May" style="min-width: 200px;">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td @click="showContent(slotProps.data[0], 5, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[5].amount_used_eff_volum
                                        ? slotProps.data[1].months[5].amount_used_eff_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 5, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].amount_used_eff
                                    ? slotProps.data[1].months[0].amount_used_eff
                                    : 0,
                                eff: slotProps.data[1].months[5].amount_used_eff
                                        ? slotProps.data[1].months[5].amount_used_eff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td @click="showContent(slotProps.data[0], 5, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[5].totalcoststd_volum
                                        ? slotProps.data[1].months[5].totalcoststd_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 5, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].totalcoststd
                                    ? slotProps.data[1].months[0].totalcoststd
                                    : 0,
                                eff: slotProps.data[1].months[5].totalcoststd
                                        ? slotProps.data[1].months[5].totalcoststd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td @click="showContent(slotProps.data[0], 5, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[5].totalcosteff_volum
                                        ? slotProps.data[1].months[5].totalcosteff_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 5, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].totalcosteff
                                    ? slotProps.data[1].months[0].totalcosteff
                                    : 0,
                                eff: slotProps.data[1].months[5].totalcosteff
                                        ? slotProps.data[1].months[5].totalcosteff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data[0], 5, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[5]
                                        .material_cost_1_tire_standard_volum
                                        ? slotProps.data[1].months[5]
                                            .material_cost_1_tire_standard_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 5, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].material_cost_1_tire_standard
                                    ? slotProps.data[1].months[0].material_cost_1_tire_standard
                                    : 0,
                                eff: slotProps.data[1].months[5].material_cost_1_tire_standard
                                        ? slotProps.data[1].months[5].material_cost_1_tire_standard
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data[0], 5, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[5]
                                        .material_cost_1_tire_effective_volum
                                        ? slotProps.data[1].months[5]
                                            .material_cost_1_tire_effective_volum
                                        : "-"
                                }}
                            </td>

                            <TableRaw @click="showContent(slotProps.data[0], 5, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].material_cost_1_tire_effective
                                    ? slotProps.data[1].months[0].material_cost_1_tire_effective
                                    : 0,
                                eff: slotProps.data[1].months[5].material_cost_1_tire_effective
                                        ? slotProps.data[1].months[5].material_cost_1_tire_effective
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td @click="showContent(slotProps.data[0], 5, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[5].dtc_volum
                                        ? slotProps.data[1].months[5].dtc_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 5, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].dtc
                                    ? slotProps.data[1].months[0].dtc
                                    : 0,
                                eff: slotProps.data[1].months[5].dtc
                                        ? slotProps.data[1].months[5].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                    </template>
                </Column>
                <Column header="Jun" style="min-width: 200px;">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td @click="showContent(slotProps.data[0], 6, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[6].amount_used_eff_volum
                                        ? slotProps.data[1].months[6].amount_used_eff_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 6, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].amount_used_eff
                                    ? slotProps.data[1].months[0].amount_used_eff
                                    : 0,
                                eff: slotProps.data[1].months[6].amount_used_eff
                                        ? slotProps.data[1].months[6].amount_used_eff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td @click="showContent(slotProps.data[0], 6, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[6].totalcoststd_volum
                                        ? slotProps.data[1].months[6].totalcoststd_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 6, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].totalcoststd
                                    ? slotProps.data[1].months[0].totalcoststd
                                    : 0,
                                eff: slotProps.data[1].months[6].totalcoststd
                                        ? slotProps.data[1].months[6].totalcoststd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td @click="showContent(slotProps.data[0], 6, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[6].totalcosteff_volum
                                        ? slotProps.data[1].months[6].totalcosteff_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 6, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].totalcosteff
                                    ? slotProps.data[1].months[0].totalcosteff
                                    : 0,
                                eff: slotProps.data[1].months[6].totalcosteff
                                        ? slotProps.data[1].months[6].totalcosteff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data[0], 6, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[6]
                                        .material_cost_1_tire_standard_volum
                                        ? slotProps.data[1].months[6]
                                            .material_cost_1_tire_standard_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 6, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].material_cost_1_tire_standard
                                    ? slotProps.data[1].months[0].material_cost_1_tire_standard
                                    : 0,
                                eff: slotProps.data[1].months[6].material_cost_1_tire_standard
                                        ? slotProps.data[1].months[6].material_cost_1_tire_standard
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data[0], 6, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[6]
                                        .material_cost_1_tire_effective_volum
                                        ? slotProps.data[1].months[6]
                                            .material_cost_1_tire_effective_volum
                                        : "-"
                                }}
                            </td>

                            <TableRaw @click="showContent(slotProps.data[0], 6, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].material_cost_1_tire_effective
                                    ? slotProps.data[1].months[0].material_cost_1_tire_effective
                                    : 0,
                                eff: slotProps.data[1].months[6].material_cost_1_tire_effective
                                        ? slotProps.data[1].months[6].material_cost_1_tire_effective
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td @click="showContent(slotProps.data[0], 6, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[6].dtc_volum
                                        ? slotProps.data[1].months[6].dtc_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 6, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].dtc
                                    ? slotProps.data[1].months[0].dtc
                                    : 0,
                                eff: slotProps.data[1].months[6].dtc
                                        ? slotProps.data[1].months[6].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                    </template>
                </Column>
                <Column header="Jul" style="min-width: 200px;">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td @click="showContent(slotProps.data[0], 7, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[7].amount_used_eff_volum
                                        ? slotProps.data[1].months[7].amount_used_eff_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 7, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].amount_used_eff
                                    ? slotProps.data[1].months[0].amount_used_eff
                                    : 0,
                                eff: slotProps.data[1].months[7].amount_used_eff
                                        ? slotProps.data[1].months[7].amount_used_eff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td @click="showContent(slotProps.data[0], 7, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[7].totalcoststd_volum
                                        ? slotProps.data[1].months[7].totalcoststd_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 7, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].totalcoststd
                                    ? slotProps.data[1].months[0].totalcoststd
                                    : 0,
                                eff: slotProps.data[1].months[7].totalcoststd
                                        ? slotProps.data[1].months[7].totalcoststd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td @click="showContent(slotProps.data[0], 7, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[7].totalcosteff_volum
                                        ? slotProps.data[1].months[7].totalcosteff_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 7, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].totalcosteff
                                    ? slotProps.data[1].months[0].totalcosteff
                                    : 0,
                                eff: slotProps.data[1].months[7].totalcosteff
                                        ? slotProps.data[1].months[7].totalcosteff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data[0], 7, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[7]
                                        .material_cost_1_tire_standard_volum
                                        ? slotProps.data[1].months[7]
                                            .material_cost_1_tire_standard_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 7, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].material_cost_1_tire_standard
                                    ? slotProps.data[1].months[0].material_cost_1_tire_standard
                                    : 0,
                                eff: slotProps.data[1].months[7].material_cost_1_tire_standard
                                        ? slotProps.data[1].months[7].material_cost_1_tire_standard
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data[0], 7, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[7]
                                        .material_cost_1_tire_effective_volum
                                        ? slotProps.data[1].months[7]
                                            .material_cost_1_tire_effective_volum
                                        : "-"
                                }}
                            </td>

                            <TableRaw @click="showContent(slotProps.data[0], 7, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].material_cost_1_tire_effective
                                    ? slotProps.data[1].months[0].material_cost_1_tire_effective
                                    : 0,
                                eff: slotProps.data[1].months[7].material_cost_1_tire_effective
                                        ? slotProps.data[1].months[7].material_cost_1_tire_effective
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td @click="showContent(slotProps.data[0], 7, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[7].dtc_volum
                                        ? slotProps.data[1].months[7].dtc_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 7, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].dtc
                                    ? slotProps.data[1].months[0].dtc
                                    : 0,
                                eff: slotProps.data[1].months[7].dtc
                                        ? slotProps.data[1].months[7].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                    </template>
                </Column>
                <Column header="Aug" style="min-width: 200px;">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td @click="showContent(slotProps.data[0], 8, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[8].amount_used_eff_volum
                                        ? slotProps.data[1].months[8].amount_used_eff_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 8, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].amount_used_eff
                                    ? slotProps.data[1].months[0].amount_used_eff
                                    : 0,
                                eff: slotProps.data[1].months[8].amount_used_eff
                                        ? slotProps.data[1].months[8].amount_used_eff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td @click="showContent(slotProps.data[0], 8, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[8].totalcoststd_volum
                                        ? slotProps.data[1].months[8].totalcoststd_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 8, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].totalcoststd
                                    ? slotProps.data[1].months[0].totalcoststd
                                    : 0,
                                eff: slotProps.data[1].months[8].totalcoststd
                                        ? slotProps.data[1].months[8].totalcoststd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td @click="showContent(slotProps.data[0], 8, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[8].totalcosteff_volum
                                        ? slotProps.data[1].months[8].totalcosteff_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 8, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].totalcosteff
                                    ? slotProps.data[1].months[0].totalcosteff
                                    : 0,
                                eff: slotProps.data[1].months[8].totalcosteff
                                        ? slotProps.data[1].months[8].totalcosteff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data[0], 8, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[8]
                                        .material_cost_1_tire_standard_volum
                                        ? slotProps.data[1].months[8]
                                            .material_cost_1_tire_standard_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 8, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].material_cost_1_tire_standard
                                    ? slotProps.data[1].months[0].material_cost_1_tire_standard
                                    : 0,
                                eff: slotProps.data[1].months[8].material_cost_1_tire_standard
                                        ? slotProps.data[1].months[8].material_cost_1_tire_standard
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data[0], 8, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[8]
                                        .material_cost_1_tire_effective_volum
                                        ? slotProps.data[1].months[8]
                                            .material_cost_1_tire_effective_volum
                                        : "-"
                                }}
                            </td>

                            <TableRaw @click="showContent(slotProps.data[0], 8, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].material_cost_1_tire_effective
                                    ? slotProps.data[1].months[0].material_cost_1_tire_effective
                                    : 0,
                                eff: slotProps.data[1].months[8].material_cost_1_tire_effective
                                        ? slotProps.data[1].months[8].material_cost_1_tire_effective
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td @click="showContent(slotProps.data[0], 8, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[8].dtc_volum
                                        ? slotProps.data[1].months[8].dtc_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 8, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].dtc
                                    ? slotProps.data[1].months[0].dtc
                                    : 0,
                                eff: slotProps.data[1].months[8].dtc
                                        ? slotProps.data[1].months[8].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                    </template>
                </Column>
                <Column header="Set" style="min-width: 200px;">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td @click="showContent(slotProps.data[0], 9, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[9].amount_used_eff_volum
                                        ? slotProps.data[1].months[9].amount_used_eff_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 9, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].amount_used_eff
                                    ? slotProps.data[1].months[0].amount_used_eff
                                    : 0,
                                eff: slotProps.data[1].months[9].amount_used_eff
                                        ? slotProps.data[1].months[9].amount_used_eff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td @click="showContent(slotProps.data[0], 9, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[9].totalcoststd_volum
                                        ? slotProps.data[1].months[9].totalcoststd_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 9, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].totalcoststd
                                    ? slotProps.data[1].months[0].totalcoststd
                                    : 0,
                                eff: slotProps.data[1].months[9].totalcoststd
                                        ? slotProps.data[1].months[9].totalcoststd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td @click="showContent(slotProps.data[0], 9, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[9].totalcosteff_volum
                                        ? slotProps.data[1].months[9].totalcosteff_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 9, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].totalcosteff
                                    ? slotProps.data[1].months[0].totalcosteff
                                    : 0,
                                eff: slotProps.data[1].months[9].totalcosteff
                                        ? slotProps.data[1].months[9].totalcosteff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data[0], 9, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[9]
                                        .material_cost_1_tire_standard_volum
                                        ? slotProps.data[1].months[9]
                                            .material_cost_1_tire_standard_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 9, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].material_cost_1_tire_standard
                                    ? slotProps.data[1].months[0].material_cost_1_tire_standard
                                    : 0,
                                eff: slotProps.data[1].months[9].material_cost_1_tire_standard
                                        ? slotProps.data[1].months[9].material_cost_1_tire_standard
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data[0], 9, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[9]
                                        .material_cost_1_tire_effective_volum
                                        ? slotProps.data[1].months[9]
                                            .material_cost_1_tire_effective_volum
                                        : "-"
                                }}
                            </td>

                            <TableRaw @click="showContent(slotProps.data[0], 9, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].material_cost_1_tire_effective
                                    ? slotProps.data[1].months[0].material_cost_1_tire_effective
                                    : 0,
                                eff: slotProps.data[1].months[9].material_cost_1_tire_effective
                                        ? slotProps.data[1].months[9].material_cost_1_tire_effective
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td @click="showContent(slotProps.data[0], 9, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[9].dtc_volum
                                        ? slotProps.data[1].months[9].dtc_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 9, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].dtc
                                    ? slotProps.data[1].months[0].dtc
                                    : 0,
                                eff: slotProps.data[1].months[9].dtc
                                        ? slotProps.data[1].months[9].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                    </template>
                </Column>
                <Column header="Out" style="min-width: 200px;">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td @click="showContent(slotProps.data[0], 10, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[10].amount_used_eff_volum
                                        ? slotProps.data[1].months[10].amount_used_eff_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 10, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].amount_used_eff
                                    ? slotProps.data[1].months[0].amount_used_eff
                                    : 0,
                                eff: slotProps.data[1].months[10].amount_used_eff
                                        ? slotProps.data[1].months[10].amount_used_eff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td @click="showContent(slotProps.data[0], 10, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[10].totalcoststd_volum
                                        ? slotProps.data[1].months[10].totalcoststd_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 10, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].totalcoststd
                                    ? slotProps.data[1].months[0].totalcoststd
                                    : 0,
                                eff: slotProps.data[1].months[10].totalcoststd
                                        ? slotProps.data[1].months[10].totalcoststd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td @click="showContent(slotProps.data[0], 10, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[10].totalcosteff_volum
                                        ? slotProps.data[1].months[10].totalcosteff_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 10, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].totalcosteff
                                    ? slotProps.data[1].months[0].totalcosteff
                                    : 0,
                                eff: slotProps.data[1].months[10].totalcosteff
                                        ? slotProps.data[1].months[10].totalcosteff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data[0], 10, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[10]
                                        .material_cost_1_tire_standard_volum
                                        ? slotProps.data[1].months[10]
                                            .material_cost_1_tire_standard_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 10, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].material_cost_1_tire_standard
                                    ? slotProps.data[1].months[0].material_cost_1_tire_standard
                                    : 0,
                                eff: slotProps.data[1].months[10].material_cost_1_tire_standard
                                        ? slotProps.data[1].months[10].material_cost_1_tire_standard
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data[0], 10, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[10]
                                        .material_cost_1_tire_effective_volum
                                        ? slotProps.data[1].months[10]
                                            .material_cost_1_tire_effective_volum
                                        : "-"
                                }}
                            </td>

                            <TableRaw @click="showContent(slotProps.data[0], 10, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].material_cost_1_tire_effective
                                    ? slotProps.data[1].months[0].material_cost_1_tire_effective
                                    : 0,
                                eff: slotProps.data[1].months[10].material_cost_1_tire_effective
                                        ? slotProps.data[1].months[10].material_cost_1_tire_effective
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td @click="showContent(slotProps.data[0], 10, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[10].dtc_volum
                                        ? slotProps.data[1].months[10].dtc_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 10, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].dtc
                                    ? slotProps.data[1].months[0].dtc
                                    : 0,
                                eff: slotProps.data[1].months[10].dtc
                                        ? slotProps.data[1].months[10].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                    </template>
                </Column>
                <Column header="Nov" style="min-width: 200px;">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td @click="showContent(slotProps.data[0], 11, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[11].amount_used_eff_volum
                                        ? slotProps.data[1].months[11].amount_used_eff_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 11, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].amount_used_eff
                                    ? slotProps.data[1].months[0].amount_used_eff
                                    : 0,
                                eff: slotProps.data[1].months[11].amount_used_eff
                                        ? slotProps.data[1].months[11].amount_used_eff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td @click="showContent(slotProps.data[0], 11, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[11].totalcoststd_volum
                                        ? slotProps.data[1].months[11].totalcoststd_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 11, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].totalcoststd
                                    ? slotProps.data[1].months[0].totalcoststd
                                    : 0,
                                eff: slotProps.data[1].months[11].totalcoststd
                                        ? slotProps.data[1].months[11].totalcoststd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td @click="showContent(slotProps.data[0], 11, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[11].totalcosteff_volum
                                        ? slotProps.data[1].months[11].totalcosteff_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 11, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].totalcosteff
                                    ? slotProps.data[1].months[0].totalcosteff
                                    : 0,
                                eff: slotProps.data[1].months[11].totalcosteff
                                        ? slotProps.data[1].months[11].totalcosteff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data[0], 11, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[11]
                                        .material_cost_1_tire_standard_volum
                                        ? slotProps.data[1].months[11]
                                            .material_cost_1_tire_standard_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 11, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].material_cost_1_tire_standard
                                    ? slotProps.data[1].months[0].material_cost_1_tire_standard
                                    : 0,
                                eff: slotProps.data[1].months[11].material_cost_1_tire_standard
                                        ? slotProps.data[1].months[11].material_cost_1_tire_standard
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data[0], 11, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[11]
                                        .material_cost_1_tire_effective_volum
                                        ? slotProps.data[1].months[11]
                                            .material_cost_1_tire_effective_volum
                                        : "-"
                                }}
                            </td>

                            <TableRaw @click="showContent(slotProps.data[0], 11, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].material_cost_1_tire_effective
                                    ? slotProps.data[1].months[0].material_cost_1_tire_effective
                                    : 0,
                                eff: slotProps.data[1].months[11].material_cost_1_tire_effective
                                        ? slotProps.data[1].months[11].material_cost_1_tire_effective
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td @click="showContent(slotProps.data[0], 11, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[11].dtc_volum
                                        ? slotProps.data[1].months[11].dtc_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 11, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].dtc
                                    ? slotProps.data[1].months[0].dtc
                                    : 0,
                                eff: slotProps.data[1].months[11].dtc
                                        ? slotProps.data[1].months[11].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                    </template>
                </Column>
                <Column header="Dez" style="min-width: 200px;">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td @click="showContent(slotProps.data[0], 12, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[12].amount_used_eff_volum
                                        ? slotProps.data[1].months[12].amount_used_eff_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 12, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].amount_used_eff
                                    ? slotProps.data[1].months[0].amount_used_eff
                                    : 0,
                                eff: slotProps.data[1].months[12].amount_used_eff
                                        ? slotProps.data[1].months[12].amount_used_eff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td @click="showContent(slotProps.data[0], 12, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[12].totalcoststd_volum
                                        ? slotProps.data[1].months[12].totalcoststd_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 12, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].totalcoststd
                                    ? slotProps.data[1].months[0].totalcoststd
                                    : 0,
                                eff: slotProps.data[1].months[12].totalcoststd
                                        ? slotProps.data[1].months[12].totalcoststd
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td @click="showContent(slotProps.data[0], 12, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[12].totalcosteff_volum
                                        ? slotProps.data[1].months[12].totalcosteff_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 12, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].totalcosteff
                                    ? slotProps.data[1].months[0].totalcosteff
                                    : 0,
                                eff: slotProps.data[1].months[12].totalcosteff
                                        ? slotProps.data[1].months[12].totalcosteff
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data[0], 12, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[12]
                                        .material_cost_1_tire_standard_volum
                                        ? slotProps.data[1].months[12]
                                            .material_cost_1_tire_standard_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 12, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].material_cost_1_tire_standard
                                    ? slotProps.data[1].months[0].material_cost_1_tire_standard
                                    : 0,
                                eff: slotProps.data[1].months[12].material_cost_1_tire_standard
                                        ? slotProps.data[1].months[12].material_cost_1_tire_standard
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data[0], 12, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[12]
                                        .material_cost_1_tire_effective_volum
                                        ? slotProps.data[1].months[12]
                                            .material_cost_1_tire_effective_volum
                                        : "-"
                                }}
                            </td>

                            <TableRaw @click="showContent(slotProps.data[0], 12, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].material_cost_1_tire_effective
                                    ? slotProps.data[1].months[0].material_cost_1_tire_effective
                                    : 0,
                                eff: slotProps.data[1].months[12].material_cost_1_tire_effective
                                        ? slotProps.data[1].months[12].material_cost_1_tire_effective
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                        <tr>
                            <td @click="showContent(slotProps.data[0], 12, 0)" v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[12].dtc_volum
                                        ? slotProps.data[1].months[12].dtc_volum
                                        : "-"
                                }}
                            </td>
                            <TableRaw @click="showContent(slotProps.data[0], 12, 0)" v-else :value="{
                                std: slotProps.data[1].months[0].dtc
                                    ? slotProps.data[1].months[0].dtc
                                    : 0,
                                eff: slotProps.data[1].months[12].dtc
                                        ? slotProps.data[1].months[12].dtc
                                    : 0,
                            }">
                            </TableRaw>
                        </tr>
                    </template>
                </Column>
                <Column header="Year" style="min-width: 200px;">
                    <template #body="slotProps">
                        <tr v-if="showAmount">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[14].amount_in_tire_kg_volum
                                        ? slotProps.data[1].months[14].amount_in_tire_kg_volum
                                        : "-"
                                }}
                            </td>
                            <td v-else>
                                {{
                                    slotProps.data[1].months[13].totalAmount
                                        ? slotProps.data[1].months[13].totalAmount
                                        : "-"
                                }}
                            </td>
                        </tr>
                        <tr v-if="showMatCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[14].totalcoststd_volum
                                        ? slotProps.data[1].months[14].totalcoststd_volum
                                        : "-"
                                }}
                            </td>
                            <td v-else>
                                {{
                                    slotProps.data[1].months[13].totalCostStd
                                        ? slotProps.data[1].months[13].totalCostStd
                                        : "-"
                                }}
                            </td>
                        </tr>
                        <tr v-if="showMatCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[14].totalcosteff_volum
                                        ? slotProps.data[1].months[14].totalcosteff_volum
                                        : "-"
                                }}
                            </td>
                            <td v-else>
                                {{
                                    slotProps.data[1].months[13].totalCostEff
                                        ? slotProps.data[1].months[13].totalCostEff
                                        : "-"
                                }}
                            </td>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[14]
                                        .material_cost_1_tire_standard_volum
                                        ? slotProps.data[1].months[14]
                                            .material_cost_1_tire_standard_volum
                                        : "-"
                                }}
                            </td>
                            <td v-else>
                                {{
                                    slotProps.data[1].months[13].totalStd
                                        ? slotProps.data[1].months[13].totalStd
                                        : "-"
                                }}
                            </td>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[14]
                                        .material_cost_1_tire_effective_volum
                                        ? slotProps.data[1].months[14]
                                            .material_cost_1_tire_effective_volum
                                        : "-"
                                }}
                            </td>
                            <td v-else>
                                {{
                                    slotProps.data[1].months[13].totalEff
                                        ? slotProps.data[1].months[13].totalEff
                                        : "-"
                                }}
                            </td>
                        </tr>
                        <tr>
                            <td v-if="showTotalValue">
                                {{
                                    slotProps.data[1].months[14].dtc_volum
                                        ? slotProps.data[1].months[14].dtc_volum
                                        : "-"
                                }}
                            </td>
                            <td v-else>
                                {{
                                    slotProps.data[1].months[13].totalDtc
                                        ? slotProps.data[1].months[13].totalDtc
                                        : "-"
                                }}
                            </td>
                        </tr>
                    </template>
                </Column>
            </DataTable>
        </div>
        <Toast />
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
                                    <td>{{ slotProps.data.card.totalCostStd }}</td>
                                </tr>
                                <tr>
                                    <td>Total Cost Eff</td>
                                    <td>{{ slotProps.data.card.totalCostEff }}</td>
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
                                    <td>{{ slotProps.data.card.costPerKgStd }}</td>
                                </tr>
                                <tr>
                                    <td>Cost per KG Eff</td>
                                    <td>{{ slotProps.data.card.costPerKgEff }}</td>
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
                                    <td>{{ slotProps.data.card.costPerLiterStd }}</td>
                                </tr>
                                <tr>
                                    <td>Cost per Liter Eff</td>
                                    <td>{{ slotProps.data.card.costPerLiterEff }}</td>
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
                                    <td>{{ slotProps.data.card.totalRawMaterials }}</td>
                                </tr>
                                <tr>
                                    <td>Density</td>
                                    <td>{{ slotProps.data.card.density }}</td>
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
                                
                            <Dropdown optionLabel="text" v-model="recycleFilter" placeholder="Precission value"
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
                            <td>{{ el.cost_per_unit_std }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Cost per Unit (EFF)">
                    <template #body="slotProps">
                        <tr v-for="(el, index) in slotProps.data.table" :key="index">
                            <td>{{ el.cost_per_unit_eff }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Raw Weight">
                    <template #body="slotProps">
                        <tr v-for="(el, index) in slotProps.data.table" :key="index">
                            <td>{{ el.raw_weight }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Raw Weight %">
                    <template #body="slotProps">
                        <tr v-for="(el, index) in slotProps.data.table" :key="index">
                            <td>{{ el.raw_weight_percent }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Total Cost (STD)">
                    <template #body="slotProps">
                        <tr v-for="(el, index) in slotProps.data.table" :key="index">
                            <td>{{ el.total_cost_std }}</td>
                        </tr>
                    </template>
                </Column>
                <Column header="Total Cost (EFF)">
                    <template #body="slotProps">
                        <tr v-for="(el, index) in slotProps.data.table" :key="index">
                            <td>{{ el.total_cost_eff }}</td>
                        </tr>
                    </template>
                </Column>
            </DataTable>
        </Dialog>
    </div>
</template>
<script setup>
import Dropdown from "primevue/dropdown";
import Card from "primevue/card";
import Dialog from "primevue/dialog";
import Column from "primevue/column";
import ProgressSpinner from "primevue/progressspinner";
import InputSwitch from "primevue/inputswitch";
import axios from "axios";
import Toast from "primevue/toast";
import { useToast } from "primevue/usetoast";
import { useDtcStore } from "../../store/dtc";
import { FilterMatchMode } from "primevue/api";
import { ref, onMounted, toRaw  } from "vue";
import TableRaw from "@/layout/components/arrow-table/index.vue";
import Chart from 'primevue/chart';

const display = ref(false);
const dt = ref();
const dtc = useDtcStore();
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
const progress = ref(false);
const toast = useToast();
const showTotalValue = ref(false);
const showAmount = ref(true);
const showMatCostStd = ref(false);
const showMatCostEff = ref(false);
const showTotalCostStd = ref(true);
const showTotalCostEff = ref(true);
let modalTable = ref([]);
let mat = ref("");
let month = ref(0);
let recycleFilter = ref(0)
let modalPlant = ref("")
let modalYear = ref()
let datasets = ref([]);
let items_totais = ref([]);
let items_materials = ref([]);
let volumTotals = ref([]);
let graphselected = ref({ value: 1, text: 'Total' });
const volumTotais = ref([]);
const graph = ref([
        { value: 1, text: 'Total' },
        { value: 2, text: 'Total Value' },
        { value: 3, text: 'DTC' },
        { value: 4, text: 'Total Weight Std' },
        { value: 5, text: 'Cost Std' },
        { value: 6, text: 'Cost Eff' },
        ]);

const showContent = async (rawMaterial, mo) => {
    modalTable.value = []
    display.value = true;
    mat.value = rawMaterial;
    month.value = mo;
    modalPlant = plantSelected.value.value
    modalYear = year.value
    const response = await axios.get(
        "http://localhost:8000/api/v1/report_raw_material_breakdown/?plant=" +
        plantSelected.value.value +
        "&product=" +
        mat.value +
        "&filter=" +
        recycleFilter.value +
        "&month=" +
        month.value +
        "&year=" +
        year.value
    );
    modalTable.value = response.data;
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
    console.log(modalTable.value);
};

const exportCSV = () => {
    dt.value.exportCSV();
};
const changeGra = () => {
      const itens = toRaw(items_totais); 
      console.log(itens)
      let changedData = volumTotais.value.volum
      if (graphselected.value.value === 2) {
        changedData = volumTotais.value.value
      }
      if (graphselected.value.value === 3) {
        var dtc = []
        for (var i = 0; i <= 13; i++) {
          dtc.push(itens[0].values[i].dtc)
        }
        console.log(dtc)
        changedData = dtc
      }
      if (graphselected.value.value === 4) {
        var totalWeightStd = []
        for (var j = 0; j <= 13; j++) {
          totalWeightStd.push(itens[0].values[j].totalWeightStd)
        }
        console.log(totalWeightStd)
        changedData = totalWeightStd
      }
      if (graphselected.value.value === 5) {
        var totalCostStd = []
        for (var k = 0; k <= 13; k++) {
          totalCostStd.push(itens[0].values[k].totalCostStd)
        }
        console.log(totalCostStd)
        changedData = totalCostStd
      }
      if (graphselected.value.value === 6) {
        var totalCostEff = []
        for (var p = 0; p <= 13; p++) {
          totalCostEff.push(itens[0].values[p].totalCostEff)
        }
        console.log(totalCostEff)
        changedData = totalCostEff
      }
      datasets.value = {
                labels: ['Standard', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'Algust', 'September', 'October', 'November', 'December'],
                datasets: [
                    {
                        label: graphselected.value.text,
                        data: changedData,
                        fill: false,
                        borderColor: '#42A5F5',
                        tension: .4
                    }
                ]
            }
};
const filters = ref({
    global: { value: null, matchMode: FilterMatchMode.CONTAINS },
});
const getPlant = async () => {
    plant.value = await dtc.setPlant();
};
const getMkg = async () => {
    await dtc.setMkg();
    mkg.value = dtc.mkg;
    line.value = dtc.line;
};
const getLine = async () => {
    await dtc.setLine();
    line.value = dtc.line;
};
const getTire = async () => {
    await dtc.setTires();
    tire.value = dtc.tires;
};


const submit = async () => {
    progress.value = true;
    if (plantSelected.value.value === undefined) {
        plantSelected.value.value = "";
    }
    const response = await axios.get(
        "http://localhost:8000/api/v1/product_one_level/?plant=" +
        plantSelected.value.value +
        "&product=" +
        tireSelected.value.value +
        "&market_segment=" +
        mkgSelected.value.value +
        "&year=" +
        year.value +
        "&line=" +
        lineSelected
    );
    response.data.items;
    const entries = Object.entries(response.data.items);
    const items = [];
    const materials = [];

    const volums = ref([]);
    const totais = ref([
        { name: "Total", isTotal: "total", values: [] },
        { name: "Total", isTotal: "volum", values: [] },
    ]);

    // console.log(totais.value[0].values);
    volumTotais.value = response.data.volumTotais;
    volums.value = response.data.volumTotais.volum;
    table.value = entries;
    toast.add({
        severity: "success",
        summary: "Atualizado conforme solicitado",
        detail: "Permissoes atualizadas para a regra",
        life: 3000,
    });
    table.value.forEach((el, index) => {
        let amount_used_eff = 0;
        let total_cost_std = 0;
        let total_cost_eff = 0;
        let cost_std = 0;
        let cost_eff = 0;
        let dtc = 0;
        el[1].months.forEach((ele, ind) => {
            amount_used_eff =
                (ele.amount_used_std ? ele.amount_used_std : 0) + amount_used_eff;
            total_cost_std =
                (ele.totalcoststd ? ele.totalcoststd : 0) + total_cost_std;
            total_cost_eff =
                (ele.totalcosteff ? ele.totalcosteff : 0) + total_cost_eff;
            cost_std =
                (ele.material_cost_1_tire_standard
                    ? ele.material_cost_1_tire_standard
                    : 0) + cost_std;
            cost_eff =
                (ele.material_cost_1_tire_effective
                    ? ele.material_cost_1_tire_effective
                    : 0) + cost_eff;
            dtc = (ele.dtc_volum ? ele.dtc_volum : 0) + dtc;
        });
        el[1].months.push({
            totalAmount: amount_used_eff,
            totalCostStd: total_cost_std,
            totalCostEff: total_cost_eff,
            totalStd: cost_std,
            totalEff: cost_eff,
            totalDtc: dtc,
        });
    });

    let totalVolum = 0;
    for (var i = 0; i <= 13; i++) {
        totalVolum += volums.value[i] ?? 0;
        totais.value[0].values.push({
            totalWeightStd: 0,
            materialCostStd: 0,
            materialCostEff: 0,
            totalCostEff: 0,
            totalCostStd: 0,
            dtc: 0,
            volum: i < 13 ? volums.value[i] : totalVolum,
        });
        totais.value[1].values.push({
            totalWeightStd: 0,
            materialCostStd: 0,
            materialCostEff: 0,
            totalCostEff: 0,
            totalCostStd: 0,
            dtc: 0,
            volum: i < 13 ? volums.value[i] : totalVolum,
        });
    }

    table.value.forEach((el, index) => {
        const item = el[1];

        const year = {
            amount_used_std: 0,
            amount_in_tire_kg: 0,
            totalcoststd: 0,
            totalcosteff: 0,
            material_cost_1_tire_effective: 0,
            material_cost_1_tire_standard: 0,
            dtc: 0,
            amount_used_std_volum: 0,
            amount_in_tire_kg_volum: 0,
            totalcoststd_volum: 0,
            totalcosteff_volum: 0,
            material_cost_1_tire_effective_volum: 0,
            material_cost_1_tire_standard_volum: 0,
            dtc_volum: 0,
        };

        for (var aux = 0; aux <= 12; aux++) {
            if (item.months[aux]) {
                totais.value[0].values[aux].totalWeightStd += item.months[aux]
                    .amount_in_tire_kg
                    ? item.months[aux].amount_in_tire_kg
                    : 0;
                totais.value[0].values[aux].materialCostStd += item.months[aux]
                    .totalcoststd
                    ? item.months[aux].totalcoststd
                    : 0;
                totais.value[0].values[aux].materialCostEff += item.months[aux]
                    .totalcosteff
                    ? item.months[aux].totalcosteff
                    : 0;
                totais.value[0].values[aux].totalCostEff += item.months[aux]
                    .material_cost_1_tire_effective
                    ? item.months[aux].material_cost_1_tire_effective
                    : 0;
                totais.value[0].values[aux].totalCostStd += item.months[aux]
                    .material_cost_1_tire_standard
                    ? item.months[aux].material_cost_1_tire_standard
                    : 0;
                totais.value[0].values[aux].dtc += item.months[aux].dtc
                    ? item.months[aux].dtc
                    : 0;
                totais.value[1].values[aux].totalWeightStd += item.months[aux]
                    .amount_in_tire_kg
                    ? item.months[aux].amount_in_tire_kg
                    : 0;
                totais.value[1].values[aux].materialCostStd += item.months[aux]
                    .totalcoststd
                    ? item.months[aux].totalcoststd
                    : 0;
                totais.value[1].values[aux].materialCostEff += item.months[aux]
                    .totalcosteff
                    ? item.months[aux].totalcosteff
                    : 0;
                totais.value[1].values[aux].totalCostEff += item.months[aux]
                    .material_cost_1_tire_effective
                    ? item.months[aux].material_cost_1_tire_effective
                    : 0;
                totais.value[1].values[aux].totalCostStd += item.months[aux]
                    .material_cost_1_tire_standard
                    ? item.months[aux].material_cost_1_tire_standard
                    : 0;
                totais.value[1].values[aux].dtc += item.months[aux].dtc_volum
                    ? item.months[aux].dtc_volum
                    : 0;
                if (aux > 0) {
                    totais.value[0].values[13].totalWeightStd += item.months[aux]
                        .amount_in_tire_kg
                        ? item.months[aux].amount_in_tire_kg
                        : 0;
                    totais.value[0].values[13].materialCostStd += item.months[aux]
                        .totalcoststd
                        ? item.months[aux].totalcoststd
                        : 0;
                    totais.value[0].values[13].materialCostEff += item.months[aux]
                        .totalcosteff
                        ? item.months[aux].totalcosteff
                        : 0;
                    totais.value[0].values[13].totalCostEff += item.months[aux]
                        .material_cost_1_tire_effective
                        ? item.months[aux].material_cost_1_tire_effective
                        : 0;
                    totais.value[0].values[13].totalCostStd += item.months[aux]
                        .material_cost_1_tire_standard
                        ? item.months[aux].material_cost_1_tire_standard
                        : 0;
                    totais.value[0].values[13].dtc += item.months[aux].dtc
                        ? item.months[aux].dtc
                        : 0;
                    totais.value[1].values[13].totalWeightStd += item.months[aux]
                        .amount_in_tire_kg
                        ? item.months[aux].amount_in_tire_kg
                        : 0;
                    totais.value[1].values[13].materialCostStd += item.months[aux]
                        .totalcoststd
                        ? item.months[aux].totalcoststd
                        : 0;
                    totais.value[1].values[13].materialCostEff += item.months[aux]
                        .totalcosteff
                        ? item.months[aux].totalcosteff
                        : 0;
                    totais.value[1].values[13].totalCostEff += item.months[aux]
                        .material_cost_1_tire_effective
                        ? item.months[aux].material_cost_1_tire_effective
                        : 0;
                    totais.value[1].values[13].totalCostStd += item.months[aux]
                        .material_cost_1_tire_standard
                        ? item.months[aux].material_cost_1_tire_standard
                        : 0;
                    totais.value[1].values[13].dtc += item.months[aux].dtc_volum
                        ? item.months[aux].dtc_volum
                        : 0;
                    year.amount_used_std += item.months[aux].amount_used_std
                        ? item.months[aux].amount_used_std
                        : 0;
                    year.amount_in_tire_kg += item.months[aux].amount_in_tire_kg
                        ? item.months[aux].amount_in_tire_kg
                        : 0;
                    year.totalcoststd += item.months[aux].totalcoststd
                        ? item.months[aux].totalcoststd
                        : 0;
                    year.totalcosteff += item.months[aux].totalcosteff
                        ? item.months[aux].totalcosteff
                        : 0;
                    year.material_cost_1_tire_effective += item.months[aux]
                        .material_cost_1_tire_effective
                        ? item.months[aux].material_cost_1_tire_effective
                        : 0;
                    year.material_cost_1_tire_standard += item.months[aux]
                        .material_cost_1_tire_standard
                        ? item.months[aux].material_cost_1_tire_standard
                        : 0;
                    year.dtc += item.months[aux].dtc ? item.months[aux].dtc : 0;
                    year.amount_used_std_volum += item.months[aux].amount_used_std_volum
                        ? item.months[aux].amount_used_std_volum
                        : 0;
                    year.amount_in_tire_kg_volum += item.months[aux]
                        .amount_in_tire_kg_volum
                        ? item.months[aux].amount_in_tire_kg_volum
                        : 0;
                    year.totalcoststd_volum += item.months[aux].totalcoststd_volum
                        ? item.months[aux].totalcoststd_volum
                        : 0;
                    year.totalcosteff_volum += item.months[aux].totalcosteff_volum
                        ? item.months[aux].totalcosteff_volum
                        : 0;
                    year.material_cost_1_tire_effective_volum += item.months[aux]
                        .material_cost_1_tire_effective_volum
                        ? item.months[aux].material_cost_1_tire_effective_volum
                        : 0;
                    year.material_cost_1_tire_standard_volum += item.months[aux]
                        .material_cost_1_tire_standard_volum
                        ? item.months[aux].material_cost_1_tire_standard_volum
                        : 0;
                    year.dtc_volum += item.months[aux].dtc_volum
                        ? item.months[aux].dtc_volum
                        : 0;
                }
            }
        }

        const values = item.months;
        values.push(year);

        materials.push({
            name: el[1].mat_me,
            mat_me: item.mat_me,
            type: item.type,
            values: values,
        });
    });
    items_materials = materials;
    items_totais = totais.value;
    volumTotals = volumTotais.value;
    // console.log(table.value) 
    changeGra()   
    progress.value = false;

};
onMounted(async () => {
    getPlant();
    getMkg();
    getLine();
    getTire();
    const d = new Date();
    year.value = d.getFullYear();
});
</script>
<style>
.p-dialog-mask.p-component-overlay.p-component-overlay-enter {
    z-index: 999 !important;
}
</style>