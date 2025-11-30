import pandas as pd
from utils.logging_utils import get_logger
from typing import List

logger = get_logger("schema")

REQUIRED_COLUMNS = [
    "campaign_name",
    "adset_name",
    "ad_name",
    "impressions",
    "clicks",
    "spend"
]

def validate_schema(df: pd.DataFrame, run_id: str = "run-001"):
    current_columns = list(df.columns)

    missing = [c for c in REQUIRED_COLUMNS if c not in current_columns]
    extra = [c for c in current_columns if c not in REQUIRED_COLUMNS]

    if missing:
        logger.warning(
            f"Missing required columns: {missing}",
            extra={"run_id": run_id, "missing": missing}
        )

    if extra:
        logger.info(
            f"Extra optional columns found: {extra}",
            extra={"run_id": run_id, "extra": extra}
        )

    if missing:
        raise ValueError(f"Schema validation failed. Missing: {missing}")

    logger.info(
        "Schema validation successful",
        extra={"run_id": run_id, "columns": current_columns}
    )
