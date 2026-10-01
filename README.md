# Paid Media Performance & Acquisition

Independent, AI-assisted marketing analytics project using **synthetic data** for a fictional fitness subscription business. Findings are simulated and do not represent real campaign results.

![Results preview](outputs/preview.svg)

## Business question

Diagnose channel efficiency and audience-level changes across search, social, display and affiliate campaigns.

## Review the result

- [Decision brief](outputs/decision-brief.md): computed findings and business recommendations.
- [Interactive dashboard source](outputs/dashboard.html): download and open locally for charts, view selection, row search, metric selection, and CSV export. GitHub shows HTML source rather than running it.
- [SQL analysis](analysis.sql) and [Python pipeline](run.py).
- [Looker source and setup](bi/README.md), plus [Tableau build guide](bi/TABLEAU.md).

## Run locally

Requires Python 3.10+; **no packages, API keys or paid accounts are needed**.

```bash
git clone https://github.com/jahnavinalla1/paid-media-performance-analytics.git
cd paid-media-performance-analytics
python3 run.py
python3 -m unittest discover -s tests -v
```

Open `outputs/dashboard.html` in your browser. Generated data CSVs and the SQLite database are excluded from Git and rebuilt with a fixed seed. Committed output CSVs can be inspected immediately.

## Computed findings — simulated data

- Affiliate has the lowest observed attributed CAC ($20.41); evaluate a small budget test after checking incrementality and audience overlap.
- Social prospecting CAC increased by 54.7% on average across the three geography cuts between the two 30-day periods. Investigate creative fatigue and auction costs; this is a descriptive signal, not a causal diagnosis.
- Review the channel summary alongside audience cuts. Retargeting serves already interested users, so lower attributed CAC does not establish incremental growth.

## Deliverables and status

| Deliverable | Status |
|---|---|
| Reproducible SQL/Python analysis | Executable and locally tested |
| Offline interactive dashboard | Generated with embedded computed data |
| Data-quality / numerical tests | See [validation record](VALIDATION.md) |
| Native LookML model, view, dashboard source | Supplied; needs warehouse connection and tenant validation |
| Tableau calculated fields and layout instructions | Supplied; workbook not built or published |
| Business recommendations | Hypothetical; no media spend executed |

The HTML report is the working dashboard. The repository does **not** claim a deployed Looker or Tableau dashboard. LookML is for Looker, not Looker Studio.

## Methods and tools

SQL, marketing measurement, visualization, analytical problem solving, explicit assumptions, business recommendations, and quality-checked AI assistance.

Read [data contracts](DATA-DICTIONARY.md), [AI assistance](AI-ASSISTANCE.md), and [review questions](REVIEW-GUIDE.md).

## Related independent repositories

- [Paid Social Incrementality & Lift](https://github.com/jahnavinalla1/marketing-incrementality-lift)
- [Marketing Investment & Budget Allocation](https://github.com/jahnavinalla1/marketing-budget-optimization)
- [Trusted Marketing Data & Reporting](https://github.com/jahnavinalla1/marketing-data-quality-reporting)
