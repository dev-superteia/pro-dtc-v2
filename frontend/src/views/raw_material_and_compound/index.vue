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
                    <Dropdown optionLabel="line" placeholder="Select a line" />
                </div>
            </div>
            <div class="col-12">
                <div class="p-inputgroup">
                    <Dropdown optionLabel="segment" placeholder="Market Segment" />
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
const plantSelected = ref([]);

const getPlant = async () => {
  plant.value = await dtc.setPlant()
};

</script>