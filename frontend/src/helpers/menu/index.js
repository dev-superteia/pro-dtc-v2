export const getMenuData = [
  {
      key: '0',
      label: 'Dashboard',
      icon: 'pi pi-fw pi-file',
      url:''
  },
  {
      key: '1',
      label: 'user',
      icon: 'pi pi-fw pi-pencil',
      items: [
        {
              key: '1_0',
              label: 'DTC',
              icon: 'pi pi-fw pi-align-left',
              url:'/raw_material_and_compound'
        },          
        {
            key: '1_1',
            label: 'Product One-Level',
            icon: 'pi pi-fw pi-align-left',
            url:'/product_one_level'
        },          
        {
            key: '1_2',
            label: 'Compound & Fabric',
            icon: 'pi pi-fw pi-align-left',
            url:'/compound_and_fabric'
        },          
        {
            key: '1_3',
            label: 'Product-Raw Material',
            icon: 'pi pi-fw pi-align-left',
            url:'/product_raw_material'
        },          
        {
            key: '1_4',
            label: 'Raw Material and Compound',
            icon: 'pi pi-fw pi-align-left',
            url:'/raw_material_and_compound'
        },          
        {
            key: '1_5',
            label: 'Tissue Month',
            icon: 'pi pi-fw pi-align-left',
            url:'/tissue_month'
        },          
        {
          key: '1_6',
          label: 'Raw Material Without Cost',
          icon: 'pi pi-fw pi-align-left',
          url:'/raw_material_without_cost'
        },          
      ]
  },{
      key: '2',
      label: 'user',
      icon: 'pi pi-fw pi-pencil',
      items: [{
              key: '2_0',
              label: 'User',
              icon: 'pi pi-fw pi-align-left',
              url:''
          },
          {
              key: '2_1',
              label: 'Permission',
              icon: 'pi pi-fw pi-align-right',
              url:'/permission'
          },
          {
              key: '2_2',
              label: 'Roles',
              icon: 'pi pi-fw pi-align-right',
              url:'/roles'
          }
      ]
  },
]