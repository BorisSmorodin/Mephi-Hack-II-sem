import joblib
from pandas import DataFrame

from sanic import Sanic
from sanic.request import Request
from sanic.response import JSONResponse
from sanic_ext import validate
from openapi.api import openapi_descriptions, response_schemas, request_schemas
import pandas as pd


app = Sanic("ConversionPredictApp")

model = joblib.load("api/src/main/models/stacking_model.joblib")


@app.post("/predict")
@openapi_descriptions.perdict_desctiption
@validate(json=request_schemas.PredictRequest)
async def predict(request: Request, body: request_schemas.PredictRequest) -> JSONResponse:
    flattened = []
    json_data = request.json
    for entry in json_data["data"]:
        # Создаем копию верхнего уровня
        temp = entry.copy()
        # Извлекаем и удаляем features
        features = temp.pop("features")
        # Объединяем верхние поля и features
        temp.update(features)
        flattened.append(temp)

    # Создаем датафрейм
    df = pd.DataFrame(flattened)
    print(df)
    proba = model.predict_proba(df)
    # Возвращаем вероятность конверсии
    for it in proba[0]:
        print(it)
    response = []
    for session, proba_value in zip(json_data["data"], proba):
        response.append(
            {
                "session_id": session["session_id"],
                "client_id": session["client_id"],
                "conversion_prob": proba_value[1]
            }
        )
    return JSONResponse(
        body={"conversion_prob": response}
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=11111)

