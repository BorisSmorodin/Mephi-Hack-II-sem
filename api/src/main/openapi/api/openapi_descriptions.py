from sanic_ext.extensions.openapi import openapi

from .request_schemas import PredictRequest
from .response_schemas import PredictResponse


perdict_desctiption = openapi.definition(
    summary="Роут для предикта целевой величины",
    body={
        "application/json": PredictRequest.model_json_schema(
            ref_template="#/components/schemas/{model}"
        )
    },
    response=[
        openapi.definitions.Response(
            status=200,
            content={
                "application/json": PredictRequest,
            },
            description="Предикт выполнен успешно. Возвращает список сессий и вероятность конверсионности"
        )
    ]
)