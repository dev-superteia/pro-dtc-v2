from app.db.repositories import MaterialCostRepository, rawMaterial, MdMaterialRepository
from sqlalchemy.ext.asyncio import AsyncSession
import re
from decimal import Decimal



class Tissue:
    def __init__(self, plant = '', cloth = '', filter = None, month = None, year = None):
        # Filter Initial Value
        self.plant = plant
        self.cloth = cloth
        self.filter = filter
        self.month = month
        self.year = year
        # me values
        self.mat_me = ''
        self.mat_me_weight = Decimal(0)
        self.mat_me_cost_std = Decimal(0)
        self.mat_me_cost_eff = Decimal(0)
        self.mat_me_explode = None
        # mp values
        self.mat_mp = ''
        self.weight_mp = Decimal(0)
        self.cost_mp_std = Decimal(0)


async def table_presentation_convert_in_card(cloth, db):    
    print(cloth.mat_mp,"novo")
    description = await MaterialCostRepository.description(db, cloth.mat_mp)
    print(description,"bate")
    if (description == []):
        return []
    description = description[0][0]
    card = {
        'compound_name': cloth.mat_me,
        'compound_weight': cloth.mat_me_weight,
        'me_total_raw_materials': len(cloth.mat_me_explode['table']),
        'me_total_cost_std': cloth.mat_me_cost_std,
        'me_total_cost_eff': cloth.mat_me_cost_eff,
        'coupound_cost_std': Decimal(cloth.mat_me_weight*cloth.mat_me_cost_std),
        'coupound_cost_eff': Decimal(cloth.mat_me_weight*cloth.mat_me_cost_eff),
        'fabric_name': cloth.mat_mp  + ' - ' + str(description),
        'fabric_weight': cloth.weight_mp,
        'mat_mp_cost_std': cloth.cost_mp_std,
        'mat_mp_cost_eff': cloth.cost_mp_eff,
        'fabric_cost_std': Decimal(cloth.cost_mp_std * cloth.weight_mp),
        'fabric_cost_eff': Decimal(cloth.cost_mp_eff * cloth.weight_mp),
        'total_weight':Decimal(cloth.mat_me_weight + cloth.weight_mp),
        'total_cost_std': Decimal((cloth.mat_me_weight*cloth.mat_me_cost_std)+(cloth.cost_mp_std * cloth.weight_mp)),
        'total_cost_eff': Decimal((cloth.mat_me_weight*cloth.mat_me_cost_eff)+(cloth.cost_mp_eff * cloth.weight_mp)),
        }
    return card
def table_presentation_convert_in_list(self):

        items = [
            {'name': self.mat_me, 'weight': self.mat_me_weight,
             'cost_std': Decimal(self.mat_me_weight*self.mat_me_cost_std),
             'cost_eff': Decimal(self.mat_me_weight*self.mat_me_cost_eff)},
            {'name': self.mat_mp, 'weight': self.weight_mp,
             'cost_std': Decimal(self.cost_mp_std * self.weight_mp),
             'cost_eff': Decimal(self.cost_mp_eff * self.weight_mp)},
            {'name': 'Total', 'weight': Decimal(self.mat_me_weight + self.weight_mp),
             'cost_std': Decimal((self.mat_me_weight*self.mat_me_cost_std)+(self.cost_mp_std * self.weight_mp)),
             'cost_eff': Decimal((self.mat_me_weight*self.mat_me_cost_eff)+(self.cost_mp_eff * self.weight_mp))},
        ]
        return items


def months_index(index):

    monthsLine = ['cost_std','cost_m01','cost_m01','cost_m02','cost_m03','cost_m04','cost_m05','cost_m06','cost_m07','cost_m08','cost_m09','cost_m11','cost_m12']

    return monthsLine[index]    




async def get_cloth_month(self, db):
    
    # se for std busco em especstdtm
    if (self.month == 0):
        cloth_content = await MdMaterialRepository.find_by_materialtm(db,self.plant, self.cloth, self.year)
        print(cloth_content,"teste")
        if (cloth_content == None):
            return {'status': False, 'msg': 'Not reciple in this month'}
        self.mat_me = cloth_content.comp_material
        self.mat_me_weight = Decimal(cloth_content.comp_weight)
        self.mat_mp = cloth_content.raw_material
        self.weight_mp = Decimal(cloth_content.raw_weight)
    else:
        if re.search("^(S|Y)TM.+$",self.cloth):
            cloth_content = await MdMaterialRepository.find_by_material78(db, self.plant, self.cloth, self.month, self.year)
            if (cloth_content == None):
                return {'status': False, 'msg': 'Not reciple in this month'}
            self.mat_me = cloth_content.mat_me
            self.mat_me_weight = Decimal(cloth_content.me_weight)
            self.mat_mp = cloth_content.mat_mp
            self.weight_mp = Decimal(cloth_content.mp_weight)

        elif re.search("^(S|Y)TT.+$",self.cloth):
            cloth_content = await MdMaterialRepository.find_by_material58(db, self.plant, self.cloth, self.month, self.year)
            if (cloth_content == None):
                return {'status': False, 'msg': 'Not reciple in this month'}
            self.mat_me = cloth_content.mat_me
            self.mat_me_weight = Decimal(cloth_content.me_weight)
            self.mat_mp = cloth_content.componente
            self.weight_mp = Decimal(cloth_content.mp_weight)

    # insiro o custo self.cost_mp
    try:
        self.cost_mp_std = Decimal(await MaterialCostRepository.find_by_material(db, self.mat_mp, months_index(0)))
    except:
        self.cost_mp_std = Decimal(0)

    try:
        self.cost_mp_eff = Decimal(await MaterialCostRepository.find_by_material(db, self.mat_mp, months_index(self.month)))
    except:
        self.cost_mp_eff = Decimal(0)

    # insiro os mp
    raw_materials = rawMaterial()
    raw_materials_explosion = await rawMaterial.get_raw_material_list_explosion(db=db,plant=self.plant, materialName=self.mat_me, filterType=1, month=self.month, year=self.year)
    raw_materials_explosion_calculate = await rawMaterial.get_calculate_totals_raw_material_list(db, raw_materials_explosion, self.plant, self.mat_me, self.year, self.month)
    self.mat_me_explode = raw_materials_explosion_calculate
    self.mat_me_cost_eff = raw_materials_explosion_calculate['card']['totalCostEff']
    self.mat_me_cost_std = raw_materials_explosion_calculate['card']['totalCostStd']
    return {'status': True, 'msg': 'success'}
    
tissue = Tissue()