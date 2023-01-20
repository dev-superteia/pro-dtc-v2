<template>
<h3>{{$t(`dtc.raw_material_compoound`)}}</h3>
<div class="grid p-fluid">
    <div class="col-12">
        <h3>{{$t(`dtc.plant`)}}</h3>
        <div class="p-inputgroup">
            <Dropdown optionLabel="text" :placeholder="$t('dtc.plant')" v-model="plantSelected" :options="plant"/>
        </div>
    </div>
    <div class="col-12">
        <h3>{{$t(`dtc.line`)}}</h3>
        <div class="p-inputgroup">
            <Dropdown optionLabel="text" :placeholder="$t('dtc.line')" v-model="lineSelected" :options="line"/>
        </div>
    </div>
    <div class="col-12">
        <h3>{{$t('dtc.mkg')}}</h3>
        <div class="p-inputgroup">
            <Dropdown optionLabel="text" :placeholder="$t('dtc.mkg')" v-model="mkgSelected" :options="mkg"/>
        </div>
    </div>
    <div class="col-12">
        <h3>{{$t('dtc.type')}}</h3>
        <div class="p-inputgroup">
            <Dropdown optionLabel="text" :placeholder="$t('dtc.type')" v-model="typeSelected" :options="type"/>
        </div>
    </div>
    <div class="col-12">
        <h3>{{$t('dtc.type_list')}}</h3>
        <div class="p-inputgroup">
            <Dropdown editable optionLabel="text" :placeholder="$t('dtc.type_list')" v-model="listSelected" :options="listType" @click="getTypeList"/>
        </div>
    </div>
    <div class="col-12">
        <h3>{{$t('dtc.year')}}</h3>
        <div class="p-inputgroup">
            <InputText :placeholder="$t('dtc.year')" v-model="year"/>
        </div>
    </div>
    <div class="col-2 mt-3">
        <Button v-if="!progress" :label="$t('message.search')" @click="submit()" icon="pi pi-send"
                iconPos="right"></Button>
        <ProgressSpinner v-if="progress" style="width:50px;height:50px" strokeWidth="8" fill="var(--surface-ground)"
                animationDuration=".5s" aria-label="Custom ProgressSpinner" />
    </div>
    <div class="col-12">
        <DataTable v-if="typeSelected.value === 'material'" :value="[0]" responsiveLayout="scroll">
            <Column field="total" v-for="el in 12" :key=el>
                <template #body="slotProps">
                    <td>{{ tableTotal[el] ? tableTotal[el].total : '-'}}</td>
                </template>
            </Column>
        </DataTable>
        <DataTable ref="dt" :value="tableResult" responsiveLayout="scroll" :rowsPerPageOptions="[10, 20, 50]" :filters="filters" :paginator="true" :rows="10">
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
            <Column v-if="typeSelected.value === 'raw'" field="component" :header="$t('dtc.material')"></Column>
            <Column v-else field="material" :header="$t('dtc.material')"></Column>
            <Column v-if="typeSelected.value !== 'raw'" field='plant'  :header="$t('dtc.plant')"></Column>
            <Column field="items" :header="$t('dtc.values')">
                <template #body="slotProps">
                    <tr>
                        <td>Material Volume</td>
                    </tr>
                    <tr>
                        <td>Volume</td>
                    </tr>
                    <tr>
                        <td>Total Volume</td>
                    </tr>
                </template>
            </Column>
                <Column field="items" header="JAN">
                <template v-if="typeSelected.value === 'raw'" #body="slotProps">
                    <tr>
                        <td>{{slotProps.data.array_agg[0][0]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[0][1]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[0][2]}}</td>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr>
                        <td>{{slotProps.data.array_agg[0][1]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[0][2]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[0][2] * slotProps.data.array_agg[0][1]}}</td>
                    </tr>
                </template>
            </Column>
            <Column field="items" header="FEB">
                <template v-if="typeSelected.value === 'raw'" #body="slotProps">
                    <tr>
                        <td>{{slotProps.data.array_agg[1][0]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[1][1]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[1][2]}}</td>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr>
                        <td>{{slotProps.data.array_agg[1][1]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[1][2]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[1][2] * slotProps.data.array_agg[1][1]}}</td>
                    </tr>
                </template>
            </Column>
            <Column field="items" header="MAR">
                <template v-if="typeSelected.value === 'raw'" #body="slotProps">
                    <tr>
                        <td>{{slotProps.data.array_agg[2][0]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[2][1]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[2][2]}}</td>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr>
                        <td>{{slotProps.data.array_agg[2][1]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[2][2]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[2][2] * slotProps.data.array_agg[2][1]}}</td>
                    </tr>
                </template>
            </Column>
                <Column field="items" header="APR">
                <template v-if="typeSelected.value === 'raw'" #body="slotProps">
                    <tr>
                        <td>{{slotProps.data.array_agg[3][0]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[3][1]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[3][2]}}</td>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr>
                        <td>{{slotProps.data.array_agg[3][1]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[3][2]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[3][2] * slotProps.data.array_agg[3][1]}}</td>
                    </tr>
                </template>
            </Column>
            <Column field="items" header="MAI">
                <template v-if="typeSelected.value === 'raw'" #body="slotProps">
                    <tr>
                        <td>{{slotProps.data.array_agg[4][0]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[4][1]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[4][2]}}</td>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr>
                        <td>{{slotProps.data.array_agg[4][1]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[4][2]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[4][2] * slotProps.data.array_agg[4][1]}}</td>
                    </tr>
                </template>
            </Column>
            <Column field="items" header="JUN">
                <template v-if="typeSelected.value === 'raw'" #body="slotProps">
                    <tr>
                        <td>{{slotProps.data.array_agg[5][0]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[5][1]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[5][2]}}</td>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr>
                        <td>{{slotProps.data.array_agg[5][1]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[5][2]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[5][2] * slotProps.data.array_agg[5][1]}}</td>
                    </tr>
                </template>
            </Column>
            <Column field="items" header="JUL">
                <template v-if="typeSelected.value === 'raw'" #body="slotProps">
                    <tr>
                        <td>{{slotProps.data.array_agg[6][0]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[6][1]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[6][2]}}</td>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr>
                        <td>{{slotProps.data.array_agg[6][1]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[6][2]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[6][2] * slotProps.data.array_agg[6][1]}}</td>
                    </tr>
                </template>
            </Column>
            <Column field="items" header="AUG">
                <template v-if="typeSelected.value === 'raw'" #body="slotProps">
                    <tr>
                        <td>{{slotProps.data.array_agg[7][0]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[7][1]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[7][2]}}</td>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr>
                        <td>{{slotProps.data.array_agg[7][1]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[7][2]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[7][2] * slotProps.data.array_agg[7][1]}}</td>
                    </tr>
                </template>
            </Column>
            <Column field="items" header="SEP">
                <template v-if="typeSelected.value === 'raw'" #body="slotProps">
                    <tr>
                        <td>{{slotProps.data.array_agg[8][0]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[8][1]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[8][2]}}</td>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr>
                        <td>{{slotProps.data.array_agg[8][1]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[8][2]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[8][2] * slotProps.data.array_agg[8][1]}}</td>
                    </tr>
                </template>
            </Column>
            <Column field="items" header="OCT">
                <template v-if="typeSelected.value === 'raw'" #body="slotProps">
                    <tr>
                        <td>{{slotProps.data.array_agg[9][0]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[9][1]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[9][2]}}</td>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr>
                        <td>{{slotProps.data.array_agg[9][1]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[9][2]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[9][2] * slotProps.data.array_agg[9][1]}}</td>
                    </tr>
                </template>
            </Column>
            <Column field="items" header="NOV">
                <template v-if="typeSelected.value === 'raw'" #body="slotProps">
                    <tr>
                        <td>{{slotProps.data.array_agg[10][0]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[10][1]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[10][2]}}</td>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr>
                        <td>{{slotProps.data.array_agg[10][1]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[10][2]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[10][2] * slotProps.data.array_agg[10][1]}}</td>
                    </tr>
                </template>
            </Column>
            <Column field="items" header="DEC">
                <template v-if="typeSelected.value === 'raw'" #body="slotProps">
                    <tr>
                        <td>{{slotProps.data.array_agg[11][0]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[11][1]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[11][2]}}</td>
                    </tr>
                </template>
                <template v-else #body="slotProps">
                    <tr>
                        <td>{{slotProps.data.array_agg[11][1]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[11][2]}}</td>
                    </tr>
                    <tr>
                        <td>{{slotProps.data.array_agg[11][2] * slotProps.data.array_agg[11][1]}}</td>
                    </tr>
                </template>
            </Column>
        </DataTable>
    </div>
