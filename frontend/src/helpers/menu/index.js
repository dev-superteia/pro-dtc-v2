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
      items: [{
              key: '1_0',
              label: 'DTC',
              icon: 'pi pi-fw pi-align-left',
              url:'/raw_material_and_compound'
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