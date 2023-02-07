<template>
    <h3>Product-Raw Material</h3>
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
        
    </div>
    <div class="col-12">
            <DataTable :value="total" responsiveLayout="scroll">
            <Column :header="$t('dtc.values')" style="min-width: 150px;">
                <template #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <td>Total Materials</td>
                    </tr>
                    <tr v-if="showCostStd">
                        <td>Cost per Unit Std</td>
                    </tr>
                    <tr v-if="showCostEff">
                        <td>Cost per Unit Eff</td>
                    </tr>
                    <tr v-if="showRawWeight">
                        <td>Raw Weight</td>
                    </tr>
                    <tr>
                        <td>Total Cost Std</td>
                    </tr>
                    <tr>
                        <td>Total Cost Eff</td>
                    </tr>
                </template>
            </Column>
            <Column header="Standard">
                <template #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <td>{{(slotProps.data.tm[0]).toFixed(fixed.value)}}</td>
                    </tr>
                    <tr v-if="showCostStd">
                        <td>{{(slotProps.data.coststd[0]).toFixed(fixed.value)}}</td>
                    </tr>
                    <tr v-if="showCostEff">
                        <td>{{(slotProps.data.costeff[0]).toFixed(fixed.value)}}</td>
                    </tr>
                    <tr v-if="showRawWeight">
                        <td>{{(slotProps.data.raw[0]).toFixed(fixed.value)}}</td>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <td>{{(slotProps.data.totalstd[0]).toFixed(fixed.value)}}</td>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <td>{{(slotProps.data.totaleff[0]).toFixed(fixed.value)}}</td>
                    </tr>
                </template>
            </Column>
            <Column header="Jan" style="min-width: 200px">
                <template #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.tm[0] || slotProps.data.tm[0] != '-' ? slotProps.data.tm[0] : 0),
                                eff: (slotProps.data.tm[1] || slotProps.data.tm[1] != '-' ? (slotProps.data.tm[1]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showCostStd">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.coststd[0] || slotProps.data.coststd[0] != '-' ? slotProps.data.coststd[0] : 0),
                                eff: (slotProps.data.coststd[1] || slotProps.data.coststd[1] != '-' ? (slotProps.data.coststd[1]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showCostEff">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.costeff[0] || slotProps.data.costeff[0] != '-' ? slotProps.data.costeff[0] : 0),
                                eff: (slotProps.data.costeff[1] || slotProps.data.costeff[1] != '-' ? (slotProps.data.costeff[1]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showRawWeight">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.raw[0] || slotProps.data.raw[0] != '-' ? slotProps.data.raw[0] : 0),
                                eff: (slotProps.data.raw[1] || slotProps.data.raw[1] != '-' ? (slotProps.data.raw[1]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.totalstd[0] || slotProps.data.totalstd[0] != '-' ? slotProps.data.totalstd[0] : 0),
                                eff: (slotProps.data.totalstd[1] || slotProps.data.totalstd[1] != '-' ? (slotProps.data.totalstd[1]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.totaleff[0] || slotProps.data.totaleff[0] != '-' ? slotProps.data.totaleff[0] : 0),
                                eff: (slotProps.data.totaleff[1] || slotProps.data.totaleff[1] != '-' ? (slotProps.data.totaleff[1]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                </template>
            </Column>
            <Column header="Feb" style="min-width: 200px">
                <template #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.tm[0] || slotProps.data.tm[0] != '-' ? slotProps.data.tm[0] : 0),
                                eff: (slotProps.data.tm[2] || slotProps.data.tm[2] != '-' ? (slotProps.data.tm[2]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showCostStd">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.coststd[0] || slotProps.data.coststd[0] != '-' ? slotProps.data.coststd[0] : 0),
                                eff: (slotProps.data.coststd[2] || slotProps.data.coststd[2] != '-' ? (slotProps.data.coststd[2]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showCostEff">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.costeff[0] || slotProps.data.costeff[0] != '-' ? slotProps.data.costeff[0] : 0),
                                eff: (slotProps.data.costeff[2] || slotProps.data.costeff[2] != '-' ? (slotProps.data.costeff[2]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showRawWeight">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.raw[0] || slotProps.data.raw[0] != '-' ? slotProps.data.raw[0] : 0),
                                eff: (slotProps.data.raw[2] || slotProps.data.raw[2] != '-' ? (slotProps.data.raw[2]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.totalstd[0] || slotProps.data.totalstd[0] != '-' ? slotProps.data.totalstd[0] : 0),
                                eff: (slotProps.data.totalstd[2] || slotProps.data.totalstd[2] != '-' ? (slotProps.data.totalstd[2]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.totaleff[0] || slotProps.data.totaleff[0] != '-' ? slotProps.data.totaleff[0] : 0),
                                eff: (slotProps.data.totaleff[2] || slotProps.data.totaleff[2] != '-' ? (slotProps.data.totaleff[2]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                </template>
            </Column>
            <Column header="Mar" style="min-width: 200px">
                <template #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.tm[0] || slotProps.data.tm[0] != '-' ? slotProps.data.tm[0] : 0),
                                eff: (slotProps.data.tm[3] || slotProps.data.tm[3] != '-' ? (slotProps.data.tm[3]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showCostStd">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.coststd[0] || slotProps.data.coststd[0] != '-' ? slotProps.data.coststd[0] : 0),
                                eff: (slotProps.data.coststd[3] || slotProps.data.coststd[3] != '-' ? (slotProps.data.coststd[3]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showCostEff">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.costeff[0] || slotProps.data.costeff[0] != '-' ? slotProps.data.costeff[0] : 0),
                                eff: (slotProps.data.costeff[3] || slotProps.data.costeff[3] != '-' ? (slotProps.data.costeff[3]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showRawWeight">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.raw[0] || slotProps.data.raw[0] != '-' ? slotProps.data.raw[0] : 0),
                                eff: (slotProps.data.raw[3] || slotProps.data.raw[3] != '-' ? (slotProps.data.raw[3]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.totalstd[0] || slotProps.data.totalstd[0] != '-' ? slotProps.data.totalstd[0] : 0),
                                eff: (slotProps.data.totalstd[3] || slotProps.data.totalstd[3] != '-' ? (slotProps.data.totalstd[3]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.totaleff[0] || slotProps.data.totaleff[0] != '-' ? slotProps.data.totaleff[0] : 0),
                                eff: (slotProps.data.totaleff[3] || slotProps.data.totaleff[3] != '-' ? (slotProps.data.totaleff[3]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                </template>
            </Column>
            <Column header="Apr" style="min-width: 200px">
                <template #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.tm[0] || slotProps.data.tm[0] != '-' ? slotProps.data.tm[0] : 0),
                                eff: (slotProps.data.tm[4] || slotProps.data.tm[4] != '-' ? (slotProps.data.tm[4]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showCostStd">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.coststd[0] || slotProps.data.coststd[0] != '-' ? slotProps.data.coststd[0] : 0),
                                eff: (slotProps.data.coststd[4] || slotProps.data.coststd[4] != '-' ? (slotProps.data.coststd[4]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showCostEff">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.costeff[0] || slotProps.data.costeff[0] != '-' ? slotProps.data.costeff[0] : 0),
                                eff: (slotProps.data.costeff[4] || slotProps.data.costeff[4] != '-' ? (slotProps.data.costeff[4]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showRawWeight">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.raw[0] || slotProps.data.raw[0] != '-' ? slotProps.data.raw[0] : 0),
                                eff: (slotProps.data.raw[4] || slotProps.data.raw[4] != '-' ? (slotProps.data.raw[4]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.totalstd[0] || slotProps.data.totalstd[0] != '-' ? slotProps.data.totalstd[0] : 0),
                                eff: (slotProps.data.totalstd[4] || slotProps.data.totalstd[4] != '-' ? (slotProps.data.totalstd[4]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.totaleff[0] || slotProps.data.totaleff[0] != '-' ? slotProps.data.totaleff[0] : 0),
                                eff: (slotProps.data.totaleff[4] || slotProps.data.totaleff[4] != '-' ? (slotProps.data.totaleff[4]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                </template>
            </Column>
            <Column header="May" style="min-width: 200px">
                <template #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.tm[0] || slotProps.data.tm[0] != '-' ? slotProps.data.tm[0] : 0),
                                eff: (slotProps.data.tm[5] || slotProps.data.tm[5] != '-' ? (slotProps.data.tm[5]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showCostStd">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.coststd[0] || slotProps.data.coststd[0] != '-' ? slotProps.data.coststd[0] : 0),
                                eff: (slotProps.data.coststd[5] || slotProps.data.coststd[5] != '-' ? (slotProps.data.coststd[5]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showCostEff">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.costeff[0] || slotProps.data.costeff[0] != '-' ? slotProps.data.costeff[0] : 0),
                                eff: (slotProps.data.costeff[5] || slotProps.data.costeff[5] != '-' ? (slotProps.data.costeff[5]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showRawWeight">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.raw[0] || slotProps.data.raw[0] != '-' ? slotProps.data.raw[0] : 0),
                                eff: (slotProps.data.raw[5] || slotProps.data.raw[5] != '-' ? (slotProps.data.raw[5]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.totalstd[0] || slotProps.data.totalstd[0] != '-' ? slotProps.data.totalstd[0] : 0),
                                eff: (slotProps.data.totalstd[5] || slotProps.data.totalstd[5] != '-' ? (slotProps.data.totalstd[5]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.totaleff[0] || slotProps.data.totaleff[0] != '-' ? slotProps.data.totaleff[0] : 0),
                                eff: (slotProps.data.totaleff[5] || slotProps.data.totaleff[5] != '-' ? (slotProps.data.totaleff[5]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                </template>
            </Column>
            <Column header="Jun" style="min-width: 200px">
                <template #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.tm[0] || slotProps.data.tm[0] != '-' ? slotProps.data.tm[0] : 0),
                                eff: (slotProps.data.tm[6] || slotProps.data.tm[6] != '-' ? (slotProps.data.tm[6]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showCostStd">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.coststd[0] || slotProps.data.coststd[0] != '-' ? slotProps.data.coststd[0] : 0),
                                eff: (slotProps.data.coststd[6] || slotProps.data.coststd[6] != '-' ? (slotProps.data.coststd[6]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showCostEff">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.costeff[0] || slotProps.data.costeff[0] != '-' ? slotProps.data.costeff[0] : 0),
                                eff: (slotProps.data.costeff[6] || slotProps.data.costeff[6] != '-' ? (slotProps.data.costeff[6]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showRawWeight">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.raw[0] || slotProps.data.raw[0] != '-' ? slotProps.data.raw[0] : 0),
                                eff: (slotProps.data.raw[6] || slotProps.data.raw[6] != '-' ? (slotProps.data.raw[6]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.totalstd[0] || slotProps.data.totalstd[0] != '-' ? slotProps.data.totalstd[0] : 0),
                                eff: (slotProps.data.totalstd[6] || slotProps.data.totalstd[6] != '-' ? (slotProps.data.totalstd[6]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.totaleff[0] || slotProps.data.totaleff[0] != '-' ? slotProps.data.totaleff[0] : 0),
                                eff: (slotProps.data.totaleff[6] || slotProps.data.totaleff[6] != '-' ? (slotProps.data.totaleff[6]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                </template>
            </Column>
            <Column header="Jul" style="min-width: 200px">
                <template #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.tm[0] || slotProps.data.tm[0] != '-' ? slotProps.data.tm[0] : 0),
                                eff: (slotProps.data.tm[7] || slotProps.data.tm[7] != '-' ? (slotProps.data.tm[7]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showCostStd">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.coststd[0] || slotProps.data.coststd[0] != '-' ? slotProps.data.coststd[0] : 0),
                                eff: (slotProps.data.coststd[7] || slotProps.data.coststd[7] != '-' ? (slotProps.data.coststd[7]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showCostEff">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.costeff[0] || slotProps.data.costeff[0] != '-' ? slotProps.data.costeff[0] : 0),
                                eff: (slotProps.data.costeff[7] || slotProps.data.costeff[7] != '-' ? (slotProps.data.costeff[7]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showRawWeight">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.raw[0] || slotProps.data.raw[0] != '-' ? slotProps.data.raw[0] : 0),
                                eff: (slotProps.data.raw[7] || slotProps.data.raw[7] != '-' ? (slotProps.data.raw[7]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.totalstd[0] || slotProps.data.totalstd[0] != '-' ? slotProps.data.totalstd[0] : 0),
                                eff: (slotProps.data.totalstd[7] || slotProps.data.totalstd[7] != '-' ? (slotProps.data.totalstd[7]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.totaleff[0] || slotProps.data.totaleff[0] != '-' ? slotProps.data.totaleff[0] : 0),
                                eff: (slotProps.data.totaleff[7] || slotProps.data.totaleff[7] != '-' ? (slotProps.data.totaleff[7]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                </template>
            </Column>
            <Column header="Aug" style="min-width: 200px">
                <template #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.tm[0] || slotProps.data.tm[0] != '-' ? slotProps.data.tm[0] : 0),
                                eff: (slotProps.data.tm[8] || slotProps.data.tm[8] != '-' ? (slotProps.data.tm[8]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showCostStd">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.coststd[0] || slotProps.data.coststd[0] != '-' ? slotProps.data.coststd[0] : 0),
                                eff: (slotProps.data.coststd[8] || slotProps.data.coststd[8] != '-' ? (slotProps.data.coststd[8]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showCostEff">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.costeff[0] || slotProps.data.costeff[0] != '-' ? slotProps.data.costeff[0] : 0),
                                eff: (slotProps.data.costeff[8] || slotProps.data.costeff[8] != '-' ? (slotProps.data.costeff[8]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showRawWeight">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.raw[0] || slotProps.data.raw[0] != '-' ? slotProps.data.raw[0] : 0),
                                eff: (slotProps.data.raw[8] || slotProps.data.raw[8] != '-' ? (slotProps.data.raw[8]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.totalstd[0] || slotProps.data.totalstd[0] != '-' ? slotProps.data.totalstd[0] : 0),
                                eff: (slotProps.data.totalstd[8] || slotProps.data.totalstd[8] != '-' ? (slotProps.data.totalstd[8]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.totaleff[0] || slotProps.data.totaleff[0] != '-' ? slotProps.data.totaleff[0] : 0),
                                eff: (slotProps.data.totaleff[8] || slotProps.data.totaleff[8] != '-' ? (slotProps.data.totaleff[8]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                </template>
            </Column>
            <Column header="Sep" style="min-width: 200px">
                <template #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.tm[0] || slotProps.data.tm[0] != '-' ? slotProps.data.tm[0] : 0),
                                eff: (slotProps.data.tm[9] || slotProps.data.tm[9] != '-' ? (slotProps.data.tm[9]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showCostStd">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.coststd[0] || slotProps.data.coststd[0] != '-' ? slotProps.data.coststd[0] : 0),
                                eff: (slotProps.data.coststd[9] || slotProps.data.coststd[9] != '-' ? (slotProps.data.coststd[9]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showCostEff">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.costeff[0] || slotProps.data.costeff[0] != '-' ? slotProps.data.costeff[0] : 0),
                                eff: (slotProps.data.costeff[9] || slotProps.data.costeff[9] != '-' ? (slotProps.data.costeff[9]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showRawWeight">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.raw[0] || slotProps.data.raw[0] != '-' ? slotProps.data.raw[0] : 0),
                                eff: (slotProps.data.raw[9] || slotProps.data.raw[9] != '-' ? (slotProps.data.raw[9]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.totalstd[0] || slotProps.data.totalstd[0] != '-' ? slotProps.data.totalstd[0] : 0),
                                eff: (slotProps.data.totalstd[9] || slotProps.data.totalstd[9] != '-' ? (slotProps.data.totalstd[9]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.totaleff[0] || slotProps.data.totaleff[0] != '-' ? slotProps.data.totaleff[0] : 0),
                                eff: (slotProps.data.totaleff[9] || slotProps.data.totaleff[9] != '-' ? (slotProps.data.totaleff[9]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                </template>
            </Column>
            <Column header="Out" style="min-width: 200px">
                <template #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.tm[0] || slotProps.data.tm[0] != '-' ? slotProps.data.tm[0] : 0),
                                eff: (slotProps.data.tm[10] || slotProps.data.tm[10] != '-' ? (slotProps.data.tm[10]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showCostStd">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.coststd[0] || slotProps.data.coststd[0] != '-' ? slotProps.data.coststd[0] : 0),
                                eff: (slotProps.data.coststd[10] || slotProps.data.coststd[10] != '-' ? (slotProps.data.coststd[10]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showCostEff">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.costeff[0] || slotProps.data.costeff[0] != '-' ? slotProps.data.costeff[0] : 0),
                                eff: (slotProps.data.costeff[10] || slotProps.data.costeff[10] != '-' ? (slotProps.data.costeff[10]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showRawWeight">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.raw[0] || slotProps.data.raw[0] != '-' ? slotProps.data.raw[0] : 0),
                                eff: (slotProps.data.raw[10] || slotProps.data.raw[10] != '-' ? (slotProps.data.raw[10]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.totalstd[0] || slotProps.data.totalstd[0] != '-' ? slotProps.data.totalstd[0] : 0),
                                eff: (slotProps.data.totalstd[10] || slotProps.data.totalstd[10] != '-' ? (slotProps.data.totalstd[10]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.totaleff[0] || slotProps.data.totaleff[0] != '-' ? slotProps.data.totaleff[0] : 0),
                                eff: (slotProps.data.totaleff[10] || slotProps.data.totaleff[10] != '-' ? (slotProps.data.totaleff[10]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                </template>
            </Column>
            <Column header="Nov" style="min-width: 200px">
                <template #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.tm[0] || slotProps.data.tm[0] != '-' ? slotProps.data.tm[0] : 0),
                                eff: (slotProps.data.tm[11] || slotProps.data.tm[11] != '-' ? (slotProps.data.tm[11]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showCostStd">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.coststd[0] || slotProps.data.coststd[0] != '-' ? slotProps.data.coststd[0] : 0),
                                eff: (slotProps.data.coststd[11] || slotProps.data.coststd[11] != '-' ? (slotProps.data.coststd[11]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showCostEff">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.costeff[0] || slotProps.data.costeff[0] != '-' ? slotProps.data.costeff[0] : 0),
                                eff: (slotProps.data.costeff[11] || slotProps.data.costeff[11] != '-' ? (slotProps.data.costeff[11]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showRawWeight">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.raw[0] || slotProps.data.raw[0] != '-' ? slotProps.data.raw[0] : 0),
                                eff: (slotProps.data.raw[11] || slotProps.data.raw[11] != '-' ? (slotProps.data.raw[11]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.totalstd[0] || slotProps.data.totalstd[0] != '-' ? slotProps.data.totalstd[0] : 0),
                                eff: (slotProps.data.totalstd[11] || slotProps.data.totalstd[11] != '-' ? (slotProps.data.totalstd[11]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.totaleff[0] || slotProps.data.totaleff[0] != '-' ? slotProps.data.totaleff[0] : 0),
                                eff: (slotProps.data.totaleff[11] || slotProps.data.totaleff[11] != '-' ? (slotProps.data.totaleff[11]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                </template>
            </Column>
            <Column header="Dez" style="min-width: 200px">
                <template #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.tm[0] || slotProps.data.tm[0] != '-' ? slotProps.data.tm[0] : 0),
                                eff: (slotProps.data.tm[12] || slotProps.data.tm[12] != '-' ? (slotProps.data.tm[12]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showCostStd">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.coststd[0] || slotProps.data.coststd[0] != '-' ? slotProps.data.coststd[0] : 0),
                                eff: (slotProps.data.coststd[12] || slotProps.data.coststd[12] != '-' ? (slotProps.data.coststd[12]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showCostEff">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.costeff[0] || slotProps.data.costeff[0] != '-' ? slotProps.data.costeff[0] : 0),
                                eff: (slotProps.data.costeff[12] || slotProps.data.costeff[12] != '-' ? (slotProps.data.costeff[12]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showRawWeight">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.raw[0] || slotProps.data.raw[0] != '-' ? slotProps.data.raw[0] : 0),
                                eff: (slotProps.data.raw[12] || slotProps.data.raw[12] != '-' ? (slotProps.data.raw[12]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.totalstd[0] || slotProps.data.totalstd[0] != '-' ? slotProps.data.totalstd[0] : 0),
                                eff: (slotProps.data.totalstd[12] || slotProps.data.totalstd[12] != '-' ? (slotProps.data.totalstd[12]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <TableRaw
                            :value="{
                                std: (slotProps.data.totaleff[0] || slotProps.data.totaleff[0] != '-' ? slotProps.data.totaleff[0] : 0),
                                eff: (slotProps.data.totaleff[12] || slotProps.data.totaleff[12] != '-' ? (slotProps.data.totaleff[12]).toFixed(fixed.value) : 0)
                            }"
                        ></TableRaw>
                    </tr>
                </template>
            </Column>
        </DataTable>
        <div style="display: flex; margin: 50px 0; justify-content: center;">
            <div style="display: flex">
                <InputSwitch v-model="showTotalValue"/>
                <h3 style="margin: 0 10px;">Total Value</h3>
            </div>
            <div style="display: flex">
                <InputSwitch v-model="showMaterial"/>
                <h3 style="margin: 0 10px;">Material</h3>
            </div>
            <div style="display: flex">
                <InputSwitch v-model="showTotalMaterial"/>
                <h3 style="margin: 0 10px;">Total Material</h3>
            </div>
            <div style="display: flex">
                <InputSwitch v-model="showRawWeight"/>
                <h3 style="margin: 0 10px;">Raw Weight</h3>
            </div>
        </div>
        <div style="display: flex; margin: 50px 0; justify-content: center;">
            <div style="display: flex">
                <InputSwitch v-model="showCostStd"/>
                <h3 style="margin: 0 10px;">Cost per Unit Std</h3>
            </div>
            <div style="display: flex">
                <InputSwitch v-model="showCostEff"/>
                <h3 style="margin: 0 10px;">Cost per Unit Eff</h3>
            </div>
            <div style="display: flex">
                <InputSwitch v-model="showTotalCostStd"/>
                <h3 style="margin: 0 10px;">Total Cost Standard</h3>
            </div>
            <div style="display: flex">
                <InputSwitch v-model="showTotalCostEff"/>
                <h3 style="margin: 0 10px;">Total Cost Effective</h3>
            </div>
        </div>
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
                <Column field="material" :header="$t('dtc.raw_material')" sortable="true"></Column>
                <Column field="value" :header="$t('dtc.values')" style="min-width: 150px;">
                    <template #body="slotProps">
                        <tr v-if="showTotalMaterial">
                            <td>Total Materials</td>
                        </tr>
                        <tr v-if="showCostStd">
                            <td>Cost per Unit Std</td>
                        </tr>
                        <tr v-if="showCostEff">
                            <td>Cost per Unit Eff</td>
                        </tr>
                        <tr v-if="showRawWeight">
                            <td>Raw Weight</td>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td>Total Cost Std</td>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td>Total Cost Eff</td>
                        </tr>
                    </template>
                </Column>
                <Column v-if="!showTotalValue" field="values" header="Standard">
                    <template v-if="showMaterial" #body="slotProps">
                        <tr>
                            <tr @click="showContent(slotProps.data.material, slotProps.data.values[0].tm_composition, slotProps.data.values[0].unit)" v-for="el, ind in slotProps.data.values[0].materials" :key="ind">
                                {{slotProps.data.values[0].materials[ind].slice(0, -2)}}
                            </tr>
                        </tr>
                    </template>
                    <template v-else #body="slotProps">
                        <tr @click="showContent(slotProps.data.material, slotProps.data.values[0].tm_composition, slotProps.data.values[0].unit)" v-if="showTotalMaterial">
                            <td>{{(slotProps.data.values[0].totaltm ? slotProps.data.values[0].totaltm : '-' )}}</td>
                        </tr>
                        <tr @click="showContent(slotProps.data.material, slotProps.data.values[0].tm_composition, slotProps.data.values[0].unit)" v-if="showCostStd">
                            <td>{{(slotProps.data.values[0].costperunitstandard ? slotProps.data.values[0].costperunitstandard : '-')}}</td>
                        </tr>
                        <tr @click="showContent(slotProps.data.material, slotProps.data.values[0].tm_composition, slotProps.data.values[0].unit)" v-if="showCostEff">
                            <td>{{(slotProps.data.values[0].costperuniteffective ? slotProps.data.values[0].costperuniteffective : '-')}}</td>
                        </tr>
                        <tr @click="showContent(slotProps.data.material, slotProps.data.values[0].tm_composition, slotProps.data.values[0].unit)" v-if="showRawWeight">
                            <td>{{(slotProps.data.values[0].rawweight ? slotProps.data.values[0].rawweight : '-')}}</td>
                        </tr>
                        <tr @click="showContent(slotProps.data.material, slotProps.data.values[0].tm_composition, slotProps.data.values[0].unit)" v-if="showTotalCostStd">
                            <td>{{(slotProps.data.values[0].totalcoststandard ? slotProps.data.values[0].totalcoststandard : '-')}}</td>
                        </tr>
                        <tr @click="showContent(slotProps.data.material, slotProps.data.values[0].tm_composition, slotProps.data.values[0].unit)" v-if="showTotalCostEff">
                            <td>{{(slotProps.data.values[0].totalcosteffective ? slotProps.data.values[0].totalcosteffective : '-')}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="values" header="Jan" style="min-width: 200px">
                    <template v-if="showMaterial" #body="slotProps">
                        <tr>
                            <tr @click="showContent(slotProps.data.material, slotProps.data.values[1].tm_composition, slotProps.data.values[1].unit)" v-for="el, ind in slotProps.data.values[1].materials" :key="ind">
                                {{slotProps.data.values[1].materials[ind].slice(0, -2)}}
                            </tr>
                        </tr>
                    </template>
                    <template v-else #body="slotProps">
                        <tr v-if="showTotalMaterial">
                            <td v-if="showTotalValue" @click="showContent(slotProps.data.material, slotProps.data.values[1].tm_composition)">{{(slotProps.data.values[1].totaltm)}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[1].tm_composition)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totaltm || slotProps.data.values[0].totaltm != '-' ? slotProps.data.values[0].totaltm : 0),
                                    eff: (slotProps.data.values[1].totaltm || Object.keys(slotProps.data.values[1]).length > 0 ? (slotProps.data.values[1].totaltm).toFixed(fixed.value): 0)
                                }"
                            >
                            </TableRaw>
                        </tr>
                        <tr v-if="showCostStd">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[1].tm_composition, slotProps.data.values[1].unit)" v-if="showTotalValue">{{slotProps.data.values[1].costperunitstandard_volum || Object.keys(slotProps.data.values[1]).length > 0 ? (slotProps.data.values[1].costperunitstandard_volum).toFixed(fixed.value): '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[1].tm_composition, slotProps.data.values[1].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].costperunitstandard || slotProps.data.values[0].costperunitstandard != '-' ? slotProps.data.values[0].costperunitstandard: 0),
                                    eff: (slotProps.data.values[1].costperunitstandard || Object.keys(slotProps.data.values[1]).length > 0 ? (slotProps.data.values[1].costperunitstandard).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showCostEff">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[1].tm_composition, slotProps.data.values[1].unit)" v-if="showTotalValue">{{slotProps.data.values[1].costperuniteffective_volum || Object.keys(slotProps.data.values[1]).length > 0 ? (slotProps.data.values[1].costperuniteffective_volum).toFixed(fixed.value): '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[1].tm_composition, slotProps.data.values[1].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].costperuniteffective || slotProps.data.values[0].costperuniteffective != '-' ? slotProps.data.values[0].costperuniteffective: 0),
                                    eff: (slotProps.data.values[1].costperuniteffective || Object.keys(slotProps.data.values[1]).length > 0 ? (slotProps.data.values[1].costperuniteffective).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showRawWeight">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[1].tm_composition, slotProps.data.values[1].unit)" v-if="showTotalValue">{{slotProps.data.values[1].raw_weight_volum || Object.keys(slotProps.data.values[1]).length > 0 ? (slotProps.data.values[1].raw_weight_volum).toFixed(fixed.value): '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[1].tm_composition, slotProps.data.values[1].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].rawweight || slotProps.data.values[0].rawweight != '-' ? slotProps.data.values[0].rawweight: 0),
                                    eff: (slotProps.data.values[1].rawweight || Object.keys(slotProps.data.values[1]).length > 0 ? (slotProps.data.values[1].rawweight).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[1].tm_composition, slotProps.data.values[1].unit)" v-if="showTotalValue">{{slotProps.data.values[1].totalcoststandard_volum || Object.keys(slotProps.data.values[1]).length > 0 ? (slotProps.data.values[1].totalcoststandard_volum).toFixed(fixed.value): '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[1].tm_composition, slotProps.data.values[1].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totalcoststandard || slotProps.data.values[0].totalcoststandard != '-' ? slotProps.data.values[0].totalcoststandard: 0),
                                    eff: (slotProps.data.values[1].totalcoststandard || Object.keys(slotProps.data.values[1]).length > 0 ? (slotProps.data.values[1].totalcoststandard).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[1].tm_composition, slotProps.data.values[1].unit)" v-if="showTotalValue">{{slotProps.data.values[1].totalcosteffective_volum || Object.keys(slotProps.data.values[1]).length > 0 ? (slotProps.data.values[1].totalcosteffective_volum).toFixed(fixed.value): '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[1].tm_composition, slotProps.data.values[1].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totalcosteffective || slotProps.data.values[0].totalcosteffective != '-' ? slotProps.data.values[0].totalcosteffective: 0),
                                    eff: (slotProps.data.values[1].totalcosteffective || Object.keys(slotProps.data.values[1]).length > 0 ? (slotProps.data.values[1].totalcosteffective).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                    </template>
                </Column>
                <Column field="values" header="Feb" style="min-width: 200px">
                    <template v-if="showMaterial" #body="slotProps">
                        <tr>
                            <tr @click="showContent(slotProps.data.material, slotProps.data.values[2].tm_composition, slotProps.data.values[2].unit)" v-for="el, ind in slotProps.data.values[2].materials" :key="ind">
                                {{slotProps.data.values[2].materials[ind].slice(0, -2)}}
                            </tr>
                        </tr>
                    </template>
                    <template v-else #body="slotProps">
                        <tr v-if="showTotalMaterial">
                            <td v-if="showTotalValue" @click="showContent(slotProps.data.material, slotProps.data.values[2].tm_composition)">{{(slotProps.data.values[2].totaltm)}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[2].tm_composition)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totaltm || slotProps.data.values[0].totaltm != '-' ? slotProps.data.values[0].totaltm : 0),
                                    eff: (slotProps.data.values[2].totaltm || Object.keys(slotProps.data.values[2]).length > 0 ? slotProps.data.values[2].totaltm : 0)
                                }"
                            >
                            </TableRaw>
                        </tr>
                        <tr v-if="showCostStd">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[2].tm_composition, slotProps.data.values[2].unit)" v-if="showTotalValue">{{slotProps.data.values[2].costperunitstandard_volum || Object.keys(slotProps.data.values[2]).length > 0 ? slotProps.data.values[2].costperunitstandard_volum : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[2].tm_composition, slotProps.data.values[2].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].costperunitstandard || slotProps.data.values[0].costperunitstandard != '-' ? slotProps.data.values[0].costperunitstandard: 0),
                                    eff: (slotProps.data.values[2].costperunitstandard || Object.keys(slotProps.data.values[2]).length > 0 ? (slotProps.data.values[2].costperunitstandard).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showCostEff">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[2].tm_composition, slotProps.data.values[2].unit)" v-if="showTotalValue">{{slotProps.data.values[2].costperuniteffective_volum || Object.keys(slotProps.data.values[2]).length > 0 ? (slotProps.data.values[2].costperuniteffective_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[2].tm_composition, slotProps.data.values[2].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].costperuniteffective || slotProps.data.values[0].costperuniteffective != '-' ? slotProps.data.values[0].costperuniteffective: 0),
                                    eff: (slotProps.data.values[2].costperuniteffective || Object.keys(slotProps.data.values[2]).length > 0 ? (slotProps.data.values[2].costperuniteffective).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showRawWeight">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[2].tm_composition, slotProps.data.values[2].unit)" v-if="showTotalValue">{{slotProps.data.values[2].raw_weight_volum || Object.keys(slotProps.data.values[2]).length > 0 ? (slotProps.data.values[2].raw_weight_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[2].tm_composition, slotProps.data.values[2].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].rawweight || slotProps.data.values[0].rawweight != '-' ? slotProps.data.values[0].rawweight: 0),
                                    eff: (slotProps.data.values[2].rawweight || Object.keys(slotProps.data.values[2]).length > 0 ? (slotProps.data.values[2].rawweight).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[2].tm_composition, slotProps.data.values[2].unit)" v-if="showTotalValue">{{slotProps.data.values[2].totalcoststandard_volum || Object.keys(slotProps.data.values[2]).length > 0 ? (slotProps.data.values[2].totalcoststandard_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[2].tm_composition, slotProps.data.values[2].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totalcoststandard || slotProps.data.values[0].totalcoststandard != '-' ? slotProps.data.values[0].totalcoststandard: 0),
                                    eff: (slotProps.data.values[2].totalcoststandard || Object.keys(slotProps.data.values[2]).length > 0 ? (slotProps.data.values[2].totalcoststandard).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[2].tm_composition, slotProps.data.values[2].unit)" v-if="showTotalValue">{{slotProps.data.values[2].totalcosteffective_volum || Object.keys(slotProps.data.values[2]).length > 0 ? (slotProps.data.values[2].totalcosteffective_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[2].tm_composition, slotProps.data.values[2].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totalcosteffective || slotProps.data.values[0].totalcosteffective != '-' ? slotProps.data.values[0].totalcosteffective: 0),
                                    eff: (slotProps.data.values[2].totalcosteffective || Object.keys(slotProps.data.values[2]).length > 0 ? (slotProps.data.values[2].totalcosteffective).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                    </template>
                </Column>
                <Column field="values" header="Mar" style="min-width: 200px">
                    <template v-if="showMaterial" #body="slotProps">
                        <tr>
                            <tr @click="showContent(slotProps.data.material, slotProps.data.values[3].tm_composition, slotProps.data.values[3].unit)" v-for="el, ind in slotProps.data.values[3].materials" :key="ind">
                                {{slotProps.data.values[3].materials[ind].slice(0, -2)}}
                            </tr>
                        </tr>
                    </template>
                    <template v-else #body="slotProps">
                        <tr v-if="showTotalMaterial">
                            <td v-if="showTotalValue" @click="showContent(slotProps.data.material, slotProps.data.values[3].tm_composition)">{{(slotProps.data.values[3].totaltm)}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[3].tm_composition)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totaltm || slotProps.data.values[0].totaltm != '-' ? slotProps.data.values[0].totaltm : 0),
                                    eff: (slotProps.data.values[3].totaltm || Object.keys(slotProps.data.values[3]).length > 0 ? (slotProps.data.values[3].totaltm): 0)
                                }"
                            >
                            </TableRaw>
                        </tr>
                        <tr v-if="showCostStd">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[3].tm_composition, slotProps.data.values[3].unit)" v-if="showTotalValue">{{slotProps.data.values[3].costperunitstandard_volum || Object.keys(slotProps.data.values[3]).length > 0 ? (slotProps.data.values[3].costperunitstandard_volum).toFixed(fixed.value): '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[3].tm_composition, slotProps.data.values[3].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].costperunitstandard || slotProps.data.values[0].costperunitstandard != '-' ? slotProps.data.values[0].costperunitstandard: 0),
                                    eff: (slotProps.data.values[3].costperunitstandard || Object.keys(slotProps.data.values[3]).length > 0 ? (slotProps.data.values[3].costperunitstandard).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showCostEff">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[3].tm_composition, slotProps.data.values[3].unit)" v-if="showTotalValue">{{slotProps.data.values[3].costperuniteffective_volum || Object.keys(slotProps.data.values[3]).length > 0 ? (slotProps.data.values[3].costperuniteffective_volum).toFixed(fixed.value): '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[3].tm_composition, slotProps.data.values[3].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].costperuniteffective || slotProps.data.values[0].costperuniteffective != '-' ? slotProps.data.values[0].costperuniteffective: 0),
                                    eff: (slotProps.data.values[3].costperuniteffective || Object.keys(slotProps.data.values[3]).length > 0 ? (slotProps.data.values[3].costperuniteffective).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showRawWeight">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[3].tm_composition, slotProps.data.values[3].unit)" v-if="showTotalValue">{{slotProps.data.values[3].raw_weight_volum || Object.keys(slotProps.data.values[3]).length > 0 ? (slotProps.data.values[3].raw_weight_volum).toFixed(fixed.value): '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[3].tm_composition, slotProps.data.values[3].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].rawweight || slotProps.data.values[0].rawweight != '-' ? slotProps.data.values[0].rawweight: 0),
                                    eff: (slotProps.data.values[3].rawweight || Object.keys(slotProps.data.values[3]).length > 0 ? (slotProps.data.values[3].rawweight).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[3].tm_composition, slotProps.data.values[3].unit)" v-if="showTotalValue">{{slotProps.data.values[3].totalcoststandard_volum || Object.keys(slotProps.data.values[3]).length > 0 ? (slotProps.data.values[3].totalcoststandard_volum).toFixed(fixed.value): '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[3].tm_composition, slotProps.data.values[3].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totalcoststandard || slotProps.data.values[0].totalcoststandard != '-' ? slotProps.data.values[0].totalcoststandard: 0),
                                    eff: (slotProps.data.values[3].totalcoststandard || Object.keys(slotProps.data.values[3]).length > 0 ? (slotProps.data.values[3].totalcoststandard).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[3].tm_composition, slotProps.data.values[3].unit)" v-if="showTotalValue">{{slotProps.data.values[3].totalcosteffective_volum || Object.keys(slotProps.data.values[3]).length > 0 ? (slotProps.data.values[3].totalcosteffective_volum).toFixed(fixed.value): '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[3].tm_composition, slotProps.data.values[3].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totalcosteffective || slotProps.data.values[0].totalcosteffective != '-' ? slotProps.data.values[0].totalcosteffective: 0),
                                    eff: (slotProps.data.values[3].totalcosteffective || Object.keys(slotProps.data.values[3]).length > 0 ? (slotProps.data.values[3].totalcosteffective).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                    </template>
                </Column>
                <Column field="values" header="Apr" style="min-width: 200px">
                    <template v-if="showMaterial" #body="slotProps">
                        <tr>
                            <tr @click="showContent(slotProps.data.material, slotProps.data.values[4].tm_composition, slotProps.data.values[4].unit)" v-for="el, ind in slotProps.data.values[4].materials" :key="ind">
                                {{slotProps.data.values[4].materials[ind].slice(0, -2)}}
                            </tr>
                        </tr>
                    </template>
                    <template v-else #body="slotProps">
                        <tr v-if="showTotalMaterial">
                            <td v-if="showTotalValue" @click="showContent(slotProps.data.material, slotProps.data.values[4].tm_composition)">{{(slotProps.data.values[4].totaltm.toFixed(fixed.value))}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[4].tm_composition)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totaltm || slotProps.data.values[0].totaltm != '-' ? slotProps.data.values[0].totaltm : 0),
                                    eff: (slotProps.data.values[4].totaltm || Object.keys(slotProps.data.values[4]).length > 0 ? (slotProps.data.values[4].totaltm) : 0)
                                }"
                            >
                            </TableRaw>
                        </tr>
                        <tr v-if="showCostStd">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[4].tm_composition, slotProps.data.values[4].unit)" v-if="showTotalValue">{{slotProps.data.values[4].costperunitstandard_volum || Object.keys(slotProps.data.values[4]).length > 0 ? (slotProps.data.values[4].costperunitstandard_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[4].tm_composition, slotProps.data.values[4].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].costperunitstandard || slotProps.data.values[0].costperunitstandard != '-' ? slotProps.data.values[0].costperunitstandard: 0),
                                    eff: (slotProps.data.values[4].costperunitstandard || Object.keys(slotProps.data.values[4]).length > 0 ? (slotProps.data.values[4].costperunitstandard).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showCostEff">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[4].tm_composition, slotProps.data.values[4].unit)" v-if="showTotalValue">{{slotProps.data.values[4].costperuniteffective_volum || Object.keys(slotProps.data.values[4]).length > 0 ? (slotProps.data.values[4].costperuniteffective_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[4].tm_composition, slotProps.data.values[4].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].costperuniteffective || slotProps.data.values[0].costperuniteffective != '-' ? slotProps.data.values[0].costperuniteffective: 0),
                                    eff: (slotProps.data.values[4].costperuniteffective || Object.keys(slotProps.data.values[4]).length > 0 ? (slotProps.data.values[4].costperuniteffective).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showRawWeight">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[4].tm_composition, slotProps.data.values[4].unit)" v-if="showTotalValue">{{slotProps.data.values[4].raw_weight_volum || Object.keys(slotProps.data.values[4]).length > 0 ? (slotProps.data.values[4].raw_weight_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[4].tm_composition, slotProps.data.values[4].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].rawweight || slotProps.data.values[0].rawweight != '-' ? slotProps.data.values[0].rawweight: 0),
                                    eff: (slotProps.data.values[4].rawweight || Object.keys(slotProps.data.values[4]).length > 0 ? (slotProps.data.values[4].rawweight).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[4].tm_composition, slotProps.data.values[4].unit)" v-if="showTotalValue">{{slotProps.data.values[4].totalcoststandard_volum || Object.keys(slotProps.data.values[4]).length > 0 ? (slotProps.data.values[4].totalcoststandard_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[4].tm_composition, slotProps.data.values[4].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totalcoststandard || slotProps.data.values[0].totalcoststandard != '-' ? slotProps.data.values[0].totalcoststandard: 0),
                                    eff: (slotProps.data.values[4].totalcoststandard || Object.keys(slotProps.data.values[4]).length > 0 ? (slotProps.data.values[4].totalcoststandard).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[4].tm_composition, slotProps.data.values[4].unit)" v-if="showTotalValue">{{slotProps.data.values[4].totalcosteffective_volum || Object.keys(slotProps.data.values[4]).length > 0 ? (slotProps.data.values[4].totalcosteffective_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[4].tm_composition, slotProps.data.values[4].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totalcosteffective || slotProps.data.values[0].totalcosteffective != '-' ? slotProps.data.values[0].totalcosteffective: 0),
                                    eff: (slotProps.data.values[4].totalcosteffective || Object.keys(slotProps.data.values[4]).length > 0 ? (slotProps.data.values[4].totalcosteffective).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                    </template>
                </Column>
                <Column field="values" header="May" style="min-width: 200px">
                    <template v-if="showMaterial" #body="slotProps">
                        <tr>
                            <tr @click="showContent(slotProps.data.material, slotProps.data.values[5].tm_composition, slotProps.data.values[5].unit)" v-for="el, ind in slotProps.data.values[5].materials" :key="ind">
                                {{slotProps.data.values[5].materials[ind].slice(0, -2)}}
                            </tr>
                        </tr>
                    </template>
                    <template v-else #body="slotProps">
                        <tr v-if="showTotalMaterial">
                            <td v-if="showTotalValue" @click="showContent(slotProps.data.material, slotProps.data.values[5].tm_composition)">{{(slotProps.data.values[5].totaltm)}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[5].tm_composition)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totaltm || slotProps.data.values[0].totaltm != '-' ? slotProps.data.values[0].totaltm : 0),
                                    eff: (slotProps.data.values[5].totaltm || Object.keys(slotProps.data.values[5]).length > 0 ? (slotProps.data.values[5].totaltm) : 0)
                                }"
                            >
                            </TableRaw>
                        </tr>
                        <tr v-if="showCostStd">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[5].tm_composition, slotProps.data.values[5].unit)" v-if="showTotalValue">{{slotProps.data.values[5].costperunitstandard_volum || Object.keys(slotProps.data.values[5]).length > 0 ? (slotProps.data.values[5].costperunitstandard_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[5].tm_composition, slotProps.data.values[5].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].costperunitstandard || slotProps.data.values[0].costperunitstandard != '-' ? slotProps.data.values[0].costperunitstandard: 0),
                                    eff: (slotProps.data.values[5].costperunitstandard || Object.keys(slotProps.data.values[5]).length > 0 ? (slotProps.data.values[5].costperunitstandard).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showCostEff">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[5].tm_composition, slotProps.data.values[5].unit)" v-if="showTotalValue">{{slotProps.data.values[5].costperuniteffective_volum || Object.keys(slotProps.data.values[5]).length > 0 ? (slotProps.data.values[5].costperuniteffective_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[5].tm_composition, slotProps.data.values[5].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].costperuniteffective || slotProps.data.values[0].costperuniteffective != '-' ? slotProps.data.values[0].costperuniteffective: 0),
                                    eff: (slotProps.data.values[5].costperuniteffective || Object.keys(slotProps.data.values[5]).length > 0 ? (slotProps.data.values[5].costperuniteffective).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showRawWeight">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[5].tm_composition, slotProps.data.values[5].unit)" v-if="showTotalValue">{{slotProps.data.values[5].raw_weight_volum || Object.keys(slotProps.data.values[5]).length > 0 ? (slotProps.data.values[5].raw_weight_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[5].tm_composition, slotProps.data.values[5].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].rawweight || slotProps.data.values[0].rawweight != '-' ? slotProps.data.values[0].rawweight: 0),
                                    eff: (slotProps.data.values[5].rawweight || Object.keys(slotProps.data.values[5]).length > 0 ? (slotProps.data.values[5].rawweight).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[5].tm_composition, slotProps.data.values[5].unit)" v-if="showTotalValue">{{slotProps.data.values[5].totalcoststandard_volum || Object.keys(slotProps.data.values[5]).length > 0 ? (slotProps.data.values[5].totalcoststandard_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[5].tm_composition, slotProps.data.values[5].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totalcoststandard || slotProps.data.values[0].totalcoststandard != '-' ? slotProps.data.values[0].totalcoststandard: 0),
                                    eff: (slotProps.data.values[5].totalcoststandard || Object.keys(slotProps.data.values[5]).length > 0 ? (slotProps.data.values[5].totalcoststandard).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[5].tm_composition, slotProps.data.values[5].unit)" v-if="showTotalValue">{{slotProps.data.values[5].totalcosteffective_volum || Object.keys(slotProps.data.values[5]).length > 0 ? (slotProps.data.values[5].totalcosteffective_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[5].tm_composition, slotProps.data.values[5].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totalcosteffective || slotProps.data.values[0].totalcosteffective != '-' ? slotProps.data.values[0].totalcosteffective: 0),
                                    eff: (slotProps.data.values[5].totalcosteffective || Object.keys(slotProps.data.values[5]).length > 0 ? (slotProps.data.values[5].totalcosteffective).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                    </template>
                </Column>
                <Column field="values" header="Jun" style="min-width: 200px">
                    <template v-if="showMaterial" #body="slotProps">
                        <tr>
                            <tr @click="showContent(slotProps.data.material, slotProps.data.values[6].tm_composition, slotProps.data.values[6].unit)" v-for="el, ind in slotProps.data.values[6].materials" :key="ind">
                                {{slotProps.data.values[6].materials[ind].slice(0, -2)}}
                            </tr>
                        </tr>
                    </template>
                    <template v-else #body="slotProps">
                        <tr v-if="showTotalMaterial">
                            <td v-if="showTotalValue" @click="showContent(slotProps.data.material, slotProps.data.values[6].tm_composition)">{{(slotProps.data.values[6].totaltm)}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[6].tm_composition)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totaltm || slotProps.data.values[0].totaltm != '-' ? slotProps.data.values[0].totaltm : 0),
                                    eff: (slotProps.data.values[6].totaltm || Object.keys(slotProps.data.values[6]).length > 0 ? (slotProps.data.values[6].totaltm) : 0)
                                }"
                            >
                            </TableRaw>
                        </tr>
                        <tr v-if="showCostStd">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[6].tm_composition, slotProps.data.values[6].unit)" v-if="showTotalValue">{{slotProps.data.values[6].costperunitstandard_volum || Object.keys(slotProps.data.values[6]).length > 0 ? (slotProps.data.values[6].costperunitstandard_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[6].tm_composition, slotProps.data.values[6].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].costperunitstandard || slotProps.data.values[0].costperunitstandard != '-' ? slotProps.data.values[0].costperunitstandard: 0),
                                    eff: (slotProps.data.values[6].costperunitstandard || Object.keys(slotProps.data.values[6]).length > 0 ? (slotProps.data.values[6].costperunitstandard).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showCostEff">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[6].tm_composition, slotProps.data.values[6].unit)" v-if="showTotalValue">{{slotProps.data.values[6].costperuniteffective_volum || Object.keys(slotProps.data.values[6]).length > 0 ? (slotProps.data.values[6].costperuniteffective_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[6].tm_composition, slotProps.data.values[6].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].costperuniteffective || slotProps.data.values[0].costperuniteffective != '-' ? slotProps.data.values[0].costperuniteffective: 0),
                                    eff: (slotProps.data.values[6].costperuniteffective || Object.keys(slotProps.data.values[6]).length > 0 ? (slotProps.data.values[6].costperuniteffective).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showRawWeight">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[6].tm_composition, slotProps.data.values[6].unit)" v-if="showTotalValue">{{slotProps.data.values[6].raw_weight_volum || Object.keys(slotProps.data.values[6]).length > 0 ? (slotProps.data.values[6].raw_weight_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[6].tm_composition, slotProps.data.values[6].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].rawweight || slotProps.data.values[0].rawweight != '-' ? slotProps.data.values[0].rawweight: 0),
                                    eff: (slotProps.data.values[6].rawweight || Object.keys(slotProps.data.values[6]).length > 0 ? (slotProps.data.values[6].rawweight).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[6].tm_composition, slotProps.data.values[6].unit)" v-if="showTotalValue">{{slotProps.data.values[6].totalcoststandard_volum || Object.keys(slotProps.data.values[6]).length > 0 ? (slotProps.data.values[6].totalcoststandard_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[6].tm_composition, slotProps.data.values[6].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totalcoststandard || slotProps.data.values[0].totalcoststandard != '-' ? slotProps.data.values[0].totalcoststandard: 0),
                                    eff: (slotProps.data.values[6].totalcoststandard || Object.keys(slotProps.data.values[6]).length > 0 ? (slotProps.data.values[6].totalcoststandard).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[6].tm_composition, slotProps.data.values[6].unit)" v-if="showTotalValue">{{slotProps.data.values[6].totalcosteffective_volum || Object.keys(slotProps.data.values[6]).length > 0 ? (slotProps.data.values[6].totalcosteffective_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[6].tm_composition, slotProps.data.values[6].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totalcosteffective || slotProps.data.values[0].totalcosteffective != '-' ? slotProps.data.values[0].totalcosteffective: 0),
                                    eff: (slotProps.data.values[6].totalcosteffective || Object.keys(slotProps.data.values[6]).length > 0 ? (slotProps.data.values[6].totalcosteffective).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                    </template>
                </Column>
                <Column field="values" header="Jul" style="min-width: 200px">
                    <template v-if="showMaterial" #body="slotProps">
                        <tr>
                            <tr @click="showContent(slotProps.data.material, slotProps.data.values[7].tm_composition, slotProps.data.values[7].unit)" v-for="el, ind in slotProps.data.values[7].materials" :key="ind">
                                {{slotProps.data.values[7].materials[ind].slice(0, -2)}}
                            </tr>
                        </tr>
                    </template>
                    <template v-else #body="slotProps">
                        <tr v-if="showTotalMaterial">
                            <td v-if="showTotalValue" @click="showContent(slotProps.data.material, slotProps.data.values[7].tm_composition)">{{(slotProps.data.values[7].totaltm)}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[7].tm_composition)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totaltm || slotProps.data.values[0].totaltm != '-' ? slotProps.data.values[0].totaltm : 0),
                                    eff: (slotProps.data.values[7].totaltm || Object.keys(slotProps.data.values[7]).length > 0 ? (slotProps.data.values[7].totaltm) : 0)
                                }"
                            >
                            </TableRaw>
                        </tr>
                        <tr v-if="showCostStd">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[7].tm_composition, slotProps.data.values[7].unit)" v-if="showTotalValue">{{slotProps.data.values[7].costperunitstandard_volum || Object.keys(slotProps.data.values[7]).length > 0 ? (slotProps.data.values[7].costperunitstandard_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[7].tm_composition, slotProps.data.values[7].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].costperunitstandard || slotProps.data.values[0].costperunitstandard != '-' ? slotProps.data.values[0].costperunitstandard: 0),
                                    eff: (slotProps.data.values[7].costperunitstandard || Object.keys(slotProps.data.values[7]).length > 0 ? (slotProps.data.values[7].costperunitstandard).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showCostEff">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[7].tm_composition, slotProps.data.values[7].unit)" v-if="showTotalValue">{{slotProps.data.values[7].costperuniteffective_volum || Object.keys(slotProps.data.values[7]).length > 0 ? (slotProps.data.values[7].costperuniteffective_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[7].tm_composition, slotProps.data.values[7].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].costperuniteffective || slotProps.data.values[0].costperuniteffective != '-' ? slotProps.data.values[0].costperuniteffective: 0),
                                    eff: (slotProps.data.values[7].costperuniteffective || Object.keys(slotProps.data.values[7]).length > 0 ? (slotProps.data.values[7].costperuniteffective).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showRawWeight">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[7].tm_composition, slotProps.data.values[7].unit)" v-if="showTotalValue">{{slotProps.data.values[7].raw_weight_volum || Object.keys(slotProps.data.values[7]).length > 0 ? (slotProps.data.values[7].raw_weight_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[7].tm_composition, slotProps.data.values[7].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].rawweight || slotProps.data.values[0].rawweight != '-' ? slotProps.data.values[0].rawweight: 0),
                                    eff: (slotProps.data.values[7].rawweight || Object.keys(slotProps.data.values[7]).length > 0 ? (slotProps.data.values[7].rawweight).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[7].tm_composition, slotProps.data.values[7].unit)" v-if="showTotalValue">{{slotProps.data.values[7].totalcoststandard_volum || Object.keys(slotProps.data.values[7]).length > 0 ? (slotProps.data.values[7].totalcoststandard_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[7].tm_composition, slotProps.data.values[7].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totalcoststandard || slotProps.data.values[0].totalcoststandard != '-' ? slotProps.data.values[0].totalcoststandard: 0),
                                    eff: (slotProps.data.values[7].totalcoststandard || Object.keys(slotProps.data.values[7]).length > 0 ? (slotProps.data.values[7].totalcoststandard).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[7].tm_composition, slotProps.data.values[7].unit)" v-if="showTotalValue">{{slotProps.data.values[7].totalcosteffective_volum || Object.keys(slotProps.data.values[7]).length > 0 ? (slotProps.data.values[7].totalcosteffective_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[7].tm_composition, slotProps.data.values[7].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totalcosteffective || slotProps.data.values[0].totalcosteffective != '-' ? slotProps.data.values[0].totalcosteffective: 0),
                                    eff: (slotProps.data.values[7].totalcosteffective || Object.keys(slotProps.data.values[7]).length > 0 ? (slotProps.data.values[7].totalcosteffective).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                    </template>
                </Column>
                <Column field="values" header="Aug" style="min-width: 200px">
                    <template v-if="showMaterial" #body="slotProps">
                        <tr>
                            <tr @click="showContent(slotProps.data.material, slotProps.data.values[8].tm_composition, slotProps.data.values[8].unit)" v-for="el, ind in slotProps.data.values[8].materials" :key="ind">
                                {{slotProps.data.values[8].materials[ind].slice(0, -2)}}
                            </tr>
                        </tr>
                    </template>
                    <template v-else #body="slotProps">
                        <tr v-if="showTotalMaterial">
                            <td v-if="showTotalValue" @click="showContent(slotProps.data.material, slotProps.data.values[8].tm_composition)">{{(slotProps.data.values[8].totaltm)}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[8].tm_composition)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totaltm || slotProps.data.values[0].totaltm != '-' ? slotProps.data.values[0].totaltm : 0),
                                    eff: (slotProps.data.values[8].totaltm || Object.keys(slotProps.data.values[8]).length > 0 ? (slotProps.data.values[8].totaltm) : 0)
                                }"
                            >
                            </TableRaw>
                        </tr>
                        <tr v-if="showCostStd">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[8].tm_composition, slotProps.data.values[8].unit)" v-if="showTotalValue">{{slotProps.data.values[8].costperunitstandard_volum || Object.keys(slotProps.data.values[8]).length > 0 ? (slotProps.data.values[8].costperunitstandard_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[8].tm_composition, slotProps.data.values[8].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].costperunitstandard || slotProps.data.values[0].costperunitstandard != '-' ? slotProps.data.values[0].costperunitstandard: 0),
                                    eff: (slotProps.data.values[8].costperunitstandard || Object.keys(slotProps.data.values[8]).length > 0 ? (slotProps.data.values[8].costperunitstandard).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showCostEff">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[8].tm_composition, slotProps.data.values[8].unit)" v-if="showTotalValue">{{slotProps.data.values[8].costperuniteffective_volum || Object.keys(slotProps.data.values[8]).length > 0 ? (slotProps.data.values[8].costperuniteffective_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[8].tm_composition, slotProps.data.values[8].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].costperuniteffective || slotProps.data.values[0].costperuniteffective != '-' ? slotProps.data.values[0].costperuniteffective: 0),
                                    eff: (slotProps.data.values[8].costperuniteffective || Object.keys(slotProps.data.values[8]).length > 0 ? (slotProps.data.values[8].costperuniteffective).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showRawWeight">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[8].tm_composition, slotProps.data.values[8].unit)" v-if="showTotalValue">{{slotProps.data.values[8].raw_weight_volum || Object.keys(slotProps.data.values[8]).length > 0 ? (slotProps.data.values[8].raw_weight_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[8].tm_composition, slotProps.data.values[8].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].rawweight || slotProps.data.values[0].rawweight != '-' ? slotProps.data.values[0].rawweight: 0),
                                    eff: (slotProps.data.values[8].rawweight || Object.keys(slotProps.data.values[8]).length > 0 ? (slotProps.data.values[8].rawweight).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[8].tm_composition, slotProps.data.values[8].unit)" v-if="showTotalValue">{{slotProps.data.values[8].totalcoststandard_volum || Object.keys(slotProps.data.values[8]).length > 0 ? (slotProps.data.values[8].totalcoststandard_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[8].tm_composition, slotProps.data.values[8].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totalcoststandard || slotProps.data.values[0].totalcoststandard != '-' ? slotProps.data.values[0].totalcoststandard: 0),
                                    eff: (slotProps.data.values[8].totalcoststandard || Object.keys(slotProps.data.values[8]).length > 0 ? (slotProps.data.values[8].totalcoststandard).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[8].tm_composition, slotProps.data.values[8].unit)" v-if="showTotalValue">{{slotProps.data.values[8].totalcosteffective_volum || Object.keys(slotProps.data.values[8]).length > 0 ? (slotProps.data.values[8].totalcosteffective_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[8].tm_composition, slotProps.data.values[8].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totalcosteffective || slotProps.data.values[0].totalcosteffective != '-' ? slotProps.data.values[0].totalcosteffective: 0),
                                    eff: (slotProps.data.values[8].totalcosteffective || Object.keys(slotProps.data.values[8]).length > 0 ? (slotProps.data.values[8].totalcosteffective).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                    </template>
                </Column>
                <Column field="values" header="Sep" style="min-width: 200px">
                    <template v-if="showMaterial" #body="slotProps">
                        <tr>
                            <tr @click="showContent(slotProps.data.material, slotProps.data.values[9].tm_composition, slotProps.data.values[9].unit)" v-for="el, ind in slotProps.data.values[9].materials" :key="ind">
                                {{slotProps.data.values[9].materials[ind].slice(0, -2)}}
                            </tr>
                        </tr>
                    </template>
                    <template v-else #body="slotProps">
                        <tr v-if="showTotalMaterial">
                            <td v-if="showTotalValue" @click="showContent(slotProps.data.material, slotProps.data.values[9].tm_composition)">{{(slotProps.data.values[9].totaltm)}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[9].tm_composition)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totaltm || slotProps.data.values[0].totaltm != '-' ? slotProps.data.values[0].totaltm : 0),
                                    eff: (slotProps.data.values[9].totaltm || Object.keys(slotProps.data.values[9]).length > 0 ? (slotProps.data.values[9].totaltm) : 0)
                                }"
                            >
                            </TableRaw>
                        </tr>
                        <tr v-if="showCostStd">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[9].tm_composition, slotProps.data.values[9].unit)" v-if="showTotalValue">{{slotProps.data.values[9].costperunitstandard_volum || Object.keys(slotProps.data.values[9]).length > 0  ? (slotProps.data.values[9].costperunitstandard_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[9].tm_composition, slotProps.data.values[9].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].costperunitstandard || slotProps.data.values[0].costperunitstandard != '-' ? slotProps.data.values[0].costperunitstandard: 0),
                                    eff: (slotProps.data.values[9].costperunitstandard || Object.keys(slotProps.data.values[9]).length > 0 ? (slotProps.data.values[9].costperunitstandard).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showCostEff">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[9].tm_composition, slotProps.data.values[9].unit)" v-if="showTotalValue">{{slotProps.data.values[9].costperuniteffective_volum || Object.keys(slotProps.data.values[9]).length > 0  ? (slotProps.data.values[9].costperuniteffective_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[9].tm_composition, slotProps.data.values[9].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].costperuniteffective || slotProps.data.values[0].costperuniteffective != '-' ? slotProps.data.values[0].costperuniteffective: 0),
                                    eff: (slotProps.data.values[9].costperuniteffective || Object.keys(slotProps.data.values[9]).length > 0 ? (slotProps.data.values[9].costperuniteffective).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showRawWeight">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[9].tm_composition, slotProps.data.values[9].unit)" v-if="showTotalValue">{{slotProps.data.values[9].raw_weight_volum || Object.keys(slotProps.data.values[9]).length > 0  ? (slotProps.data.values[9].raw_weight_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[9].tm_composition, slotProps.data.values[9].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].rawweight || slotProps.data.values[0].rawweight != '-' ? slotProps.data.values[0].rawweight: 0),
                                    eff: (slotProps.data.values[9].rawweight || Object.keys(slotProps.data.values[9]).length > 0 ? (slotProps.data.values[9].rawweight).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[9].tm_composition, slotProps.data.values[9].unit)" v-if="showTotalValue">{{slotProps.data.values[9].totalcoststandard_volum || Object.keys(slotProps.data.values[9]).length > 0  ? (slotProps.data.values[9].totalcoststandard_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[9].tm_composition, slotProps.data.values[9].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totalcoststandard || slotProps.data.values[0].totalcoststandard != '-' ? slotProps.data.values[0].totalcoststandard: 0),
                                    eff: (slotProps.data.values[9].totalcoststandard || Object.keys(slotProps.data.values[9]).length > 0 ? (slotProps.data.values[9].totalcoststandard).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[9].tm_composition, slotProps.data.values[9].unit)" v-if="showTotalValue">{{slotProps.data.values[9].totalcosteffective_volum || Object.keys(slotProps.data.values[9]).length > 0  ? (slotProps.data.values[9].totalcosteffective_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[9].tm_composition, slotProps.data.values[9].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totalcosteffective || slotProps.data.values[0].totalcosteffective != '-' ? slotProps.data.values[0].totalcosteffective: 0),
                                    eff: (slotProps.data.values[9].totalcosteffective || Object.keys(slotProps.data.values[9]).length > 0 ? (slotProps.data.values[9].totalcosteffective).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                    </template>
                </Column>
                <Column field="values" header="Out" style="min-width: 200px">
                    <template v-if="showMaterial" #body="slotProps">
                        <tr>
                            <tr @click="showContent(slotProps.data.material, slotProps.data.values[10].tm_composition, slotProps.data.values[10].unit)" v-for="el, ind in slotProps.data.values[10].materials" :key="ind">
                                {{slotProps.data.values[10].materials[ind].slice(0, -2)}}
                            </tr>
                        </tr>
                    </template>
                    <template v-else #body="slotProps">
                        <tr v-if="showTotalMaterial">
                            <td v-if="showTotalValue" @click="showContent(slotProps.data.material, slotProps.data.values[10].tm_composition)">{{(slotProps.data.values[10].totaltm)}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[10].tm_composition)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totaltm || slotProps.data.values[0].totaltm != '-' ? slotProps.data.values[0].totaltm : 0),
                                    eff: (slotProps.data.values[10].totaltm || Object.keys(slotProps.data.values[10]).length > 0 ? (slotProps.data.values[10].totaltm) : 0)
                                }"
                            >
                            </TableRaw>
                        </tr>
                        <tr v-if="showCostStd">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[10].tm_composition, slotProps.data.values[10].unit)" v-if="showTotalValue">{{slotProps.data.values[10].costperunitstandard_volum || Object.keys(slotProps.data.values[10]).length > 0 ? (slotProps.data.values[10].costperunitstandard_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[10].tm_composition, slotProps.data.values[10].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].costperunitstandard || slotProps.data.values[0].costperunitstandard != '-' ? slotProps.data.values[0].costperunitstandard: 0),
                                    eff: (slotProps.data.values[10].costperunitstandard || Object.keys(slotProps.data.values[10]).length > 0 ? (slotProps.data.values[10].costperunitstandard).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showCostEff">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[10].tm_composition, slotProps.data.values[10].unit)" v-if="showTotalValue">{{slotProps.data.values[10].costperuniteffective_volum || Object.keys(slotProps.data.values[10]).length > 0 ? (slotProps.data.values[10].costperuniteffective_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[10].tm_composition, slotProps.data.values[10].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].costperuniteffective || slotProps.data.values[0].costperuniteffective != '-' ? slotProps.data.values[0].costperuniteffective: 0),
                                    eff: (slotProps.data.values[10].costperuniteffective || Object.keys(slotProps.data.values[10]).length > 0 ? (slotProps.data.values[10].costperuniteffective).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showRawWeight">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[10].tm_composition, slotProps.data.values[10].unit)" v-if="showTotalValue">{{slotProps.data.values[10].raw_weight_volum || Object.keys(slotProps.data.values[10]).length > 0 ? (slotProps.data.values[10].raw_weight_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[10].tm_composition, slotProps.data.values[10].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].rawweight || slotProps.data.values[0].rawweight != '-' ? slotProps.data.values[0].rawweight: 0),
                                    eff: (slotProps.data.values[10].rawweight || Object.keys(slotProps.data.values[10]).length > 0 ? (slotProps.data.values[10].rawweight).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[10].tm_composition, slotProps.data.values[10].unit)" v-if="showTotalValue">{{slotProps.data.values[10].totalcoststandard_volum || Object.keys(slotProps.data.values[10]).length > 0 ? (slotProps.data.values[10].totalcoststandard_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[10].tm_composition, slotProps.data.values[10].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totalcoststandard || slotProps.data.values[0].totalcoststandard != '-' ? slotProps.data.values[0].totalcoststandard: 0),
                                    eff: (slotProps.data.values[10].totalcoststandard || Object.keys(slotProps.data.values[10]).length > 0 ? (slotProps.data.values[10].totalcoststandard).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[10].tm_composition, slotProps.data.values[10].unit)" v-if="showTotalValue">{{slotProps.data.values[10].totalcosteffective_volum || Object.keys(slotProps.data.values[10]).length > 0 ? (slotProps.data.values[10].totalcosteffective_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[10].tm_composition, slotProps.data.values[10].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totalcosteffective || slotProps.data.values[0].totalcosteffective != '-' ? slotProps.data.values[0].totalcosteffective: 0),
                                    eff: (slotProps.data.values[10].totalcosteffective || Object.keys(slotProps.data.values[10]).length > 0 ? (slotProps.data.values[10].totalcosteffective).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                    </template>
                </Column>
                <Column field="values" header="Nov" style="min-width: 200px">
                    <template v-if="showMaterial" #body="slotProps">
                        <tr>
                            <tr @click="showContent(slotProps.data.material, slotProps.data.values[11].tm_composition, slotProps.data.values[11].unit)" v-for="el, ind in slotProps.data.values[11].materials" :key="ind">
                                {{slotProps.data.values[11].materials[ind].slice(0, -2)}}
                            </tr>
                        </tr>
                    </template>
                    <template v-else #body="slotProps">
                        <tr v-if="showTotalMaterial">
                            <td v-if="showTotalValue" @click="showContent(slotProps.data.material, slotProps.data.values[11].tm_composition)">{{(slotProps.data.values[11].totaltm)}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[11].tm_composition)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totaltm || slotProps.data.values[0].totaltm != '-' ? slotProps.data.values[0].totaltm : 0),
                                    eff: (slotProps.data.values[11].totaltm || Object.keys(slotProps.data.values[11]).length > 0 ? (slotProps.data.values[11].totaltm) : 0)
                                }"
                            >
                            </TableRaw>
                        </tr>
                        <tr v-if="showCostStd">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[11].tm_composition, slotProps.data.values[11].unit)" v-if="showTotalValue">{{slotProps.data.values[11].costperunitstandard_volum || Object.keys(slotProps.data.values[11]).length > 0 ? (slotProps.data.values[11].costperunitstandard_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[11].tm_composition, slotProps.data.values[11].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].costperunitstandard || slotProps.data.values[0].costperunitstandard != '-' ? slotProps.data.values[0].costperunitstandard: 0),
                                    eff: (slotProps.data.values[11].costperunitstandard || Object.keys(slotProps.data.values[11]).length > 0 ? (slotProps.data.values[11].costperunitstandard).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showCostEff">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[11].tm_composition, slotProps.data.values[11].unit)" v-if="showTotalValue">{{slotProps.data.values[11].costperuniteffective_volum || Object.keys(slotProps.data.values[11]).length > 0 ? (slotProps.data.values[11].costperuniteffective_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[11].tm_composition, slotProps.data.values[11].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].costperuniteffective || slotProps.data.values[0].costperuniteffective != '-' ? slotProps.data.values[0].costperuniteffective: 0),
                                    eff: (slotProps.data.values[11].costperuniteffective || Object.keys(slotProps.data.values[11]).length > 0 ? (slotProps.data.values[11].costperuniteffective).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showRawWeight">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[11].tm_composition, slotProps.data.values[11].unit)" v-if="showTotalValue">{{slotProps.data.values[11].raw_weight_volum || Object.keys(slotProps.data.values[11]).length > 0 ? (slotProps.data.values[11].raw_weight_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[11].tm_composition, slotProps.data.values[11].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].rawweight || slotProps.data.values[0].rawweight != '-' ? slotProps.data.values[0].rawweight: 0),
                                    eff: (slotProps.data.values[11].rawweight || Object.keys(slotProps.data.values[11]).length > 0 ? (slotProps.data.values[11].rawweight).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[11].tm_composition, slotProps.data.values[11].unit)" v-if="showTotalValue">{{slotProps.data.values[11].totalcoststandard_volum || Object.keys(slotProps.data.values[11]).length > 0 ? (slotProps.data.values[11].totalcoststandard_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[11].tm_composition, slotProps.data.values[11].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totalcoststandard || slotProps.data.values[0].totalcoststandard != '-' ? slotProps.data.values[0].totalcoststandard: 0),
                                    eff: (slotProps.data.values[11].totalcoststandard || Object.keys(slotProps.data.values[11]).length > 0 ? (slotProps.data.values[11].totalcoststandard).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[11].tm_composition, slotProps.data.values[11].unit)" v-if="showTotalValue">{{slotProps.data.values[11].totalcosteffective_volum || Object.keys(slotProps.data.values[11]).length > 0 ? (slotProps.data.values[11].totalcosteffective_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[11].tm_composition, slotProps.data.values[11].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totalcosteffective || slotProps.data.values[0].totalcosteffective != '-' ? slotProps.data.values[0].totalcosteffective: 0),
                                    eff: (slotProps.data.values[11].totalcosteffective || Object.keys(slotProps.data.values[11]).length > 0 ? (slotProps.data.values[11].totalcosteffective).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                    </template>
                </Column>
                <Column field="values" header="Dez" style="min-width: 200px">
                    <template v-if="showMaterial" #body="slotProps">
                        <tr>
                            <tr @click="showContent(slotProps.data.material, slotProps.data.values[12].tm_composition, slotProps.data.values[12].unit)" v-for="el, ind in slotProps.data.values[12].materials" :key="ind">
                                {{slotProps.data.values[12].materials[ind].slice(0, -2)}}
                            </tr>
                        </tr>
                    </template>
                    <template v-else #body="slotProps">
                        <tr v-if="showTotalMaterial">
                            <td v-if="showTotalValue" @click="showContent(slotProps.data.material, slotProps.data.values[12].tm_composition)">{{(slotProps.data.values[12].totaltm)}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[12].tm_composition)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totaltm || slotProps.data.values[0].totaltm != '-' ? slotProps.data.values[0].totaltm : 0),
                                    eff: (slotProps.data.values[12].totaltm || Object.keys(slotProps.data.values[12]).length > 0 ? (slotProps.data.values[12].totaltm) : 0)
                                }"
                            >
                            </TableRaw>
                        </tr>
                        <tr v-if="showCostStd">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[12].tm_composition, slotProps.data.values[12].unit)" v-if="showTotalValue">{{slotProps.data.values[12].costperunitstandard_volum || Object.keys(slotProps.data.values[12]).length > 0 ? (slotProps.data.values[12].costperunitstandard_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[12].tm_composition, slotProps.data.values[12].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].costperunitstandard || slotProps.data.values[0].costperunitstandard != '-' ? slotProps.data.values[0].costperunitstandard: 0),
                                    eff: (slotProps.data.values[12].costperunitstandard || Object.keys(slotProps.data.values[12]).length > 0 ? (slotProps.data.values[12].costperunitstandard).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showCostEff">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[12].tm_composition, slotProps.data.values[12].unit)" v-if="showTotalValue">{{slotProps.data.values[12].costperuniteffective_volum || Object.keys(slotProps.data.values[12]).length > 0 ? (slotProps.data.values[12].costperuniteffective_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[12].tm_composition, slotProps.data.values[12].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].costperuniteffective || slotProps.data.values[0].costperuniteffective != '-' ? slotProps.data.values[0].costperuniteffective: 0),
                                    eff: (slotProps.data.values[12].costperuniteffective || Object.keys(slotProps.data.values[12]).length > 0 ? (slotProps.data.values[12].costperuniteffective).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showRawWeight">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[12].tm_composition, slotProps.data.values[12].unit)" v-if="showTotalValue">{{slotProps.data.values[12].raw_weight_volum || Object.keys(slotProps.data.values[12]).length > 0 ? (slotProps.data.values[12].raw_weight_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[12].tm_composition, slotProps.data.values[12].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].rawweight || slotProps.data.values[0].rawweight != '-' ? slotProps.data.values[0].rawweight: 0),
                                    eff: (slotProps.data.values[12].rawweight || Object.keys(slotProps.data.values[12]).length > 0 ? (slotProps.data.values[12].rawweight).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showTotalCostStd">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[12].tm_composition, slotProps.data.values[12].unit)" v-if="showTotalValue">{{slotProps.data.values[12].totalcoststandard_volum || Object.keys(slotProps.data.values[12]).length > 0 ? (slotProps.data.values[12].totalcoststandard_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[12].tm_composition, slotProps.data.values[12].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totalcoststandard || slotProps.data.values[0].totalcoststandard != '-' ? slotProps.data.values[0].totalcoststandard: 0),
                                    eff: (slotProps.data.values[12].totalcoststandard || Object.keys(slotProps.data.values[12]).length > 0 ? (slotProps.data.values[12].totalcoststandard).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                        <tr v-if="showTotalCostEff">
                            <td @click="showContent(slotProps.data.material, slotProps.data.values[12].tm_composition, slotProps.data.values[12].unit)" v-if="showTotalValue">{{slotProps.data.values[12].totalcosteffective_volum || Object.keys(slotProps.data.values[12]).length > 0 ? (slotProps.data.values[12].totalcosteffective_volum).toFixed(fixed.value) : '-'}}</td>
                            <TableRaw @click="showContent(slotProps.data.material, slotProps.data.values[12].tm_composition, slotProps.data.values[12].unit)" v-else
                                :value="{
                                    std: (slotProps.data.values[0].totalcosteffective || slotProps.data.values[0].totalcosteffective != '-' ? slotProps.data.values[0].totalcosteffective: 0),
                                    eff: (slotProps.data.values[12].totalcosteffective || Object.keys(slotProps.data.values[12]).length > 0 ? (slotProps.data.values[12].totalcosteffective).toFixed(fixed.value): 0)
                                }"
                            ></TableRaw>
                        </tr>
                    </template>
                </Column>
            </DataTable>
        </div>
        <Toast />
        <Dialog :modal="true" v-model:visible="display">
            <template #header>
                <h2>Raw Material Composition</h2>
                <h3>{{ rawMaterial }}</h3>
            </template>
            <DataTable :value="comp" responsiveLayout="scroll">
                <Column field="value" :header="$t('dtc.raw_material')">
                    <template #body="slotProps">
                        <tr>
                            <td>{{ slotProps.data[0] }}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="Unit">
                    <template #body="slotProps">
                        <tr>
                            <td>{{ unity }}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="Raw Weight">
                    <template #body="slotProps">
                        <tr>
                            <td>{{ (slotProps.data[1].raw_weight).toFixed(fixed.value) }}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="Total Cost (EFF)">
                    <template #body="slotProps">
                        <tr>
                            <td>{{ (slotProps.data[1].totalcosteffective).toFixed(fixed.value) }}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="Total Cost (STD)">
                    <template #body="slotProps">
                        <tr>
                            <td>{{ (slotProps.data[1].totalcoststandard).toFixed(fixed.value) }}</td>
                        </tr>
                    </template>
                </Column>
            </DataTable>
            
        </Dialog>
    </template>
    <script setup>
    import Dropdown from 'primevue/dropdown';
    import Dialog from 'primevue/dialog'
    import Column from "primevue/column";
    import ProgressSpinner from 'primevue/progressspinner';
    import InputSwitch from 'primevue/inputswitch'
    import axios from "axios";
    import Toast from 'primevue/toast';
    import TableRaw from '@/layout/components/arrow-table/index.vue'
    import { useToast } from "primevue/usetoast";
    import { useDtcStore } from '../../store/dtc';
    import { FilterMatchMode } from 'primevue/api';
    import { ref, onMounted } from "vue";
    const display = ref(false)
    const dtc = useDtcStore()
    const plant = ref([]);
    const mkg = ref([]);
    const line = ref([]);
    const tire = ref([]);
    const dt = ref();
    const plantSelected = ref([]);
    const mkgSelected = ref([]);
    const lineSelected = ref([]);
    const tireSelected = ref([]);
    const year = ref([]);
    const table = ref([]);
    const fixed = ref({ value: 3, text: '3 - precision' });
    const progress = ref(false)
    const toast = useToast();
    const showTotalValue = ref(false)
    const showMaterial = ref(false)
    const showTotalMaterial = ref(true)
    const showRawWeight = ref(true)
    const showCostStd = ref(false)
    const showCostEff = ref(false)
    const showTotalCostStd = ref(true)
    const showTotalCostEff = ref(true)
    const total = ref([]);
    const modalTable = ref([]);
    let rawMaterial = ref('')
    let comp = ref([])
    let tires = ref('')
    let unity = ref('')
    const arr = ref([])
    const showContent = (rm, tm_cs, unit) => {
        comp.value = []
        display.value = true
        rawMaterial = rm
        comp.value = Object.entries(tm_cs)
        unity.value = unit
    }
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
    const submit = async () => {
        total.value = []
        progress.value = true
        if (plantSelected.value.value === undefined) {
            plantSelected.value.value = ''
        }
        const response = await axios.get('http://localhost:8000/api/v1/product_raw_material/?plant='+plantSelected.value.value + '&product=' +tireSelected.value.value + '&year=' + year.value + '&market_segment=' + mkgSelected.value.value + '&line=' + lineSelected.value.value)
        table.value = response.data
        var tm = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        var cs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        var ce = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        var rw = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        var ts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        var te = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
        table.value.forEach((element, index) => {
            element.values.forEach((el, index) => {
                tm[index] = tm[index] + (el.totaltm ? el.totaltm : 0)
                cs[index] = cs[index] + (el.costperunitstandard ? el.costperunitstandard : 0)
                ce[index] = ce[index] + (el.costperuniteffective ? el.costperuniteffective : 0)
                rw[index] = rw[index] + (el.rawweight ? el.rawweight : 0)
                ts[index] = ts[index] + (el.totalcoststandard ? el.totalcoststandard : 0)
                te[index] = te[index] + (el.totalcosteffective ? el.totalcosteffective : 0)
            })
        })
        total.value.push({
            tm: tm,
            coststd: cs,
            costeff: ce,
            raw: rw,
            totalstd: ts,
            totaleff: te,
        })
        toast.add({severity:'success', summary: 'Atualizado conforme solicitado', detail:'Permissoes atualizadas para a regra', life: 3000});
        console.log(table.value);
        progress.value = false
    }
    onMounted(async () => {
        getPlant()
        getMkg()
        getLine()
        getTire()
        const d = new Date()
        year.value = d.getFullYear()
    })
    </script>