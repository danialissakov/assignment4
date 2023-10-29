from typing import Any, List

from fastapi import Depends
from pydantic import Field

from app.utils import AppModel

from ..service import Service, get_service
from . import router


class ActsResponse(AppModel):
    response: str

@router.get("/")
def get_weatherr(
    inp: str,
    svc : Service = Depends(get_service),
):
    responce = svc.weather_service.get_weather(inp)

    print(responce)
    return responce