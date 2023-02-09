<template>
    <h3>Compound and Fabric</h3>
    <div class="grid p-fluid">
        <div class="col-12">
            <h3>{{ $t('dtc.plant') }}</h3>
            <div class="p-inputgroup">
                <Dropdown optionLabel="text" v-model="plantSelected" :options="plant" placeholder="Select a plant"
                    />
            </div>
        </div>
        <div class="col-12">
            <h3>{{ $t('dtc.material') }}</h3>
            <div class="p-inputgroup">
                <Dropdown editable optionLabel="text" placeholder="Select a Material" v-model="materialSelected"
                    :options="material"/>
            </div>
        </div>
        <div class="col-12">
            <h3>{{ $t('dtc.year') }}</h3>
            <div class="p-inputgroup">
                <InputText placeholder="Year" v-model="year" />
            </div>
        </div>
        <div class="col-12">
            <h3>{{ $t('dtc.type') }}</h3>
            <div class="p-inputgroup">
                <Dropdown optionLabel="text" placeholder="Select a Type" v-model="selectMaterialBreakdown"
                    :options="itemsMaterialBreakdown" :selectOnFocus="true" />
            </div>
        </div>
        <div class="col-3 mt-3">
            <Button v-if="!progress" :label="$t('message.search')" @click="getMaterial(materialSelected.value)" icon="pi pi-send"
                iconPos="right"></Button>
            <ProgressSpinner v-if="progress" style="width:50px;height:50px" strokeWidth="8" fill="var(--surface-ground)"
                animationDuration=".5s" aria-label="Custom ProgressSpinner" />
        </div>
        <!-- <div class="col-12">
            <Card class="w-full">
            <template #header>
                <div style="display: flex; align-items: center; justify-content: space-evenly;padding: 20px;">
                    <div class="field-radiobutton">
                        <RadioButton inputId="city1" name="city" value="weight" v-model="city" @click="changeGraph('weight')"/>
                        <label for="city1">WEIGHT</label>
                    </div>
                    <div class="field-radiobutton">
                        <RadioButton inputId="city2" name="city" value="ustd" v-model="city" @click="changeGraph('coststd')"/>
                        <label for="city2">COST PER UNIT STD</label>
                    </div>
                    <div class="field-radiobutton">
                        <RadioButton inputId="city3" name="city" value="usteff" v-model="city" @click="changeGraph('costeff')"/>
                        <label for="city3">COST PER UNIT EFF</label>
                    </div>
                    <div class="field-radiobutton">
                        <RadioButton inputId="city4" name="city" value="totalstd" v-model="city" @click="changeGraph('totalcoststd')"/>
                        <label for="city4">TOTAL COST STD</label>
                    </div>
                    <div class="field-radiobutton">
                        <RadioButton inputId="city5" name="city" value="totaleff" v-model="city" @click="changeGraph('totalcosteff')"/>
                        <label for="city5">TOTAL COST EFF</label>
                    </div>
                </div>
            </template>
            <template #content>
                <Chart type="line" :data="datasets" class="w-full p-5" />
            </template>
        </Card>
        </div> -->
        <div class="col-12" v-if="component">
            <TableComponent :tableValue=table></TableComponent>
        </div>
        <div class="col-12" v-if="tissue">
            <TableTissue :tableValue="table" :plantSelected="plantSelected" :year="year"></TableTissue>
        </div>
    </div>
    <Toast />
</template>
<script setup>
import Dropdown from 'primevue/dropdown';
import axios from "axios";
import { useDtcStore } from '../../store/dtc';
import { ref, onMounted } from "vue";
import { useToast } from "primevue/usetoast";
import TableComponent from './table/mass.vue'
import TableTissue from './table/tissue.vue'
import ProgressSpinner from 'primevue/progressspinner';
import Toast from 'primevue/toast';
import Chart from 'primevue/chart';
import RadioButton from 'primevue/radiobutton';
const city = ref('weight');
const dtc = useDtcStore()
const component = ref(true)
const tissue = ref(false)
const plant = ref([]);
const toast = useToast();
const material = ref([]);
const plantSelected = ref([]);
const materialSelected = ref([]);
const year = ref([]);
const progress = ref(false)
const selectMaterialBreakdown = ref({ id: 1, text: 'Without Recycle' })
const itemsMaterialBreakdown = ref([{ id: 1, text: 'Without Recycle' }, { id: 2, text: 'With Recycle (no explosion)' }, { id: 3, text: 'With Recycle (explosion)' }])
const table = ref([]);
const desserts = ref([]);
const datasets = ref({});
const arr = ref([])

const getPlant = async () => {
    plant.value = await dtc.setPlant()

};
const getMassAll = async () => {
    await dtc.setMassAll()
    material.value = dtc.mass_all
};

const getMaterial = async (materialVmodel) => {
    if(materialVmodel.match(('^C.+$'))) {
        component.value = true
        tissue.value = false
        getComponents()
    } else {
        component.value = false
        tissue.value = true
        submit()
    }
}

