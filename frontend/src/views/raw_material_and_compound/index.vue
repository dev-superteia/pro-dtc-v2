<template>
<h3>Raw Material and Compound</h3>
<div class="grid p-fluid">
    <div class="col-12">
        <h3>{{$t(`dtc.plant`)}}</h3>
        <div class="p-inputgroup">
            <Dropdown optionLabel="text" v-model="plantSelected" :options="plant" placeholder="Select a plant"/>
        </div>
    </div>
    <div class="col-12">
        <h3>{{$t(`dtc.line`)}}</h3>
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
        <h3>{{$t('dtc.type')}}</h3>
        <div class="p-inputgroup">
            <Dropdown optionLabel="text" placeholder="Type" v-model="typeSelected" :options="type"/>
        </div>
    </div>
    <div class="col-12">
        <h3>{{$t('dtc.type_list')}}</h3>
        <div class="p-inputgroup">
            <Dropdown editable optionLabel="text" placeholder="List of Type Selected" v-model="listSelected" :options="listType" @click="getTypeList"/>
        </div>
    </div>
    <div class="col-12">
        <h3>{{$t('dtc.year')}}</h3>
        <div class="p-inputgroup">
            <InputText placeholder="Year" v-model="year"/>
        </div>
    </div>
    <div class="col-2 mt-3">
        <Button :label="$t('message.search')" @click="submit" icon="pi pi-send" iconPos="right" ></Button>
        <Button label="CONFUSÃO" @click="test" icon="pi pi-send" iconPos="right" ></Button>
    </div>
    <div class="col-12">
            <DataTable :value="table" responsiveLayout="scroll" groupRowsBy="product.teste" sortMode="single"
            sortField="product.teste" :sortOrder="1" :paginator="true" :rows="10">
            <template #header>
                <div class="grid">
                    <div class="col-12 md:col-6">
                        <span class="p-input-icon-left">
                            <i class="pi pi-search"/>
                            <InputText  style="max-width: 200px;"/>
                        </span>
                    </div>       
                    <div class="col-12 md:col-6"><Dropdown optionLabel="text" placeholder="Precission value" style="max-width: 200px; float: right;"/></div>       
                </div>
            </template>
                <Column v-if="typeSelected.value === 'raw'" field="component" header="Material"></Column>
                <Column v-else field="material" header="Material"></Column>
                <Column v-if="typeSelected.value !== 'raw'" field='plant'  header="Plant"></Column>
                <Column field="value" header="Values">
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
                 <Column field="value" header="JAN">
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
                <Column field="value" header="FEB">
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
                <Column field="value" header="MAR">
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
                 <Column field="value" header="APR">
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
                <Column field="value" header="MAI">
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
                <Column field="value" header="JUN">
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
                <Column field="value" header="JUL">
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
                <Column field="value" header="AUG">
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
                <Column field="value" header="SEP">
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
                <Column field="value" header="OCT">
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
                <Column field="value" header="NOV">
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
                <Column field="value" header="DEC">
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
</template>
<script setup>
import Dropdown from 'primevue/dropdown';
import Column from "primevue/column";
import axios from "axios";
import { useDtcStore } from '../../store/dtc';
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
    if (typeSelected.value.value === 'material') {
        console.log(typeSelected.value);
        await dtc.setTypeListMat()
        listType.value = dtc.typeListMat
    }
    if (typeSelected.value.value === 'raw') {
        console.log(typeSelected.value);
        await dtc.setTypeListRaw()
        listType.value = dtc.typeListRaw
    }
};
const submit = async () => {
    const response = await axios.get('http://localhost:8000/api/v1/raw_material_and_compound?type='+typeSelected.value.value + '&plant=' +plantSelected.value.value + '&market_segment=' + mkgSelected.value.value + '&year=' + year.value + '&line=' + lineSelected + '&type_selected=' + listSelected.value.value)
    table.value = response.data
    if ( typeSelected.value.value === 'raw' ) {
        table.value.forEach((element, index) => {
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
        table.value.forEach((element, index) => {
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
    console.table(table.value)
};

let arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
const test = async () => {
    table.value.forEach((element, index) => {
        element.array_agg.forEach(el => {
            arr[el[0]] = arr[el[0]] + (el[1] * el[2])
        })
    })
    console.table(arr);
}

onMounted(async () => {
    getPlant()
    getMkg()
    getLine()
    getType()
    const d = new Date()
    year.value = d.getFullYear()
})
</script>