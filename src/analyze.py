import pandas as pd
import json
import numpy as np

def generate_insights(df):
    total_impr = df['impressions'].sum()
    total_clicks = df['clicks'].sum()
    total_spend = df['spend'].sum()
    total_conv = df['conversions'].sum()

    ctr = total_clicks / total_impr if total_impr > 0 else 0
    cpc = total_spend / total_clicks if total_clicks > 0 else 0
    cpa = total_spend / total_conv if total_conv > 0 else 0

    insights = {
        "total_impressions": int(total_impr),
        "total_clicks": int(total_clicks),
        "total_spend": float(total_spend),
        "total_conversions": int(total_conv),
        "ctr": ctr,
        "cpc": cpc,
        "cpa": cpa
    }

    return insights

if __name__ == "__main__":
    df = pd.read_csv("data/synthetic_fb_ads_undergarments.csv")
    insights = generate_insights(df)
    with open("outputs/insights.json", "w") as f:
        json.dump(insights, f, indent=4)
    print("insights.json created")