const getComponents = async () => {
    progress.value = true
    const response = await axios.get('http://localhost:8000/api/v1/compound_and_fabric?plant=' + plantSelected.value.value + '&material=' + materialSelected.value.value + '&year=' + year.value + '&type=' + selectMaterialBreakdown.value.id)
    table.value = response.data
    const weights = response.data.weights;
    const lines = []
    toast.add({ severity: 'success', summary: 'Atualizado conforme solicitado', detail: 'Permissoes atualizadas para a regra', life: 3000 });
    progress.value = false
    response.data.table.forEach(function (item, i) {
        lines.push({
            name: item.rawmaterial,
            value: 0,
            std: { material: item.months[1].material, weight: convertNumber(item.months[1].raw_weight), costeff: convertNumber(item.months[1].cost_effective), coststd: convertNumber(item.months[1].cost_standard), totalcosteff: convertNumber(item.months[1].total_cost_effective), totalcoststd: convertNumber(item.months[1].total_cost_standard), weight_percent: item.months[1].raw_weight !== '--' ? convertNumber(item.months[1].raw_weight / weights[0]) : '--' },
            jan: { material: item.months[2].material, weight: convertNumber(item.months[2].raw_weight), costeff: convertNumber(item.months[2].cost_effective), coststd: convertNumber(item.months[2].cost_standard), totalcosteff: convertNumber(item.months[2].total_cost_effective), totalcoststd: convertNumber(item.months[2].total_cost_standard), weight_percent: item.months[2].raw_weight !== '--' ? convertNumber(item.months[2].raw_weight / weights[1]) : '--' },
            feb: { material: item.months[3].material, weight: convertNumber(item.months[3].raw_weight), costeff: convertNumber(item.months[3].cost_effective), coststd: convertNumber(item.months[3].cost_standard), totalcosteff: convertNumber(item.months[3].total_cost_effective), totalcoststd: convertNumber(item.months[3].total_cost_standard), weight_percent: item.months[3].raw_weight !== '--' ? convertNumber(item.months[3].raw_weight / weights[2]) : '--' },
            mar: { material: item.months[4].material, weight: convertNumber(item.months[4].raw_weight), costeff: convertNumber(item.months[4].cost_effective), coststd: convertNumber(item.months[4].cost_standard), totalcosteff: convertNumber(item.months[4].total_cost_effective), totalcoststd: convertNumber(item.months[4].total_cost_standard), weight_percent: item.months[4].raw_weight !== '--' ? convertNumber(item.months[4].raw_weight / weights[3]) : '--' },
            apr: { material: item.months[5].material, weight: convertNumber(item.months[5].raw_weight), costeff: convertNumber(item.months[5].cost_effective), coststd: convertNumber(item.months[5].cost_standard), totalcosteff: convertNumber(item.months[5].total_cost_effective), totalcoststd: convertNumber(item.months[5].total_cost_standard), weight_percent: item.months[5].raw_weight !== '--' ? convertNumber(item.months[5].raw_weight / weights[4]) : '--' },
            mai: { material: item.months[6].material, weight: convertNumber(item.months[6].raw_weight), costeff: convertNumber(item.months[6].cost_effective), coststd: convertNumber(item.months[6].cost_standard), totalcosteff: convertNumber(item.months[6].total_cost_effective), totalcoststd: convertNumber(item.months[6].total_cost_standard), weight_percent: item.months[6].raw_weight !== '--' ? convertNumber(item.months[6].raw_weight / weights[5]) : '--' },
            jun: { material: item.months[7].material, weight: convertNumber(item.months[7].raw_weight), costeff: convertNumber(item.months[7].cost_effective), coststd: convertNumber(item.months[7].cost_standard), totalcosteff: convertNumber(item.months[7].total_cost_effective), totalcoststd: convertNumber(item.months[7].total_cost_standard), weight_percent: item.months[7].raw_weight !== '--' ? convertNumber(item.months[7].raw_weight / weights[6]) : '--' },
            jul: { material: item.months[7].material, weight: convertNumber(item.months[7].raw_weight), costeff: convertNumber(item.months[7].cost_effective), coststd: convertNumber(item.months[7].cost_standard), totalcosteff: convertNumber(item.months[7].total_cost_effective), totalcoststd: convertNumber(item.months[7].total_cost_standard), weight_percent: item.months[8].raw_weight !== '--' ? convertNumber(item.months[8].raw_weight / weights[7]) : '--' },
            aug: { material: item.months[8].material, weight: convertNumber(item.months[8].raw_weight), costeff: convertNumber(item.months[8].cost_effective), coststd: convertNumber(item.months[8].cost_standard), totalcosteff: convertNumber(item.months[8].total_cost_effective), totalcoststd: convertNumber(item.months[8].total_cost_standard), weight_percent: item.months[9].raw_weight !== '--' ? convertNumber(item.months[9].raw_weight / weights[8]) : '--' },
            sep: { material: item.months[10].material, weight: convertNumber(item.months[10].raw_weight), costeff: convertNumber(item.months[10].cost_effective), coststd: convertNumber(item.months[10].cost_standard), totalcosteff: convertNumber(item.months[10].total_cost_effective), totalcoststd: convertNumber(item.months[10].total_cost_standard), weight_percent: item.months[10].raw_weight !== '--' ? convertNumber(item.months[10].raw_weight / weights[9]) : '--' },
            oct: { material: item.months[11].material, weight: convertNumber(item.months[11].raw_weight), costeff: convertNumber(item.months[11].cost_effective), coststd: convertNumber(item.months[11].cost_standard), totalcosteff: convertNumber(item.months[11].total_cost_effective), totalcoststd: convertNumber(item.months[11].total_cost_standard), weight_percent: item.months[11].raw_weight !== '--' ? convertNumber(item.months[11].raw_weight / weights[10]) : '--' },
            nov: { material: item.months[12].material, weight: convertNumber(item.months[12].raw_weight), costeff: convertNumber(item.months[12].cost_effective), coststd: convertNumber(item.months[12].cost_standard), totalcosteff: convertNumber(item.months[12].total_cost_effective), totalcoststd: convertNumber(item.months[12].total_cost_standard), weight_percent: item.months[12].raw_weight !== '--' ? convertNumber(item.months[12].raw_weight / weights[11]) : '--' },
            dec: { material: item.months[13].material, weight: convertNumber(item.months[13].raw_weight), costeff: convertNumber(item.months[13].cost_effective), coststd: convertNumber(item.months[13].cost_standard), totalcosteff: convertNumber(item.months[13].total_cost_effective), totalcoststd: convertNumber(item.months[13].total_cost_standard), weight_percent: item.months[13].raw_weight !== '--' ? convertNumber(item.months[13].raw_weight / weights[12]) : '--' },
        })
    })
    desserts.value = lines
    changeGraph('weight')
    let costEff = 0
    let costStd = 0
    let rawWeight = 0
    let totalStd = 0
    let totalEff = 0

    for(let i = 2; i<=13; i++) {
        costEff = 0
        costStd = 0
        rawWeight = 0
        table.value.table.forEach((element, index) => {
          costEff = costEff + (element.months[i].cost_effective !== '--' ? element.months[i].cost_effective : 0)
          costStd = costStd + (element.months[i].cost_standard !== '--' ? element.months[i].cost_standard : 0)
          rawWeight = rawWeight + (element.months[i].raw_weight !== '--' ? element.months[i].raw_weight : 0)
          totalStd = totalStd + (element.months[i].total_cost_standard !== '--' ? element.months[i].total_cost_standard : 0)
          totalEff = totalEff + (element.months[i].total_cost_effective !== '--' ? element.months[i].total_cost_effective : 0)
        })
        arr.value.push({cost_effective: costEff, cost_standard: costStd, raw_weight: rawWeight, total_cost_standard: totalStd, total_cost_effective: totalEff})
    }
    table.value.total.push(arr.value)
    console.log(table.value)
};

