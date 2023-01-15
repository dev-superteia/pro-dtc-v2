<template>
    <h3>Tissue Month</h3>
    <div class="grid p-fluid">
        <div class="col-12">
            <h3>{{$t('dtc.plant')}}</h3>
            <div class="p-inputgroup">
                <Dropdown optionLabel="text" v-model="plantSelected" :options="plant" :placeholder="$t('dtc.plant')"
                    @click="getPlant" />
            </div>
        </div>
        <div class="col-12">
            <h3>{{$t('dtc.year')}}</h3>
            <div class="p-inputgroup">
                <InputText :placeholder="$t('dtc.year')" v-model="year" />
            </div>
        </div>
        <div class="col-2 mt-3">
            <Button v-if="!progress" :label="$t('message.search')" @click="submit()" icon="pi pi-send"
                iconPos="right"></Button>
            <ProgressSpinner v-if="progress" style="width:50px;height:50px" strokeWidth="8" fill="var(--surface-ground)"
                animationDuration=".5s" aria-label="Custom ProgressSpinner" />
        </div>
        <div class="col-12">
            <DataTable :value="table" responsiveLayout="scroll" groupRowsBy="product.teste" sortMode="single" :loading="progress"
            sortField="product.teste" :sortOrder="1">
                <Column field="material" header="Material"></Column>
                <Column field="year" header="Year"></Column>
                <Column field="mat_desc" header="Descrição"></Column>
                <Column field="plant" header="Plant"></Column>
                <Column field="comp" header="Massa"></Column>
                <Column field="raw" header="Materia Prima"></Column>
                <Column field="value" header="Values">
                    <template #body="slotProps">
                        <tr>
                            <td>STD</td>
                        </tr>
                        <tr>
                            <td>KG</td>
                        </tr>
                        <tr>
                            <td>MT</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="PDG">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[0][3] + slotProps.data.array_agg[0][4]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[0][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[0][2]}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="JAN">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[1][5] + slotProps.data.array_agg[1][6]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[1][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[1][2]}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="FEB">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[2][5] + slotProps.data.array_agg[2][6]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[2][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[2][2]}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="MAR">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[3][5] + slotProps.data.array_agg[3][6]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[3][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[3][2]}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="APR">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[4][5] + slotProps.data.array_agg[4][6]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[4][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[4][2]}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="MAI">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[5][5] + slotProps.data.array_agg[5][6]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[5][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[5][2]}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="JUN">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[6][5] + slotProps.data.array_agg[6][6]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[6][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[6][2]}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="JUL">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[7][5] + slotProps.data.array_agg[7][6]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[7][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[7][2]}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="AUG">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[8][5] + slotProps.data.array_agg[8][6]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[8][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[8][2]}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="SEP">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[9][5] + slotProps.data.array_agg[9][6]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[9][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[9][2]}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="OCT">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[10][5] + slotProps.data.array_agg[10][6]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[10][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[10][2]}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="NOV">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[11][5] + slotProps.data.array_agg[11][6]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[11][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[11][2]}}</td>
                        </tr>
                    </template>
                </Column>
                <Column field="value" header="DEC">
                    <template #body="slotProps">
                        <tr>
                            <td>{{slotProps.data.array_agg[12][5] + slotProps.data.array_agg[12][6]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[12][1]}}</td>
                        </tr>
                        <tr>
                            <td>{{slotProps.data.array_agg[12][2]}}</td>
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
import ColumnGroup from "primevue/columngroup";
import Row from "primevue/row";
import ProgressSpinner from 'primevue/progressspinner';
import axios from "axios";
import { useDtcStore } from '../../store/dtc';
import { ref, onMounted } from "vue";
const dtc = useDtcStore()
const plant = ref([]);
const plantSelected = ref([]);
const year = ref([]);
const table = ref([])
const progress = ref(false)
const getPlant = async () => {
    plant.value = await dtc.setPlant()
};
onMounted(async () => {
    getPlant()
    const d = new Date()
    year.value = d.getFullYear()
})
const submit = async () => {
    progress.value = true
    const response = await axios.get("http://localhost:8000/api/v1/multselect/raw")
    table.value = response.data
    table.value.forEach((element, index) => {
        var array = []
        for (let index = 0; index < 13; index++) {
           var searchFind = element.array_agg.find(el => {
            return el[0] == index || (el[0] == 'std' && index == 0)
        })
          if(searchFind){
            array.push(searchFind)
          }else{
            array.push([index,'-','-','-','-','-','-'])
          }         
        }
        element.array_agg = array
    });
    progress.value = false
}
</script>