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
        <h3>Market Segment</h3>
        <div class="p-inputgroup">
            <Dropdown optionLabel="text" placeholder="Market Segment" v-model="mkgSelected" :options="mkg" @click="getMkg"/>
        </div>
    </div>
    <div class="col-12">
        <h3>Type</h3>
        <div class="p-inputgroup">
            <InputText placeholder="Type" />
        </div>
    </div>
    <div class="col-12">
        <h3>List of Type Selected</h3>
        <div class="p-inputgroup">
            <InputText placeholder="List of Type Selected" />
        </div>
    </div>
    <div class="col-12">
        <h3>Year</h3>
        <div class="p-inputgroup">
            <InputText placeholder="Year" v-model="year"/>
        </div>
    </div>
    <Button @click="getPlant">Testess</Button>
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
const lineSelected = ref([]);
const year = ref([]);

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
onMounted(async () => {
    getPlant()
    getMkg()
    getLine()
    const d = new Date()
    year.value = d.getFullYear()
})
</script>