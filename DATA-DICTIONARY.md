# Data contracts and metric definitions

All records are synthetic. Seeds 41, 52, 63, and 74 regenerate the four respective datasets. No personal data, WHOOP data, scraped ad accounts, or API credentials are used.

## Project 01 — paid media

`campaign_daily.csv`: one row per date × campaign (channel/geography/audience); campaign ID is unique within date. Dates span August 1–September 29, 2026 inclusive. Four channels × three countries × two audiences × sixty days = 1,440 rows. Platform is functionally dependent on channel in this small demonstration; independent multi-platform comparisons within a channel are not possible.

| Field | Type / meaning |
|---|---|
| date | ISO date, UTC reporting day |
| campaign_id | Synthetic stable string |
| channel / platform | Search / Google Ads, Social / Meta Ads, Display / Display Network, Affiliate / Partner Network |
| geography | US, UK, CA; labels only; all money is normalized USD |
| audience | Prospecting or Retargeting |
| impressions / clicks | Integer delivered impressions / clicks |
| spend_usd | Nonnegative media spend, USD |
| new_members | Exclusive attributed acquisitions; one assigned campaign per acquisition |
| net_revenue_usd | First-term modeled receipts: members × 144 USD × 0.95 |

CTR = sum(clicks)/sum(impressions). CPC = sum(spend)/sum(clicks). Click-to-member rate = sum(members)/sum(clicks). Media CAC = sum(spend)/sum(members). Attributed ROAS = sum(net revenue)/sum(spend). Ratios use aggregate numerators and denominators; never average row CAC or ROAS. Undefined ratios are null, not zero. These are mature, last-click-equivalent simulation aggregates, not evidence of incremental returns. Revenue is not LTV, margin, or recognized subscription revenue.
