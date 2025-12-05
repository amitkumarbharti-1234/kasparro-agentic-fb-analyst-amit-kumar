import numpy as np
from math import sqrt
from utils.logging_utils import get_logger

logger = get_logger("statistics_v3")

def ctr_z_test(clicks_baseline, impressions_baseline, clicks_current, impressions_current):
    """
    Two-proportion z-test for CTR change significance
    Returns p-value and significance flag
    """

    if impressions_baseline == 0 or impressions_current == 0:
        logger.warning("Cannot run z-test due to zero impressions")
        return None, False, 0.0

    p1 = clicks_baseline / impressions_baseline
    p2 = clicks_current / impressions_current

    p_pool = (clicks_baseline + clicks_current) / (impressions_baseline + impressions_current)
    se = sqrt(p_pool * (1 - p_pool) * (1/impressions_baseline + 1/impressions_current))

    if se == 0:
        return None, False, 0.0

    z_score = (p2 - p1) / se

    p_value = np.exp(-0.717*z_score - 0.416*(z_score**2))  # approximation formula

    significance = p_value < 0.05  # 95% confidence threshold

    confidence = round((1 - p_value) * 100, 2)

    return float(round(p_value, 6)), significance, confidence
