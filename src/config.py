CONFIG = {
    "input_path": "data/synthetic_fb_ads_undergarments.csv",
    "output_dir": "outputs",
    "log_dir": "logs",

    # Minimum data confidence
    "min_clicks_per_segment": 1000,

    # Significant CTR change thresholds
    "ctr_drop_threshold": 0.20,        # 20% drop
    "ctr_increase_threshold": 0.20,    # 20% increase

    # Impact classification
    "high_impact_threshold": 0.30,     # >30% change
    "medium_impact_threshold": 0.15    # 15–30% change
}
