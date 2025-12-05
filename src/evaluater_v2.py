from typing import List, Dict
import numpy as np
import pandas as pd
from utils.logging_utils import get_logger
from config import CONFIG

logger = get_logger("evaluator_v2")

def classify_impact(rel_delta: float) -> str:
    rel_delta_abs = abs(rel_delta)
    if rel_delta_abs >= CONFIG["high_impact_threshold"]:
        return "high"
    if rel_delta_abs >= CONFIG["medium_impact_threshold"]:
        return "medium"
    return "low"


def estimate_confidence(clicks_baseline: float, clicks_current: float, rel_delta: float) -> float:
    total_clicks = clicks_baseline + clicks_current
    clicks_factor = min(total_clicks / 10000.0, 1.0)
    delta_factor = min(abs(rel_delta) / 0.5, 1.0)

    raw_score = 0.3 + 0.65 * (0.5 * clicks_factor + 0.5 * delta_factor)
    return float(round(raw_score, 2))


def build_hypotheses(
    baseline_metrics: pd.DataFrame,
    current_metrics: pd.DataFrame,
    segment_key: str = "campaign_name"
) -> List[Dict]:

    b = baseline_metrics.copy().add_prefix("baseline_")
    c = current_metrics.copy().add_prefix("current_")

    merged = b.merge(
        c,
        left_on=f"baseline_{segment_key}",
        right_on=f"current_{segment_key}",
        how="inner"
    )

    hypotheses = []

    for _, row in merged.iterrows():
        segment = row.get(f"baseline_{segment_key}", "overall")

        base_ctr = row.get("baseline_ctr", np.nan)
        curr_ctr = row.get("current_ctr", np.nan)
        base_clicks = row.get("baseline_clicks", 0.0)
        curr_clicks = row.get("current_clicks", 0.0)

        if np.isnan(base_ctr) or base_ctr == 0:
            continue

        rel_delta = (curr_ctr - base_ctr) / base_ctr

        if abs(rel_delta) < CONFIG["ctr_drop_threshold"]:
            continue

        impact = classify_impact(rel_delta)
        confidence = estimate_confidence(base_clicks, curr_clicks, rel_delta)

        hypotheses.append({
            "hypothesis": f"CTR changed by {rel_delta:.2%} for segment '{segment}'.",
            "evidence": {
                "segment": segment,
                "ctr_baseline": float(base_ctr),
                "ctr_current": float(curr_ctr),
                "ctr_delta_relative": float(round(rel_delta, 4)),
                "clicks_baseline": int(base_clicks),
                "clicks_current": int(curr_clicks)
            },
            "impact": impact,
            "confidence": confidence
        })

    logger.info("Generated hypotheses", extra={"count": len(hypotheses)})

    return hypotheses
