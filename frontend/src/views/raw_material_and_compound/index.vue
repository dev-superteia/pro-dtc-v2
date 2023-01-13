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
        <Button :label="$t('message.search')" @click="getResult" icon="pi pi-send" iconPos="right" ></Button>
    </div>
    
</div>
</template>
<script setup>
import Dropdown from 'primevue/dropdown';
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
const material = ref([]);

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
const getResult = async () => {
    const response = await axios.get('http://localhost:8000/api/v1/')
    material.value = response.data
    console.log(material.value);
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