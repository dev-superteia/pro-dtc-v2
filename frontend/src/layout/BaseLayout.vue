<script setup>
import  Navbar from '../layout/components/app-navbar/Navbar.vue'
import  Sidebar from '../layout/components/sidebar/Sidebar.vue'
import { useConfigStore } from '@/store';
import { storeToRefs } from 'pinia';
const store = useConfigStore()
const { toolbar } = storeToRefs(store);

const changeTheme = (event) => {
    let themeElement = document.getElementById('theme-link')
    themeElement.setAttribute('href', '/node_modules/primevue/resources/themes/tailwind-light/theme.css');
}
</script>

<template>
    <section :class="toolbar ? 'section-toggle' : ''"> 
        <router-view />
        <!-- <Button  @click="changeTheme()"> testegggggggggggggggggggggggg</Button> -->
    </section>
    <Navbar> </Navbar>
    <Sidebar></Sidebar>    
</template>

<style>
body {
  margin: 0 !important;
  background-color: var(--surface-ground);
}
section{
    margin-top: 100px;
    margin-right:30px ;
    margin-left:250px ;
    overflow: auto;
    }
.section-toggle{
    margin-left: 100px;
}    
</style>