import json
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer
from utils.logging_utils import get_logger

logger = get_logger("creative_clustering_v3")


def creative_cluster_analysis(df: pd.DataFrame, num_clusters: int = 5):
    """
    Cluster creative text using sentence embeddings + KMeans
    """
    if "primary_text" not in df.columns:
        logger.warning("primary_text column missing, skipping creative clustering")
        return []

    model = SentenceTransformer("all-MiniLM-L6-v2")

    texts = df["primary_text"].astype(str).tolist()
    embeddings = model.encode(texts)

    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    clusters = kmeans.fit_predict(embeddings)

    df["cluster"] = clusters

    cluster_summary = (
        df.groupby("cluster")
        .agg(
            avg_ctr=("ctr", "mean"),
            avg_cpc=("cpc", "mean"),
            count=("cluster", "count"),
            sample_text=("primary_text", lambda x: x.iloc[0])
        )
        .reset_index()
        .sort_values(by="avg_ctr", ascending=False)
    )

    results = cluster_summary.to_dict(orient="records")

    logger.info("Creative clustering complete", extra={"clusters": len(results)})

    return results


def save_creative_clusters(results, path):
    with open(path, "w") as f:
        json.dump(results, f, indent=4)
