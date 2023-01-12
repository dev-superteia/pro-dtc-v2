from app.core.config import settings
from fastapi import FastAPI, Request, Response
from fastapi_redis_cache import FastApiRedisCache, cache, cache_one_day
from sqlalchemy.orm import Session
import logging
from fastapi.middleware.cors import CORSMiddleware
from app.api.api_v1.api import api_router
from app.core.logging_setup import setup_root_logger
import os
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

# setup root logger
setup_root_logger()

# Get logger for module
LOGGER = logging.getLogger(__name__)


LOGGER.info("---Starting App---")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/health")
def health():
    return {"message": "ok!"}

LOCAL_REDIS_URL = "redis://:devpassword@redis:6379"

@app.on_event("startup")
def startup():
    redis_cache = FastApiRedisCache()
    redis_cache.init(
        host_url=os.environ.get("REDIS_URL", LOCAL_REDIS_URL),
        prefix="myapi-cache",
        response_header="X-MyAPI-Cache",
        ignore_arg_types=[Request, Response, Session]
    )
    
# WILL NOT be cached
@app.get("/data_no_cache")
def get_data():
    return {"success": True, "message": "this data is not cacheable, for... you know, reasons"}

# Will be cached for one year
@app.get("/immutable_data")
@cache()
async def get_immutable_data():
    return {"success": True, "message": "this data can be cached indefinitely"}    

# Will be cached for thirty seconds
@app.get("/dynamic_data")
@cache_one_day()
def partial_cache_one_day(response: Response):
    return {"success": True, "message": "this data should be cached for 24 hours"}