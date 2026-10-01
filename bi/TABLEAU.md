# Tableau dashboard build guide

Status: CSV exports and exact build specifications supplied; no Tableau workbook has been created or published. Build these in Tableau Desktop/Public after regenerating data. Every workbook title must include “Synthetic portfolio study.”

## 01 — Paid Media Performance

Connect to `data/campaign_daily.csv` as Text File. Set `date` to Date, spend/revenue to decimal, counts to whole numbers, and categorical IDs to strings.

Calculated fields:

```text
Media CAC = IF SUM([new_members]) > 0 THEN SUM([spend_usd])/SUM([new_members]) END
CTR = IF SUM([impressions]) > 0 THEN SUM([clicks])/SUM([impressions]) END
CPC = IF SUM([clicks]) > 0 THEN SUM([spend_usd])/SUM([clicks]) END
Attributed ROAS = IF SUM([spend_usd]) > 0 THEN SUM([net_revenue_usd])/SUM([spend_usd]) END
Click-to-member rate = IF SUM([clicks]) > 0 THEN SUM([new_members])/SUM([clicks]) END
```

Create sheets: channel CAC horizontal bars; continuous date CAC line colored by channel; geography × audience CAC heatmap; spend/members/CAC/ROAS KPI tiles. Add date, channel, platform, geography, and audience filters; apply to all sheets using this source. Use ratio-of-sums calculations after filters. Add attribution and USD notes. Reconcile channel rows to `outputs/channel_performance.csv`.

## Validation before publishing

Check each dashboard's full-data totals, one filtered slice, zero-denominator behavior, field types, tooltips, and synthetic-data disclosure. Export a screenshot, retain the `.twb`/`.twbx`, and add a real Tableau Public URL only after publishing. Never place real customer IDs in a public workbook.
