import pandas as pd
import numpy as np
from prophet import Prophet
from utils.logging_utils import get_logger

logger = get_logger("forecasting_v3")


def forecast_ctr(df: pd.DataFrame, periods: int = 7):
    if "ctr" not in df.columns:
        logger.warning("CTR column missing. Forecast unavailable.")
        return None

    if "date" not in df.columns:
        logger.warning("Date column missing. Cannot run time-series forecasting.")
        return None

    df_forecast = df[["date", "ctr"]].rename(columns={"date": "ds", "ctr": "y"})
    df_forecast["ds"] = pd.to_datetime(df_forecast["ds"], errors="coerce")
    df_forecast = df_forecast.dropna()

    if len(df_forecast) < 10:
        logger.warning("Not enough data points for model training.")
        return None

    model = Prophet()
    model.fit(df_forecast)

    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    predicted_ctr = float(forecast.iloc[-1]["yhat"])

    trend_direction = (
        "increasing" if predicted_ctr > df_forecast["y"].iloc[-1]
        else "declining" if predicted_ctr < df_forecast["y"].iloc[-1]
        else "flat"
    )

    budget_rec = (
        "increase budget on top performers"
        if trend_direction == "increasing"
        else "reduce budget and run creative experiments"
        if trend_direction == "declining"
        else "maintain steady budget"
    )

    return {
        "forecast_ctr": predicted_ctr,
        "trend_direction": trend_direction,
        "budget_recommendation": budget_rec
    }
