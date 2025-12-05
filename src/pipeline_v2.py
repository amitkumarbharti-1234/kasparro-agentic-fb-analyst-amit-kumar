import os
import json
import uuid
import pandas as pd

from config import CONFIG
from utils.logging_utils import get_logger
from utils.schema_utils import validate_schema
from metrics_v2 import compute_basic_kpis, split_baseline_current, aggregate_by_segment
from evaluator_v2 import build_hypotheses
from creatives_v2 import generate_creatives_from_hypotheses, save_creatives

logger = get_logger("pipeline_v2")


def ensure_dirs():
    os.makedirs(CONFIG["output_dir"], exist_ok=True)
    os.makedirs(CONFIG["log_dir"], exist_ok=True)


def run_pipeline_v2():
    run_id = str(uuid.uuid4())
    ensure_dirs()

    logger.info("V2 pipeline started", extra={"run_id": run_id})

    try:
        df = pd.read_csv(CONFIG["input_path"])
        logger.info("Loaded dataset", extra={"rows": len(df), "run_id": run_id})

        # schema validation
        validate_schema(df, run_id=run_id)

        # KPI computation
        df_kpi = compute_basic_kpis(df)

        # split into baseline vs current
        baseline_df, current_df = split_baseline_current(df_kpi)

        # -------- MULTI-LEVEL SEGMENTATION -----------
        segment_cols = [
            "campaign_name",
            "adset_name",
            "placement",
            "device_platform"
        ]

        baseline_metrics = aggregate_by_segment(baseline_df, segment_cols)
        current_metrics = aggregate_by_segment(current_df, segment_cols)
        # ----------------------------------------------

        # build hypotheses
        hypotheses = build_hypotheses(
            baseline_metrics,
            current_metrics,
            segment_key="campaign_name"
        )

        hypotheses_path = os.path.join(CONFIG["output_dir"], "hypotheses_v2.json")
        with open(hypotheses_path, "w") as f:
            json.dump(hypotheses, f, indent=4)

        # generate creatives
        creatives = generate_creatives_from_hypotheses(hypotheses)
        creatives_path = os.path.join(CONFIG["output_dir"], "creatives_v2.json")
        save_creatives(creatives, creatives_path)

        logger.info(
            "V2 pipeline completed successfully",
            extra={"run_id": run_id, "hypotheses": len(hypotheses)}
        )

        return {
            "status": "success",
            "run_id": run_id,
            "hypotheses_path": hypotheses_path,
            "creatives_path": creatives_path
        }

    except Exception as e:
        logger.error(
            f"V2 pipeline failed: {e}",
            extra={"run_id": run_id, "error_type": type(e).__name__}
        )
        return {"status": "failed", "error": str(e), "run_id": run_id}


if __name__ == "__main__":
    run_pipeline_v2()