</div>
<Toast />
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

const dtc = useDtcStore()
const plant = ref([]);
const mkg = ref([]);
const line = ref([]);
const plantSelected = ref([]);
const mkgSelected = ref([]);
const typeSelected = ref([]);
const lineSelected = ref([]);
const listSelected = ref([]);
const year = ref([]);
const type = ref([]);
const listType = ref([]);
const table = ref([]);
const tableResult = ref([]);
const tableTotal = ref([]);
const dt = ref();
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
};
const getLine = async () => {
    await dtc.setLine()
    line.value = dtc.line
};
const getType = async () => {
    await dtc.setType()
    type.value = dtc.type
};
const getTypeList = async () => {
    listSelected.value = []
    if (typeSelected.value.value === 'material') {
        await dtc.setTypeListMat()
        listType.value = dtc.typeListMat
    }
    if (typeSelected.value.value === 'raw') {
        await dtc.setTypeListRaw()
        listType.value = dtc.typeListRaw
    }
};
const submit = async () => {
    progress.value = true
    if (plantSelected.value.value === undefined) {
        plantSelected.value.value = ''
    }
    const response = await axios.get('http://localhost:8000/api/v1/raw_material_and_compound?type='+typeSelected.value.value + '&plant=' +plantSelected.value.value + '&market_segment=' + mkgSelected.value.value + '&year=' + year.value + '&line=' + lineSelected + '&type_selected=' + listSelected.value.value)
    table.value = response.data
    if ( typeSelected.value.value === 'raw' ) {
        table.value.items.forEach((element, index) => {
            var array = []
            for (let index = 1; index < 13; index++) {
               var searchFind = element.array_agg.find(el => {
                return el[3] == index
            })
              if(searchFind){
                array.push(searchFind)
              }else{
                array.push(['-', '-', '-'])
              }         
            }
            element.array_agg = array
        });
    } else {
        table.value.items.forEach((element, index) => {
            var array = []
            for (let index = 1; index < 13; index++) {
               var searchFind = element.array_agg.find(el => {
                return el[0] == index
            })
              if(searchFind){
                array.push(searchFind)
              }else{
                array.push([0, 0, 0])
              }         
            }
            element.array_agg = array
        });
    }
    tableResult.value = table.value.items
    tableTotal.value = table.value.total
    toast.add({severity:'success', summary: 'Atualizado conforme solicitado', detail:'Permissoes atualizadas para a regra', life: 3000});
    progress.value = false
};


onMounted(async () => {
    getPlant()
    getMkg()
    getLine()
    getType()
    const d = new Date()
    year.value = d.getFullYear()
})
</script>