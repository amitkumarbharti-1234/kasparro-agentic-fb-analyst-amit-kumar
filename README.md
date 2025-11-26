Kasparro Agentic FB Analyst – Assignment

This repository contains the solution for the Kasparro Applied AI Engineer assignment.

Objective:
Analyze the Facebook Ads dataset for an undergarments brand and generate:
- Performance insights (insights.json)
- Creative clustering and insights (creatives.json)
- Final marketing optimization report (report.md)

Repository Structure:
kasparro-agentic-fb-analyst-<your-name>/
├─ data/ → dataset
├─ notebooks/ → EDA notebooks
├─ src/ → scripts for pipeline
├─ outputs/ → generated reports and json insights
└─ README.md

How to Run:
Install dependencies:
pip install -r requirements.txt

Run pipeline:
python src/analyze.py data/synthetic_fb_ads_undergarments.csv
python src/creatives.py data/synthetic_fb_ads_undergarments.csv
python src/generate_report.py

Outputs will be saved in:
outputs/insights.json
outputs/creatives.json
outputs/report.md

Deliverables:
- insights.json
- creatives.json
- report.md

Status:
Work in Progress (v0.1)
