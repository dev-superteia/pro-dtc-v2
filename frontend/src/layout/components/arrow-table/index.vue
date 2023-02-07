<template>
    <tr v-if="(value.eff == 'undefined') || (value.eff == '--') || ((value.eff == 0) && (value.std == 0) || (value.std == 'undefined') || (value.std == '--') )">
        <td>--</td>
    </tr>
    <tr v-else>
        <td v-if="(parseFloat(value.std) == parseFloat(value.eff))" style="color:#03966f;">{{parseFloat(value.eff)}}<span style="color: #03966f;margin-left: 5px;">=</span></td>
        <td v-if="(parseFloat(value.std) < parseFloat(value.eff))" style="color:#fc0303;">{{parseFloat(value.eff)}}<i class="pi pi-arrow-down" style="color: #fc0303;margin-left: 5px;"></i></td>
        <td v-if="(parseFloat(value.std) > parseFloat(value.eff))" style="color:#03966f;">{{parseFloat(value.eff)}}<i class="pi pi-arrow-up" style="color: #03966f;margin-left: 5px;"></i></td>
    </tr>

</template>

<script setup>
import {PrimeIcons} from 'primevue/api';
import {computed, ref } from 'vue';
import { useConfigStore } from '@/store/config';
import { storeToRefs } from 'pinia';
const config = useConfigStore()
const { fixed } = storeToRefs(config);
const props = defineProps({
    value: Object
})
const fixedRef = ref(3)
computed(() => {
    console.log(fixed);
    fixedRef.value = fixed
});
</script>
