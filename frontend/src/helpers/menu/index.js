export const getMenuData = [
  {
      key: '0',
      label: 'Dashboard',
      icon: 'pi pi-fw pi-file',
  },
  {
      key: '1',
      label: 'user',
      icon: 'pi pi-fw pi-pencil',
      to:'',
      items: [         
        {
            key: '1_1',
            label: 'Product One-Level',
            icon: 'pi pi-chart-bar',
            to:'/product_one_level'
        },          
        {
            key: '1_2',
            label: 'Compound & Fabric',
            icon: 'pi pi-chart-bar',
            to:'/compound_and_fabric'
        },          
        {
            key: '1_3',
            label: 'Product-Raw Material',
            icon: 'pi pi-chart-bar',
            to:'/product_raw_material'
        },          
        {
            key: '1_4',
            label: 'Raw Material and Compound',
            icon: 'pi pi-chart-bar',
            to:'/raw_material_and_compound'
        },          
        {
            key: '1_5',
            label: 'Tissue Month',
            icon: 'pi pi-chart-bar',
            to:'/tissue_month'
        },          
        {
          key: '1_6',
          label: 'Raw Material Without Cost',
          icon: 'pi pi-chart-bar',
          to:'/raw_material_without_cost'
        },          

      ]
  },{
      key: '2',
      label: 'user',
      icon: 'pi pi-fw pi-pencil',
      to:'',
      items: [{
              key: '2_0',
              label: 'User',
              icon: 'pi pi-fw pi-align-left',
              to:''
          },
          {
              key: '2_1',
              label: 'Permission',
              icon: 'pi pi-fw pi-align-right',
              to:'/permission'
          },
          {
              key: '2_2',
              label: 'Roles',
              icon: 'pi pi-fw pi-align-right',
              to:'/roles'
          }
      ]
  },
]