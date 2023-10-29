from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.weather.router import router as weather_router
from app.config import client, env, fastapi_config


app = FastAPI(**fastapi_config)


@app.on_event("shutdown")
def shutdown_db_client():
    client.close()


app.add_middleware(
    CORSMiddleware,
    allow_origins=env.CORS_ORIGINS,
    allow_methods=env.CORS_METHODS,
    allow_headers=env.CORS_HEADERS,
    allow_credentials=True,
)

app.include_router(weather_router, prefix="/weather", tags=["Weather"])
