-- Geography/platform/audience cuts and comparable, non-overlapping 30-day periods.
WITH grouped AS (
 SELECT channel, geography, platform, audience,
 CASE WHEN date < '2026-08-31' THEN 'first_30_days' ELSE 'last_30_days' END AS period,
 SUM(spend_usd) AS spend_usd, SUM(new_members) AS new_members,
 SUM(clicks) AS clicks, SUM(impressions) AS impressions
 FROM campaign_daily GROUP BY 1,2,3,4,5
), rates AS (
 SELECT *, ROUND(spend_usd/NULLIF(new_members,0),2) AS cac_usd,
 ROUND(1.0*clicks/NULLIF(impressions,0),5) AS ctr FROM grouped
)
SELECT *, LAG(cac_usd) OVER (
 PARTITION BY channel, geography, platform, audience ORDER BY period
) AS previous_period_cac_usd FROM rates;
