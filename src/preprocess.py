import pandas as pd
import numpy as np

def preprocess(df):

    numeric_cols = ['impressions', 'clicks', 'spend', 'conversions']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
        else:
            df[col] = 0  

    df['ctr'] = df['clicks'] / df['impressions'].replace(0, np.nan)
    df['cpc'] = df['spend'] / df['clicks'].replace(0, np.nan)
    df['cpa'] = df['spend'] / df['conversions'].replace(0, np.nan)

    return df

if __name__ == "__main__":
    df = pd.read_csv(r"C:\Users\Amit\Downloads\synthetic_fb_ads_undergarments.csv")
    df = preprocess(df)
    print(df.head())
    print("Impressions:", df['impressions'].sum())
print("Clicks:", df['clicks'].sum())
print("Spend:", df['spend'].sum())
