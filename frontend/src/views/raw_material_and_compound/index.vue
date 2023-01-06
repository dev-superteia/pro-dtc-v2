<template>
<h3>Raw Material and Compound</h3>

<h5>Addons</h5>
        <div class="grid p-fluid">
            <div class="col-12">
                <div class="p-inputgroup">
                    <Dropdown optionLabel="text" v-model="plantSelected" :options="plant" placeholder="Select a plant"  @click="getPlant"/>
                </div>
            </div>
            <div class="col-12">
                <div class="p-inputgroup">
                    <Dropdown optionLabel="text" placeholder="Select a line" v-model="mkgSelected" :options="mkg" @click="getMkg"/>
                </div>
            </div>
            <div class="col-12">
                <div class="p-inputgroup">
                    <Dropdown optionLabel="text" placeholder="Market Segment" v-model="lineSelected" :options="line" @click="getMkg"/>
                </div>
            </div>
            <div class="col-12">
                <div class="p-inputgroup">
                    <InputText placeholder="Product" />
                </div>
            </div>
            <Button @click="getPlant">Testess</Button>
        </div>
</template>
<script setup>
import Dropdown from 'primevue/dropdown';
import axios from "axios";
import { useDtcStore } from '../../store/dtc';
import { ref } from "vue";
const dtc = useDtcStore()
const plant = ref([]);
const mkg = ref([]);
const line = ref([]);
const plantSelected = ref([]);
const mkgSelected = ref([]);
const lineSelected = ref([]);

const getPlant = async () => {
  plant.value = await dtc.setPlant()
};
const getMkg = async () => {
    await dtc.setMkg()
    mkg.value = dtc.mkg
    line.value = dtc.line
};

</script>