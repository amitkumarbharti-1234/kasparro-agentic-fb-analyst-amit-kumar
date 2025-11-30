Kasparro Agentic FB Analyst – Assignment

This repository contains the solution for the Kasparro Applied AI Engineer assignment.

Objective

Analyze the synthetic Facebook Ads dataset for an undergarments brand and generate:

Performance insights (insights.json)

Creative clustering and insights (creatives.json)

Final marketing optimization report (report.md)

Repository Structure
kasparro-agentic-fb-analyst-amit-kumar/
├─ data/               → dataset
├─ notebooks/          → EDA notebooks
├─ src/                → main pipeline and agents
├─ outputs/            → generated reports and json insights
└─ README.md           → documentation

How to Run
Install dependencies
pip install -r requirements.txt

Run pipeline scripts
python src/analyze.py data/synthetic_fb_ads_undergarments.csv
python src/creatives.py data/synthetic_fb_ads_undergarments.csv
python src/generate_report.py

Output files are saved in:
outputs/insights.json
outputs/creatives.json
outputs/report.md

Deliverables
File	Description
insights.json	Performance insights and KPI metrics
creatives.json	Creative analysis and clustering summary
report.md	Final optimization recommendations
Design Choices

This project is structured with a modular multi-agent architecture to enable scalability, clarity, and independent component improvements.

Component	Responsibility
Ingestion & Validation	Load dataset, validate schema, detect drift
Insights Agent	CTR, CPC, spend metrics and performance insights
Creative Agent	Creative text and theme analysis
Evaluation Agent	Validate and refine generated insights
Logging System	Structured JSON logging
Retry System	Resilience with backoff retry mechanism
Orchestrator	Pipeline coordination and execution management
Assumptions

Dataset contains impressions, clicks, spend columns.

Conversion data is not included; therefore CPA cannot be calculated.

Dataset follows a Facebook Ads export-like format.

LLM reasoning requires an API key.

Data is synthetic and simulates real-world ad performance.

Limitations

CPA and ROAS cannot be computed due to missing conversion and revenue data.

No UI dashboard or visualization layer.

Retry logic applies only to LLM calls.

Insights do not include statistical confidence scoring.

Future Improvements

Add conversion tracking and ROAS calculations.

Add Langfuse or MLFlow observability and monitoring.

Introduce checkpointing for pipeline state saving.

Visual dashboards for insights and trends.

Creative clustering using ML models instead of heuristics.

Example Output Summary (Based on dataset used)
Metric	Value
Total Impressions	1,190,236,513
Total Clicks	15,071,264
Total Spend	₹2,105,579.90
CTR	1.27%
CPC	₹0.14
CPA	Not available (conversion column missing)
Release Notes (v1.1)
- Added structured JSON logging
- Added retry logic with exponential backoff
- Added schema validation and drift detection
- Updated documentation and improved engineering clarity

Author

Amit Kumar
Kasparro Applied AI Engineer Assignment Submission
