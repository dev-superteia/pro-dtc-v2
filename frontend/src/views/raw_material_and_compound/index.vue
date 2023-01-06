<template>
<h3>Raw Material and Compound</h3>

<h5>Addons</h5>
        <div class="grid p-fluid">
            <div class="col-12">
                <div class="p-inputgroup">
                    <Dropdown optionLabel="plant" placeholder="Select a plant" />
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
        </div>

</template>
<script setup>
import Dropdown from 'primevue/dropdown';
</script>