const submit = async() => {
    progress.value = true
    const response = await axios.get('http://localhost:8000/api/v1/tissue/report_raw_material_month_tissue?plant=' + plantSelected.value.value + '&material=' + materialSelected.value.value + '&year=' + year.value + '&type=' + selectMaterialBreakdown.value.id)
    table.value = {table: response.data}
    console.log(table.value);
    progress.value = false
}

const changeGraph = (type) => {
    const lines = desserts.value
    const seriesLines = []
    lines.forEach(function (item, i) {
        seriesLines.push({
            label: item.name,
            data: [verifyNumber(item.std[type]), verifyNumber(item.jan[type]), verifyNumber(item.feb[type]), verifyNumber(item.mar[type]), verifyNumber(item.apr[type]), verifyNumber(item.mai[type]), verifyNumber(item.jun[type]), verifyNumber(item.jul[type]), verifyNumber(item.aug[type]), verifyNumber(item.sep[type]), verifyNumber(item.oct[type]), verifyNumber(item.nov[type]), verifyNumber(item.dec[type])],
            fill: false,
            borderColor: 'rgb(' + Math.floor(Math.random() * 255) + ', ' + Math.floor(Math.random() * 255) + ', ' + Math.floor(Math.random() * 255) + ')',
            tension: 0.1,
            hidden: true,
        })
    })

    datasets.value.labels = ['Standard', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'Algust', 'September', 'October', 'November', 'December']
    datasets.value.datasets = seriesLines
}
const convertNumber = (number) => {
    if (number !== '--') {
        return parseFloat(number).toFixed(8)
    } else {
        return number
    }
}
const verifyNumber = (number) => {
    if (isNaN(parseFloat(number))) {
        return 0;
    } else {
        return parseFloat(number);
    }
}
onMounted(async () => {
    getPlant()
    getMassAll()
    const d = new Date()
    year.value = d.getFullYear()
})
</script>