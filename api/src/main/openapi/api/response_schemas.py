from pydantic import BaseModel
from sanic_ext.extensions.openapi import openapi


@openapi.component
class SingleProb(BaseModel):
    session_id: int
    client_id: int
    conversion_prob: float


@openapi.component
class PredictResponse(BaseModel):
    response: list[SingleProb]