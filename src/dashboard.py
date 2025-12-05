import streamlit as st
import pandas as pd
import json
import plotly.express as px

from pipeline_v2 import run_pipeline_v2
from config import CONFIG


st.set_page_config(page_title="Kasparro FB Analyst", layout="wide")

st.title("Kasparro Agentic FB Analyst Dashboard")
st.write("Advanced data + AI system for diagnosing performance shifts and generating creative strategy")


if st.button("Run Full Analysis Pipeline"):
    result = run_pipeline_v2()
    st.success("Pipeline executed successfully")
    st.json(result)


st.header("📊 Performance Insights & Hypotheses")
try:
    with open(f"{CONFIG['output_dir']}/hypotheses_v2.json", "r") as f:
        hypotheses = json.load(f)
    st.json(hypotheses)
except:
    st.warning("Run pipeline to generate hypotheses")


st.header("🎨 Creative Suggestions")
try:
    with open(f"{CONFIG['output_dir']}/creatives_v2.json", "r") as f:
        creatives = json.load(f)
    st.json(creatives)
except:
    st.warning("Run pipeline to generate creative suggestions")


st.header("🧠 Creative Clusters (ML Grouping)")
try:
    with open(f"{CONFIG['output_dir']}/creative_clusters_v3.json", "r") as f:
        clusters = json.load(f)

    df_clusters = pd.DataFrame(clusters)
    st.dataframe(df_clusters)

    fig = px.bar(df_clusters, x="cluster", y="avg_ctr", color="avg_ctr", title="Best Performing Creative Clusters")
    st.plotly_chart(fig)

except:
    st.warning("Run pipeline to generate creative clusters")


st.header("📈 CTR Forecast & Budget Recommendation")
try:
    with open(f"{CONFIG['output_dir']}/forecast_v3.json", "r") as f:
        forecast = json.load(f)
    st.json(forecast)
except:
    st.warning("Run pipeline to generate forecast")
