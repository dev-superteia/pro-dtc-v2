from app.db import repositories
from sqlalchemy.ext.asyncio import AsyncSession
import re
from decimal import Decimal

class rawMaterial:
    def __init__(self, 
        number_material = 0,
        raw_material = '',
        unit = '',
        cost_per_unit_std = 0.00000,
        cost_per_unit_eff = 0.00000,
        raw_weight = 0.00000,
        raw_weight_percent = 0,
        total_cost_std = 0.00000,
        total_cost_eff = 0.00000,
        plant = '',
        material = '',
        month = 0,
        year = 0
    ):
        self.number_material = number_material,
        self.raw_material = raw_material
        self.unit = unit
        self.cost_per_unit_std = cost_per_unit_std
        self.cost_per_unit_eff = cost_per_unit_eff
        self.raw_weight = raw_weight
        self.raw_weight_percent = raw_weight_percent
        self.total_cost_std = total_cost_std
        self.total_cost_eff = total_cost_eff
        self.plant = plant
        self.material = material
        self.month = month
        self.year = year

    async def get_raw_material_list_explosion(db: AsyncSession, plant, materialName, filterType, month, year):

        result = []

        if month == 0:
            material_table = await repositories.MaterialEspecStdMeRepository.explode_material(db=db, plant=plant, tm_material=materialName, year=year)
            for index, aux in enumerate(material_table):
                material = rawMaterial()
                material.number_material = (index+1),
                material.plant = plant
                material.material = materialName
                material.month = month
                material.year = year
                material.raw_material = aux.raw_material
                material.unit = await repositories.MaterialEspecZp45Repository.find_material_measure_unit(db=db, plant=plant, material=materialName, component=aux.raw_material)
                material.raw_weight = await rawWeightCalculate(db=db, plant=plant, material=material.material, rawMaterial=material.raw_material, month=month, year=year, filterType=filterType, result=aux.raw_weight)
                material.cost_per_unit_std = Decimal(await repositories.MaterialCostRepository.find_by_material(db=db, material=aux.raw_material, cost=materialCostIndex(0)))
                material.cost_per_unit_eff = Decimal(await repositories.MaterialCostRepository.find_by_material(db=db, material=aux.raw_material, cost=materialCostIndex(month)))
                material.total_cost_std = Decimal(material.cost_per_unit_std * material.raw_weight)
                material.total_cost_eff = Decimal(material.cost_per_unit_eff * material.raw_weight)
                result.append(material)

            return result
        elif (month > 0):
            material_table = await repositories.MaterialEspecZp45Repository.find_by_plant_component_month_year(db=db, plant=plant, component=materialName, month=month, year=year)
            raw_weight_index = 24

        for index, aux in enumerate(material_table):
            material = rawMaterial()
            material.number_material = (index+1),
            material.plant = plant
            material.material = materialName
            material.month = month
            material.year = year
            material.raw_material = aux.component
            material.unit = await repositories.MaterialEspecZp45Repository.find_material_measure_unit(db=db, plant=plant, material=materialName, component=aux.component)
            material.raw_weight = await rawWeightCalculate(db=db, plant=plant, material=material.material, rawMaterial=material.raw_material, month=month, year=year, filterType=filterType, result=aux.qtd_without)
            material.cost_per_unit_std = Decimal(await repositories.MaterialCostRepository.find_by_material(db=db, material=aux.component, cost=materialCostIndex(0)))
            material.cost_per_unit_eff = Decimal(await repositories.MaterialCostRepository.find_by_material(db=db, material=aux.component, cost=materialCostIndex(month)))
            material.total_cost_std = Decimal(material.cost_per_unit_std * material.raw_weight)
            material.total_cost_eff = Decimal(material.cost_per_unit_eff * material.raw_weight)
            result.append(material)

        return result


    async def get_calculate_totals_raw_material_list(db: AsyncSession, listRawMaterial, plant, material, year, month):

        card = {
            'totalRawMaterials': 0,
            'totalWeight': Decimal(0.00),
            'totalWeightPercent': Decimal(0.00),
            'totalCostStd': Decimal(0.00),
            'totalCostEff': Decimal(0.00),
            'costPerKgStd': Decimal(0.00),
            'costPerKgEff': Decimal(0.00),
            'density': Decimal(0.00),
            'costPerLiterStd': Decimal(0.00),
            'costPerLiterEff': Decimal(0.00),
        }

        table = []

        for index, aux in enumerate(listRawMaterial):
            card['totalWeight'] += aux.raw_weight
            card['totalCostStd'] += aux.total_cost_std
            card['totalCostEff'] += aux.total_cost_eff

        if (card['totalWeight'] > 0):
            card['costPerKgStd'] = Decimal(card['totalCostStd'] / card['totalWeight'])
            card['costPerKgEff'] = Decimal(card['totalCostEff'] / card['totalWeight'])
        else:
            card['costPerKgStd'] = Decimal(0.00)
            card['costPerKgEff'] = Decimal(0.00)

        card['density'] = await repositories.MdMaterialRepository.find_density(db=db, plant=plant, material=material, year=year, month=month)
        card['costPerLiterStd'] = card['costPerKgStd'] * card['density']
        card['costPerLiterEff'] = card['costPerKgEff'] * card['density']

        for index, aux in enumerate(listRawMaterial):
            card['totalRawMaterials'] = (index+1)
            aux.raw_weight_percent = aux.raw_weight / card['totalWeight'] * 1
            card['totalWeightPercent'] += aux.raw_weight_percent
            table.append(aux.__dict__)

        return {
            'card': card,
            'table': table
        }



async def rawWeightCalculate(db: AsyncSession, plant, material, rawMaterial, month, year, filterType, result):
    if(int(filterType) == 1 and re.search("^RG.+$",rawMaterial)):
        result = 0

    if(int(filterType) == 3):
        try:
            result = repositories.MaterialEspecZp45Repository.find_material_utilization(db=db, plant=plant, material=material, component=rawMaterial, month='02', year=year)
        except:
            result = Decimal(0)

    return result

def materialCostIndex(index):

    costIndex = ['cost_std', 'cost_m01', 'cost_m02', 'cost_m03', 'cost_m04', 'cost_m05', 'cost_m06', 'cost_m07', 'cost_m08', 'cost_m09', 'cost_m10', 'cost_m11', 'cost_m12']

    return costIndex[int(index)]