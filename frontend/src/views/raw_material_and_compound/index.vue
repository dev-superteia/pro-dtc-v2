<template>
<h3>Raw Material and Compound</h3>
<div class="grid p-fluid">
    <div class="col-12">
        <h3>{{$t(`dtc.plant`)}}</h3>
        <div class="p-inputgroup">
            <Dropdown optionLabel="text" v-model="plantSelected" :options="plant" placeholder="Select a plant"  @click="getPlant"/>
        </div>
    </div>
    <div class="col-12">
        <h3>Line</h3>
        <div class="p-inputgroup">
            <Dropdown optionLabel="text" placeholder="Select a line" v-model="lineSelected" :options="line" @click="getLine"/>
        </div>
    </div>
    <div class="col-12">
        <h3>{{$t('dtc.mkg')}}</h3>
        <div class="p-inputgroup">
            <Dropdown optionLabel="text" placeholder="Market Segment" v-model="mkgSelected" :options="mkg" @click="getMkg"/>
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
    </div>
    <div class="col-12">
            <DataTable :value="table" responsiveLayout="scroll" groupRowsBy="product.teste" sortMode="single"
            sortField="product.teste" :sortOrder="1">
                <Column field="component" header="Material"></Column>
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
                    <template #body="slotProps">
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
                </Column>
                <Column field="value" header="FEB">
                    <template #body="slotProps">
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
                </Column>
                <Column field="value" header="MAR">
                    <template #body="slotProps">
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
                </Column>
                 <Column field="value" header="APR">
                    <template #body="slotProps">
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
                </Column>
                <Column field="value" header="MAI">
                    <template #body="slotProps">
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
                </Column>
                <Column field="value" header="JUN">
                    <template #body="slotProps">
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
                </Column>
                <Column field="value" header="JUL">
                    <template #body="slotProps">
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
                </Column>
                <Column field="value" header="AUG">
                    <template #body="slotProps">
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
                </Column>
                <Column field="value" header="SEP">
                    <template #body="slotProps">
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
                </Column>
                <Column field="value" header="OCT">
                    <template #body="slotProps">
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
                </Column>
                <Column field="value" header="NOV">
                    <template #body="slotProps">
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
                </Column>
                <Column field="value" header="DEC">
                    <template #body="slotProps">
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
    console.table(response.data)
    table.value = response.data
    table.value.forEach((element, index) => {
        var array = []
        for (let index = 0; index < 12; index++) {
           var searchFind = element.array_agg.find(el => {
            return el[3] == index
        })
          if(searchFind){
            array.push(searchFind)
          }else{
            array.push(['-', '-', index])
          }         
        }
        element.array_agg = array
    });
    console.table(table)
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