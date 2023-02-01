from fastapi import APIRouter

from app.api.api_v1.endpoints import login, users, permission, role, role_permission, multselect, tissue, report_raw_material, raw_material_and_compound, compound_and_fabric, product_raw_material, product_one_level, report_raw_material_breakdown # noqa: E501, E261

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(role.router, prefix="/roles",
                          tags=["roles"])
api_router.include_router(permission.router, prefix="/permissions",
                          tags=["permissions"])
api_router.include_router(role_permission.router,
                          prefix="/role_permissions",
                          tags=["role_permissions"])
api_router.include_router(multselect.router,
                          prefix="/multselect",
                          tags=["multselect"])
api_router.include_router(tissue.router,
                          prefix="/tissue",
                          tags=["tissue"])
api_router.include_router(report_raw_material.router,
                          prefix="/report_raw_material_null",
                          tags=["report_raw_material_null"])
api_router.include_router(raw_material_and_compound.router,
                          prefix="/raw_material_and_compound",
                          tags=["raw_material_and_compound"])
api_router.include_router(compound_and_fabric.router,
                          prefix="/compound_and_fabric",
                          tags=["compound_and_fabric"])
api_router.include_router(product_raw_material.router,
                          prefix="/product_raw_material",
                          tags=["product_raw_material"])
api_router.include_router(product_one_level.router,
                          prefix="/product_one_level",
                          tags=["product_one_level"])
api_router.include_router(report_raw_material_breakdown.router,
                          prefix="/report_raw_material_breakdown",
                          tags=["report_raw_material_breakdown"])
