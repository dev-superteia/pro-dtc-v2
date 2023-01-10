from fastapi import APIRouter

from app.api.api_v1.endpoints import login, users, permission, role, role_permission, multselect, report_raw_material # noqa: E501, E261

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
api_router.include_router(report_raw_material.router,
                          prefix="/report_raw_material_null",
                          tags=["report_raw_material_null"])
