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
            <Column field="material" :header="$t('dtc.raw_material')"></Column>
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
                    <tr>
                        <td>Total Cost Std</td>
                    </tr>
                    <tr>
                        <td>Total Cost Eff</td>
                    </tr>
                </template>
            </Column>
            <Column v-if="!showTotalValue" field="values" header="Standard">
                <template v-if="showMaterial" #body="slotProps">
                    <tr>
                        <tr v-for="el, ind in slotProps.data.values[0].materials" :key="ind">
                            {{slotProps.data.values[0].materials[ind].slice(0, -2)}}
                        </tr>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <td>{{slotProps.data.values[0].totaltm}}</td>
                    </tr>
                    <tr v-if="showCostStd">
                        <td>{{slotProps.data.values[0].costperunitstandard}}</td>
                    </tr>
                    <tr v-if="showCostEff">
                        <td>{{slotProps.data.values[0].costperuniteffective}}</td>
                    </tr>
                    <tr v-if="showRawWeight">
                        <td>{{slotProps.data.values[0].rawweight}}</td>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <td>{{slotProps.data.values[0].totalcoststandard}}</td>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <td>{{slotProps.data.values[0].totalcosteffective}}</td>
                    </tr>
                </template>
            </Column>
            <Column field="values" header="Jan">
                <template v-if="showMaterial" #body="slotProps">
                    <tr>
                        <tr v-for="el, ind in slotProps.data.values[1].materials" :key="ind">
                            {{slotProps.data.values[1].materials[ind].slice(0, -2)}}
                        </tr>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <td v-if="showTotalValue">{{slotProps.data.values[1].totaltm ? slotProps.data.values[1].totaltm : '-'}}</td>
                        <td v-else>{{slotProps.data.values[1].totaltm ? slotProps.data.values[1].totaltm : '-'}}</td>
                    </tr>
                    <tr v-if="showCostStd">
                        <td v-if="showTotalValue">{{slotProps.data.values[1].costperunitstandard_volum ? slotProps.data.values[1].costperunitstandard_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[1].costperunitstandard ? slotProps.data.values[1].costperunitstandard : '-'}}</td>
                    </tr>
                    <tr v-if="showCostEff">
                        <td v-if="showTotalValue">{{slotProps.data.values[1].costperuniteffective_volum ? slotProps.data.values[1].costperuniteffective_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[1].costperuniteffective ? slotProps.data.values[1].costperuniteffective : '-'}}</td>
                    </tr>
                    <tr v-if="showRawWeight">
                        <td v-if="showTotalValue">{{slotProps.data.values[1].raw_weight_volum ? slotProps.data.values[1].raw_weight_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[1].rawweight ? slotProps.data.values[1].rawweight : '-'}}</td>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <td v-if="showTotalValue">{{slotProps.data.values[1].totalcoststandard_volum ? slotProps.data.values[1].totalcoststandard_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[1].totalcoststandard ? slotProps.data.values[1].totalcoststandard : '-'}}</td>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <td v-if="showTotalValue">{{slotProps.data.values[1].totalcosteffective_volum ? slotProps.data.values[1].totalcosteffective_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[1].totalcosteffective ? slotProps.data.values[1].totalcosteffective : '-'}}</td>
                    </tr>
                </template>
            </Column>
            <Column field="values" header="Feb">
                <template v-if="showMaterial" #body="slotProps">
                    <tr>
                        <tr v-for="el, ind in slotProps.data.values[2].materials" :key="ind">
                            {{slotProps.data.values[2].materials[ind].slice(0, -2)}}
                        </tr>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <td v-if="showTotalValue">{{slotProps.data.values[2].totaltm ? slotProps.data.values[2].totaltm : '-'}}</td>
                        <td v-else>{{slotProps.data.values[2].totaltm ? slotProps.data.values[2].totaltm : '-'}}</td>
                    </tr>
                    <tr v-if="showCostStd">
                        <td v-if="showTotalValue">{{slotProps.data.values[2].costperunitstandard_volum ? slotProps.data.values[2].costperunitstandard_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[2].costperunitstandard ? slotProps.data.values[2].costperunitstandard : '-'}}</td>
                    </tr>
                    <tr v-if="showCostEff">
                        <td v-if="showTotalValue">{{slotProps.data.values[2].costperuniteffective_volum ? slotProps.data.values[2].costperuniteffective_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[2].costperuniteffective ? slotProps.data.values[2].costperuniteffective : '-'}}</td>
                    </tr>
                    <tr v-if="showRawWeight">
                        <td v-if="showTotalValue">{{slotProps.data.values[2].raw_weight_volum ? slotProps.data.values[2].raw_weight_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[2].rawweight ? slotProps.data.values[2].rawweight : '-'}}</td>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <td v-if="showTotalValue">{{slotProps.data.values[2].totalcoststandard_volum ? slotProps.data.values[2].totalcoststandard_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[2].totalcoststandard ? slotProps.data.values[2].totalcoststandard : '-'}}</td>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <td v-if="showTotalValue">{{slotProps.data.values[2].totalcosteffective_volum ? slotProps.data.values[2].totalcosteffective_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[2].totalcosteffective ? slotProps.data.values[2].totalcosteffective : '-'}}</td>
                    </tr>
                </template>
            </Column>
            <Column field="values" header="Mar">
                <template v-if="showMaterial" #body="slotProps">
                    <tr>
                        <tr v-for="el, ind in slotProps.data.values[3].materials" :key="ind">
                            {{slotProps.data.values[3].materials[ind].slice(0, -2)}}
                        </tr>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <td v-if="showTotalValue">{{slotProps.data.values[3].totaltm ? slotProps.data.values[3].totaltm : '-'}}</td>
                        <td v-else>{{slotProps.data.values[3].totaltm ? slotProps.data.values[3].totaltm : '-'}}</td>
                    </tr>
                    <tr v-if="showCostStd">
                        <td v-if="showTotalValue">{{slotProps.data.values[3].costperunitstandard_volum ? slotProps.data.values[3].costperunitstandard_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[3].costperunitstandard ? slotProps.data.values[3].costperunitstandard : '-'}}</td>
                    </tr>
                    <tr v-if="showCostEff">
                        <td v-if="showTotalValue">{{slotProps.data.values[3].costperuniteffective_volum ? slotProps.data.values[3].costperuniteffective_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[3].costperuniteffective ? slotProps.data.values[3].costperuniteffective : '-'}}</td>
                    </tr>
                    <tr v-if="showRawWeight">
                        <td v-if="showTotalValue">{{slotProps.data.values[3].raw_weight_volum ? slotProps.data.values[3].raw_weight_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[3].rawweight ? slotProps.data.values[3].rawweight : '-'}}</td>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <td v-if="showTotalValue">{{slotProps.data.values[3].totalcoststandard_volum ? slotProps.data.values[3].totalcoststandard_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[3].totalcoststandard ? slotProps.data.values[3].totalcoststandard : '-'}}</td>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <td v-if="showTotalValue">{{slotProps.data.values[3].totalcosteffective_volum ? slotProps.data.values[3].totalcosteffective_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[3].totalcosteffective ? slotProps.data.values[3].totalcosteffective : '-'}}</td>
                    </tr>
                </template>
            </Column>
            <Column field="values" header="Apr">
                <template v-if="showMaterial" #body="slotProps">
                    <tr>
                        <tr v-for="el, ind in slotProps.data.values[4].materials" :key="ind">
                            {{slotProps.data.values[4].materials[ind].slice(0, -2)}}
                        </tr>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <td v-if="showTotalValue">{{slotProps.data.values[4].totaltm ? slotProps.data.values[4].totaltm : '-'}}</td>
                        <td v-else>{{slotProps.data.values[4].totaltm ? slotProps.data.values[4].totaltm : '-'}}</td>
                    </tr>
                    <tr v-if="showCostStd">
                        <td v-if="showTotalValue">{{slotProps.data.values[4].costperunitstandard_volum ? slotProps.data.values[4].costperunitstandard_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[4].costperunitstandard ? slotProps.data.values[4].costperunitstandard : '-'}}</td>
                    </tr>
                    <tr v-if="showCostEff">
                        <td v-if="showTotalValue">{{slotProps.data.values[4].costperuniteffective_volum ? slotProps.data.values[4].costperuniteffective_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[4].costperuniteffective ? slotProps.data.values[4].costperuniteffective : '-'}}</td>
                    </tr>
                    <tr v-if="showRawWeight">
                        <td v-if="showTotalValue">{{slotProps.data.values[4].raw_weight_volum ? slotProps.data.values[4].raw_weight_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[4].rawweight ? slotProps.data.values[4].rawweight : '-'}}</td>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <td v-if="showTotalValue">{{slotProps.data.values[4].totalcoststandard_volum ? slotProps.data.values[4].totalcoststandard_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[4].totalcoststandard ? slotProps.data.values[4].totalcoststandard : '-'}}</td>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <td v-if="showTotalValue">{{slotProps.data.values[4].totalcosteffective_volum ? slotProps.data.values[4].totalcosteffective_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[4].totalcosteffective ? slotProps.data.values[4].totalcosteffective : '-'}}</td>
                    </tr>
                </template>
            </Column>
            <Column field="values" header="May">
                <template v-if="showMaterial" #body="slotProps">
                    <tr>
                        <tr v-for="el, ind in slotProps.data.values[5].materials" :key="ind">
                            {{slotProps.data.values[5].materials[ind].slice(0, -2)}}
                        </tr>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <td>{{slotProps.data.values[5].totaltm ? slotProps.data.values[5].totaltm : '-'}}</td>
                    </tr>
                    <tr v-if="showCostStd">
                        <td v-if="showTotalValue">{{slotProps.data.values[5].costperunitstandard_volum ? slotProps.data.values[5].costperunitstandard_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[5].costperunitstandard ? slotProps.data.values[5].costperunitstandard : '-'}}</td>
                    </tr>
                    <tr v-if="showCostEff">
                        <td v-if="showTotalValue">{{slotProps.data.values[5].costperuniteffective_volum ? slotProps.data.values[5].costperuniteffective_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[5].costperuniteffective ? slotProps.data.values[5].costperuniteffective : '-'}}</td>
                    </tr>
                    <tr v-if="showRawWeight">
                        <td v-if="showTotalValue">{{slotProps.data.values[5].raw_weight_volum ? slotProps.data.values[5].raw_weight_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[5].rawweight ? slotProps.data.values[5].rawweight : '-'}}</td>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <td v-if="showTotalValue">{{slotProps.data.values[5].totalcoststandard_volum ? slotProps.data.values[5].totalcoststandard_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[5].totalcoststandard ? slotProps.data.values[5].totalcoststandard : '-'}}</td>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <td v-if="showTotalValue">{{slotProps.data.values[5].totalcosteffective_volum ? slotProps.data.values[5].totalcosteffective_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[5].totalcosteffective ? slotProps.data.values[5].totalcosteffective : '-'}}</td>
                    </tr>
                </template>
            </Column>
            <Column field="values" header="Jun">
                <template v-if="showMaterial" #body="slotProps">
                    <tr>
                        <tr v-for="el, ind in slotProps.data.values[6].materials" :key="ind">
                            {{slotProps.data.values[6].materials[ind].slice(0, -2)}}
                        </tr>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <td v-if="showTotalValue">{{slotProps.data.values[6].totaltm ? slotProps.data.values[6].totaltm : '-'}}</td>
                        <td v-else>{{slotProps.data.values[6].totaltm ? slotProps.data.values[6].totaltm : '-'}}</td>
                    </tr>
                    <tr v-if="showCostStd">
                        <td v-if="showTotalValue">{{slotProps.data.values[6].costperunitstandard_volum ? slotProps.data.values[6].costperunitstandard_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[6].costperunitstandard ? slotProps.data.values[6].costperunitstandard : '-'}}</td>
                    </tr>
                    <tr v-if="showCostEff">
                        <td v-if="showTotalValue">{{slotProps.data.values[6].costperuniteffective_volum ? slotProps.data.values[6].costperuniteffective_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[6].costperuniteffective ? slotProps.data.values[6].costperuniteffective : '-'}}</td>
                    </tr>
                    <tr v-if="showRawWeight">
                        <td v-if="showTotalValue">{{slotProps.data.values[6].raw_weight_volum ? slotProps.data.values[6].raw_weight_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[6].rawweight ? slotProps.data.values[6].rawweight : '-'}}</td>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <td v-if="showTotalValue">{{slotProps.data.values[6].totalcoststandard_volum ? slotProps.data.values[6].totalcoststandard_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[6].totalcoststandard ? slotProps.data.values[6].totalcoststandard : '-'}}</td>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <td v-if="showTotalValue">{{slotProps.data.values[6].totalcosteffective_volum ? slotProps.data.values[6].totalcosteffective_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[6].totalcosteffective ? slotProps.data.values[6].totalcosteffective : '-'}}</td>
                    </tr>
                </template>
            </Column>
            <Column field="values" header="Jul">
                <template v-if="showMaterial" #body="slotProps">
                    <tr>
                        <tr v-for="el, ind in slotProps.data.values[7].materials" :key="ind">
                            {{slotProps.data.values[7].materials[ind].slice(0, -2)}}
                        </tr>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <td v-if="showTotalValue">{{slotProps.data.values[7].totaltm ? slotProps.data.values[7].totaltm : '-'}}</td>
                        <td v-else>{{slotProps.data.values[7].totaltm ? slotProps.data.values[7].totaltm : '-'}}</td>
                    </tr>
                    <tr v-if="showCostStd">
                        <td v-if="showTotalValue">{{slotProps.data.values[7].costperunitstandard_volum ? slotProps.data.values[7].costperunitstandard_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[7].costperunitstandard ? slotProps.data.values[7].costperunitstandard : '-'}}</td>
                    </tr>
                    <tr v-if="showCostEff">
                        <td v-if="showTotalValue">{{slotProps.data.values[7].costperuniteffective_volum ? slotProps.data.values[7].costperuniteffective_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[7].costperuniteffective ? slotProps.data.values[7].costperuniteffective : '-'}}</td>
                    </tr>
                    <tr v-if="showRawWeight">
                        <td v-if="showTotalValue">{{slotProps.data.values[7].raw_weight_volum ? slotProps.data.values[7].raw_weight_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[7].rawweight ? slotProps.data.values[7].rawweight : '-'}}</td>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <td v-if="showTotalValue">{{slotProps.data.values[7].totalcoststandard_volum ? slotProps.data.values[7].totalcoststandard_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[7].totalcoststandard ? slotProps.data.values[7].totalcoststandard : '-'}}</td>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <td v-if="showTotalValue">{{slotProps.data.values[7].totalcosteffective_volum ? slotProps.data.values[7].totalcosteffective_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[7].totalcosteffective ? slotProps.data.values[7].totalcosteffective : '-'}}</td>
                    </tr>
                </template>
            </Column>
            <Column field="values" header="Aug">
                <template v-if="showMaterial" #body="slotProps">
                    <tr>
                        <tr v-for="el, ind in slotProps.data.values[8].materials" :key="ind">
                            {{slotProps.data.values[8].materials[ind].slice(0, -2)}}
                        </tr>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <td v-if="showTotalValue">{{slotProps.data.values[8].totaltm ? slotProps.data.values[8].totaltm : '-'}}</td>
                        <td v-else>{{slotProps.data.values[8].totaltm ? slotProps.data.values[8].totaltm : '-'}}</td>
                    </tr>
                    <tr v-if="showCostStd">
                        <td v-if="showTotalValue">{{slotProps.data.values[8].costperunitstandard_volum ? slotProps.data.values[8].costperunitstandard_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[8].costperunitstandard ? slotProps.data.values[8].costperunitstandard : '-'}}</td>
                    </tr>
                    <tr v-if="showCostEff">
                        <td v-if="showTotalValue">{{slotProps.data.values[8].costperuniteffective_volum ? slotProps.data.values[8].costperuniteffective_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[8].costperuniteffective ? slotProps.data.values[8].costperuniteffective : '-'}}</td>
                    </tr>
                    <tr v-if="showRawWeight">
                        <td v-if="showTotalValue">{{slotProps.data.values[8].raw_weight_volum ? slotProps.data.values[8].raw_weight_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[8].rawweight ? slotProps.data.values[8].rawweight : '-'}}</td>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <td v-if="showTotalValue">{{slotProps.data.values[8].totalcoststandard_volum ? slotProps.data.values[8].totalcoststandard_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[8].totalcoststandard ? slotProps.data.values[8].totalcoststandard : '-'}}</td>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <td v-if="showTotalValue">{{slotProps.data.values[8].totalcosteffective_volum ? slotProps.data.values[8].totalcosteffective_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[8].totalcosteffective ? slotProps.data.values[8].totalcosteffective : '-'}}</td>
                    </tr>
                </template>
            </Column>
            <Column field="values" header="Sep">
                <template v-if="showMaterial" #body="slotProps">
                    <tr>
                        <tr v-for="el, ind in slotProps.data.values[9].materials" :key="ind">
                            {{slotProps.data.values[9].materials[ind].slice(0, -2)}}
                        </tr>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <td v-if="showTotalValue">{{slotProps.data.values[9].totaltm ? slotProps.data.values[9].totaltm : '-'}}</td>
                        <td v-else>{{slotProps.data.values[9].totaltm ? slotProps.data.values[9].totaltm : '-'}}</td>
                    </tr>
                    <tr v-if="showCostStd">
                        <td v-if="showTotalValue">{{slotProps.data.values[9].costperunitstandard_volum ? slotProps.data.values[9].costperunitstandard_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[9].costperunitstandard ? slotProps.data.values[9].costperunitstandard : '-'}}</td>
                    </tr>
                    <tr v-if="showCostEff">
                        <td v-if="showTotalValue">{{slotProps.data.values[9].costperuniteffective_volum ? slotProps.data.values[9].costperuniteffective_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[9].costperuniteffective ? slotProps.data.values[9].costperuniteffective : '-'}}</td>
                    </tr>
                    <tr v-if="showRawWeight">
                        <td v-if="showTotalValue">{{slotProps.data.values[9].raw_weight_volum ? slotProps.data.values[9].raw_weight_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[9].rawweight ? slotProps.data.values[9].rawweight : '-'}}</td>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <td v-if="showTotalValue">{{slotProps.data.values[9].totalcoststandard_volum ? slotProps.data.values[9].totalcoststandard_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[9].totalcoststandard ? slotProps.data.values[9].totalcoststandard : '-'}}</td>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <td v-if="showTotalValue">{{slotProps.data.values[9].totalcosteffective_volum ? slotProps.data.values[9].totalcosteffective_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[9].totalcosteffective ? slotProps.data.values[9].totalcosteffective : '-'}}</td>
                    </tr>
                </template>
            </Column>
            <Column field="values" header="Out">
                <template v-if="showMaterial" #body="slotProps">
                    <tr>
                        <tr v-for="el, ind in slotProps.data.values[10].materials" :key="ind">
                            {{slotProps.data.values[10].materials[ind].slice(0, -2)}}
                        </tr>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <td v-if="showTotalValue">{{slotProps.data.values[10].totaltm ? slotProps.data.values[10].totaltm : '-'}}</td>
                        <td v-else>{{slotProps.data.values[10].totaltm ? slotProps.data.values[10].totaltm : '-'}}</td>
                    </tr>
                    <tr v-if="showCostStd">
                        <td v-if="showTotalValue">{{slotProps.data.values[10].costperunitstandard_volum ? slotProps.data.values[10].costperunitstandard_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[10].costperunitstandard ? slotProps.data.values[10].costperunitstandard : '-'}}</td>
                    </tr>
                    <tr v-if="showCostEff">
                        <td v-if="showTotalValue">{{slotProps.data.values[10].costperuniteffective_volum ? slotProps.data.values[10].costperuniteffective_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[10].costperuniteffective ? slotProps.data.values[10].costperuniteffective : '-'}}</td>
                    </tr>
                    <tr v-if="showRawWeight">
                        <td v-if="showTotalValue">{{slotProps.data.values[10].raw_weight_volum ? slotProps.data.values[10].raw_weight_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[10].rawweight ? slotProps.data.values[10].rawweight : '-'}}</td>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <td v-if="showTotalValue">{{slotProps.data.values[10].totalcoststandard_volum ? slotProps.data.values[10].totalcoststandard_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[10].totalcoststandard ? slotProps.data.values[10].totalcoststandard : '-'}}</td>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <td v-if="showTotalValue">{{slotProps.data.values[10].totalcosteffective_volum ? slotProps.data.values[10].totalcosteffective_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[10].totalcosteffective ? slotProps.data.values[10].totalcosteffective : '-'}}</td>
                    </tr>
                </template>
            </Column>
            <Column field="values" header="Nov">
                <template v-if="showMaterial" #body="slotProps">
                    <tr>
                        <tr v-for="el, ind in slotProps.data.values[11].materials" :key="ind">
                            {{slotProps.data.values[11].materials[ind].slice(0, -2)}}
                        </tr>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <td v-if="showTotalValue">{{slotProps.data.values[11].totaltm ? slotProps.data.values[11].totaltm : '-'}}</td>
                        <td v-else>{{slotProps.data.values[11].totaltm ? slotProps.data.values[11].totaltm : '-'}}</td>
                    </tr>
                    <tr v-if="showCostStd">
                        <td v-if="showTotalValue">{{slotProps.data.values[11].costperunitstandard_volum ? slotProps.data.values[11].costperunitstandard_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[11].costperunitstandard ? slotProps.data.values[11].costperunitstandard : '-'}}</td>
                    </tr>
                    <tr v-if="showCostEff">
                        <td v-if="showTotalValue">{{slotProps.data.values[11].costperuniteffective_volum ? slotProps.data.values[11].costperuniteffective_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[11].costperuniteffective ? slotProps.data.values[11].costperuniteffective : '-'}}</td>
                    </tr>
                    <tr v-if="showRawWeight">
                        <td v-if="showTotalValue">{{slotProps.data.values[11].raw_weight_volum ? slotProps.data.values[11].raw_weight_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[11].rawweight ? slotProps.data.values[11].rawweight : '-'}}</td>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <td v-if="showTotalValue">{{slotProps.data.values[11].totalcoststandard_volum ? slotProps.data.values[11].totalcoststandard_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[11].totalcoststandard ? slotProps.data.values[11].totalcoststandard : '-'}}</td>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <td v-if="showTotalValue">{{slotProps.data.values[11].totalcosteffective_volum ? slotProps.data.values[11].totalcosteffective_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[11].totalcosteffective ? slotProps.data.values[11].totalcosteffective : '-'}}</td>
                    </tr>
                </template>
            </Column>
            <Column field="values" header="Dez">
                <template v-if="showMaterial" #body="slotProps">
                    <tr>
                        <tr v-for="el, ind in slotProps.data.values[12].materials" :key="ind">
                            {{slotProps.data.values[12].materials[ind].slice(0, -2)}}
                        </tr>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr v-if="showTotalMaterial">
                        <td v-if="showTotalValue">{{slotProps.data.values[12].totaltm ? slotProps.data.values[12].totaltm : '-'}}</td>
                        <td v-else>{{slotProps.data.values[12].totaltm ? slotProps.data.values[12].totaltm : '-'}}</td>
                    </tr>
                    <tr v-if="showCostStd">
                        <td v-if="showTotalValue">{{slotProps.data.values[12].costperunitstandard_volum ? slotProps.data.values[12].costperunitstandard_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[12].costperunitstandard ? slotProps.data.values[12].costperunitstandard : '-'}}</td>
                    </tr>
                    <tr v-if="showCostEff">
                        <td v-if="showTotalValue">{{slotProps.data.values[12].costperuniteffective_volum ? slotProps.data.values[12].costperuniteffective_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[12].costperuniteffective ? slotProps.data.values[12].costperuniteffective : '-'}}</td>
                    </tr>
                    <tr v-if="showRawWeight">
                        <td v-if="showTotalValue">{{slotProps.data.values[12].raw_weight_volum ? slotProps.data.values[12].raw_weight_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[12].rawweight ? slotProps.data.values[12].rawweight : '-'}}</td>
                    </tr>
                    <tr v-if="showTotalCostStd">
                        <td v-if="showTotalValue">{{slotProps.data.values[12].totalcoststandard_volum ? slotProps.data.values[12].totalcoststandard_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[12].totalcoststandard ? slotProps.data.values[12].totalcoststandard : '-'}}</td>
                    </tr>
                    <tr v-if="showTotalCostEff">
                        <td v-if="showTotalValue">{{slotProps.data.values[12].totalcosteffective_volum ? slotProps.data.values[12].totalcosteffective_volum : '-'}}</td>
                        <td v-else>{{slotProps.data.values[12].totalcosteffective ? slotProps.data.values[12].totalcosteffective : '-'}}</td>
                    </tr>
                </template>
            </Column>
        </DataTable>
    </div>
    <Toast />
</template>
<script setup>
import Dropdown from 'primevue/dropdown';
import Column from "primevue/column";
import ProgressSpinner from 'primevue/progressspinner';
import InputSwitch from 'primevue/inputswitch'
import axios from "axios";
import Toast from 'primevue/toast';
import { useToast } from "primevue/usetoast";
import { useDtcStore } from '../../store/dtc';
import { FilterMatchMode } from 'primevue/api';
import { ref, onMounted } from "vue";

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
const fixed = ref();
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
    progress.value = true
    if (plantSelected.value.value === undefined) {
        plantSelected.value.value = ''
    }
    const response = await axios.get('http://localhost:8000/api/v1/product_raw_material/?plant='+plantSelected.value.value + '&product=' +tireSelected.value.value + '&year=' + year.value + '&market_segment=' + mkgSelected.value.value + '&line=' + lineSelected.value.value)
    table.value = response.data
    console.log(table.value)
    // table.value.forEach(element => {
    //     // console.log(element.values[12]);
    //     const entries = Object.entries(element.values[12]);
    //     element.values.push(entries)
    // })
    toast.add({severity:'success', summary: 'Atualizado conforme solicitado', detail:'Permissoes atualizadas para a regra', life: 3000});
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