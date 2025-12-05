import pandas as pd
import numpy as np
from utils.logging_utils import get_logger

logger = get_logger("metrics_v2")


def compute_basic_kpis(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for col in ["impressions", "clicks", "spend"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)
        else:
            df[col] = 0

    df["ctr"] = df["clicks"] / df["impressions"].replace(0, np.nan)
    df["cpc"] = df["spend"] / df["clicks"].replace(0, np.nan)

    return df


def split_baseline_current(df: pd.DataFrame):
    """
    Split data into baseline (older half) and current (recent half)
    """
    df = df.copy()
    n = len(df)
    midpoint = n // 2

    baseline_df = df.iloc[:midpoint].copy()
    current_df = df.iloc[midpoint:].copy()

    logger.info(
        "Split dataset",
        extra={"baseline_rows": len(baseline_df), "current_rows": len(current_df)}
    )

    return baseline_df, current_df


def aggregate_by_segment(df: pd.DataFrame, segment_cols=None) -> pd.DataFrame:
    """
    Aggregates performance metrics grouped by provided segment columns.
    Automatically detects existing segmentation levels.
    """
    if segment_cols is None:
        segment_cols = [
            "campaign_name",
            "adset_name",
            "placement",
            "device_platform"
        ]

    # detect existing columns
    existing = [c for c in segment_cols if c in df.columns]

    if not existing:
        logger.warning("No segmentation columns found, falling back to overall rollup.")
        df["overall"] = "all"
        existing = ["overall"]

    agg = df.groupby(existing, dropna=False).agg(
        impressions=("impressions", "sum"),
        clicks=("clicks", "sum"),
        spend=("spend", "sum")
    ).reset_index()

    # KPIs
    agg["ctr"] = agg["clicks"] / agg["impressions"].replace(0, np.nan)
    agg["cpc"] = agg["spend"] / agg["clicks"].replace(0, np.nan)

    logger.info("Aggregated metrics by segmentation", extra={"segments": existing})

    return agg
