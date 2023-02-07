<template>   
    <PanelMenu :model="items"  v-model:expandedKeys="expandedKeys">
      <template class="mb-2" #item="{item}">       
          <router-link v-if="item.to" :to=item.to><i v-tooltip.left=item.label :class=item.icon ></i
              ><span
                class="link"              
              >{{item.label}}</span
            ></router-link>
          <a v-else><i :class=item.icon></i
              ><span
                class="link"
              >{{item.label}}</span
            ></a>
      </template>
  </PanelMenu>
  </template>
  <script setup>
  import { ref } from 'vue';
  import PanelMenu from 'primevue/panelmenu';
  import {getMenuData} from '@/helpers/menu/index.js'
          const expandedKeys = ref({});
          const items = ref(getMenuData);
  
          const expandAll = () => {
              for (let node of nodes.value) {
                  expandNode(node);
              }
  
              expandedKeys.value = {...expandedKeys.value};
          };
          const collapseAll = () => {
              expandedKeys.value = {};
          };
          const expandNode = (node) => {
              if (node.children && node.children.length) {
                  expandedKeys.value[node.key] = true;
  
                  for (let child of node.children) {
                      expandNode(child);
                  }
              }
          };
  
  </script>
  
  <style lang="css">
  .p-panelmenu .p-panelmenu-panel {
     margin-bottom: 5px !important; 
  }
  .p-panelmenu .p-panelmenu-header .p-panelmenu-header-content {
      padding: 0.5rem !important;
      transition-duration: 150ms !important;
      border: none !important; 
      background-color: transparent !important;
      color: var(--primary-color-text) !important;
      display: flex !important;
      flex-direction: column;
      cursor: pointer;
      margin: 5px;
  }
  .p-panelmenu-content{
      margin: 5px;
  }
  .p-menuitem-content{
      padding-left: 10px;
      cursor: pointer;
      margin-bottom: 5px;
  }
  .p-tooltip{
      left: 50px !important;
  }
  .p-menuitem-content a {
    width: 100% !important;
    display: inline-block;
    text-decoration: none;
}
  </style>