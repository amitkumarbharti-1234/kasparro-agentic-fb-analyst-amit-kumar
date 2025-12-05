Kasparro Agentic FB Analyst – Assignment (Advanced V3 Submission)

This repository contains the solution for the Kasparro Applied AI Engineer assignment.
The system analyzes synthetic Facebook Ads performance data for an undergarments brand and generates actionable marketing insights, creative strategy, and CTR forecasting using a multi-agent AI pipeline enhanced with machine learning and observability.

Objective

Analyze the dataset and generate:

Performance diagnosis and hypotheses (hypotheses_v2.json)

Creative optimization recommendations (creatives_v2.json)

Creative semantic clustering (creative_clusters_v3.json)

CTR forecasting and budget recommendations (forecast_v3.json)

Interactive dashboard for visualization (dashboard_app.py)

System Architecture (High-Level Design)
            ┌──────────────────────────┐
            │     User Upload / Input  │
            └────────────┬─────────────┘
                         │ CSV
                         ▼
                ┌──────────────────┐
                │   Data Ingestion  │
                └─────────┬────────┘
                          ▼
                ┌──────────────────┐
                │ Data Validation   │  ← Schema check + logging
                └─────────┬────────┘
                          ▼
                ┌──────────────────┐
                │   KPI Builder     │  CTR, CPC, Spend
                └─────────┬────────┘
                          ▼
            ┌───────────────────────────────┐
            │ Baseline vs Current Split      │
            └────────────┬──────────────────┘
                         ▼
                ┌──────────────────┐
                │ Segmentation      │ campaign / adset / placement / device
                └─────────┬────────┘
                          ▼
        ┌─────────────────────────────────────────┐
        │ Hypothesis Engine                       │
        │ (evidence, delta %, impact, confidence) │
        └───────────────────┬─────────────────────┘
                            ▼
        ┌─────────────────────────────────────────┐
        │ Creative Suggestion Builder             │
        └───────────────────┬─────────────────────┘
                            ▼
        ┌─────────────────────────────────────────┐
        │ Creative Clustering (Embeddings + ML)   │
        └───────────────────┬─────────────────────┘
                            ▼
        ┌─────────────────────────────────────────┐
        │ CTR Forecasting (Prophet)               │
        └───────────────────┬─────────────────────┘
                            ▼
                ┌───────────────────────────┐
                │   Output JSON + Dashboard  │
                └───────────────────────────┘

Repository Structure
kasparro-agentic-fb-analyst-amit-kumar/
├─ data/               → dataset
├─ notebooks/          → EDA notebooks
├─ src/                → main pipeline and modules
├─ outputs/            → generated insights and forecast files
└─ README.md           → documentation

How to Run
Install dependencies
pip install -r requirements.txt

Run analysis pipeline
python src/pipeline_v2.py

Run dashboard
streamlit run src/dashboard_app.py

Generated Output Files
File	Description
hypotheses_v2.json	Performance drivers with evidence, impact & confidence
creatives_v2.json	Creative improvements tied to hypotheses
creative_clusters_v3.json	ML-based cluster insights using embeddings and KMeans
forecast_v3.json	CTR forecast and budget recommendation
Key Features

Multi-agent modular pipeline architecture

Schema validation and drift detection

Structured logging with run-tracking and debugging context

Segmentation and baseline vs current comparison

Hypothesis engine with impact scoring and confidence metrics

Creative generation aligned with diagnosed performance

Embedding-based creative clustering (Sentence-Transformers + KMeans)

Forecasting engine using Prophet

Streamlit dashboard for interactive visual analysis

Example Summary Metrics
Metric	Value
Total Impressions	1,190,236,513
Total Clicks	15,071,264
Total Spend	₹2,105,579.90
CTR	1.27%
CPC	₹0.14
Design Choices
Component	Responsibility
Data ingestion + validation	Data integrity & schema check
Metric builder	CTR, CPC, Spend calculations
Segmentation layer	Compare performance across dimensions
Hypothesis engine	Generate quantified evidence & impact
Creative agent	Strategy suggestions
Creative clustering	Theme grouping to identify winning styles
Forecasting model	Predict future CTR and recommend budget
Dashboard	Usability layer for marketing teams
Assumptions

No conversions or revenue field available → CPA and ROAS cannot be computed

Data simulates real Facebook Ads exports

Insights are derived purely from performance signals

Limitations

Forecasting model accuracy depends on dataset length

Creative insight limited to text only (no image/video analysis)

No real-time streaming yet

Future Improvements

Add CLIP-based image/video creative clustering

Add reinforcement learning for budget optimization

Deploy backend + UI on cloud infrastructure

Add Langfuse / MLFlow tools for monitoring

Real-time incremental dataset processing

Author

Amit Kumar
Kasparro Applied AI Engineer Assignment Submission
