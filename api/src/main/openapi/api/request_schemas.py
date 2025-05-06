from pydantic import BaseModel
from sanic_ext.extensions.openapi import openapi


@openapi.component
class FeaturesData(BaseModel):
    # Категориальные признаки
    utm_source: str
    utm_medium: str
    device_browser: str
    geo_country: str
    geo_city: str
    traffic_type_cat: str

    # Числовые признаки
    visit_number: int
    catalog_visits: int
    total_actions: int
    form_interactions: int
    avg_time_between_actions: float
    error_ratio: float
    screen_width: float
    screen_height: float
    pagination_clicks: int
    retry_attempts: int

    # Бинарные признаки
    is_mobile: int
    is_evening: int
    used_filters: int
    viewed_pricing: int
    multiple_sms_errors: float
    is_million: int
    is_holiday: int


@openapi.component
class SessionData(BaseModel):
    session_id: int
    client_id: int
    features: FeaturesData


@openapi.component
class PredictRequest(BaseModel):
    data: list[SessionData]