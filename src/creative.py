import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
def cluster_creatives(df, n_clusters=4):
    df['text'] = df['headline'].fillna('') + " " + df['body'].fillna('')
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df['text'])
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['cluster'] = kmeans.fit_predict(X)
    clusters = {}
    for c in range(n_clusters):
        members = df[df['cluster'] == c]
        clusters[c] = {
            "count": len(members),
            "sample_headlines": members['headline'].dropna().unique().tolist()[:5]
        }
    return clusters
if __name__ == "__main__":
    df = pd.read_csv("data/synthetic_fb_ads_undergarments.csv")
    clusters = cluster_creatives(df)
    with open("outputs/creatives.json", "w") as f:
        json.dump(clusters, f, indent=4)
    print("creatives.json created")
