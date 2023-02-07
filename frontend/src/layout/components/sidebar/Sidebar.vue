<template>
  <aside  :class="toolbar ? 'toggle_aside' : ''">
    
    <nav class="sidebar">
      <div>
        <div class="m-0">
            <a href="#" class="logo"><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="24" height="24"><defs><linearGradient x1="12.581%" y1="10.333%" x2="88.841%" y2="100%" id="a"><stop stop-color="#1AD697" offset="0%"/><stop stop-color="#0019FF" offset="100%"/></linearGradient></defs><circle cx="12" cy="12" r="10" stroke="url(#a)" stroke-width="4" fill="transparent"/></svg>
              <div class="logo_name"><img src="@/assets/logo.png" style="height: 15px"/></div>
            </a>
        </div>
        <hr class="mb-5">
      <Menu></Menu>
    </div>
    </nav>
  </aside>
</template>

<script setup>
import Menu from './menu/index.vue';
import {getMenuData} from '@/helpers/menu'
import { useConfigStore } from '@/store';
import { storeToRefs } from 'pinia';
const store = useConfigStore()
const { toolbar } = storeToRefs(store);
const list = getMenuData

</script>

<style>
aside {
  transform: translateX(0px);
  background-image: url(https://demos.creative-tim.com/vue-material-dashboard/img/sidebar-2.32103624.jpg) !important;
  background-size: cover !important;
  position: fixed;
  top: 0;
  bottom: 0;
  background: #fff;
  width: 200px;
  transition: all .5s ease;
  color: var(--text-color);
}
.link{
  margin-left: 10px;  
}
.p-component, .p-component * , .link {
  text-decoration: none !important;
}
.p-panelmenu .p-panelmenu-content .p-menuitem > .p-menuitem-content{
  margin-bottom: 10px;
}
.logo_name {
  font-size: 25px;
  font-weight: 600;
  transition: all .5s ease;
  display: block;
  color: var(--green-600);
  }
  .logo{
    display: flex !important;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap: 10px;
    text-decoration: none;
    height: 43px;
  }
.toggle_aside{
  width: 50px !important;
  transition: all .5s ease;
}
.toggle_aside .logo_name {  
  display: none;
}
.toggle_aside .link{
  margin-left: 10px;
  display: block;
  position: absolute;
  background: rgba(255,255,255,0.5);
  border-radius: 100%;
  transform: scale(0);
  pointer-events: none;
}

.sidebar {
  height: 100%;
  width: 100%;
  background-color: #212b59  !important;
  color: var(--text-color) !important;
}
</style>
