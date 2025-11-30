import pandas as pd
import sys
from utils.schema_utils import validate_schema
def load_data(path):
    df = pd.read_csv(path)
    validate_schema(df, run_id="run-001")
    print("Rows:", len(df))
    print("Columns:", list(df.columns))
    return df

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "data/synthetic_fb_ads_undergarments.csv"
    load_data(path)
