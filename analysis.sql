-- Grain: one row per channel. Weighted rates use ratios of sums.
WITH channel_totals AS (
 SELECT channel, SUM(spend_usd) AS spend_usd, SUM(impressions) AS impressions,
        SUM(clicks) AS clicks, SUM(new_members) AS new_members,
        SUM(net_revenue_usd) AS net_revenue_usd
 FROM campaign_daily GROUP BY channel
)
SELECT *, ROUND(1.0*clicks/NULLIF(impressions,0),5) AS ctr,
 ROUND(spend_usd/NULLIF(clicks,0),2) AS cpc_usd,
 ROUND(1.0*new_members/NULLIF(clicks,0),5) AS click_to_member_rate,
 ROUND(spend_usd/NULLIF(new_members,0),2) AS cac_usd,
 ROUND(net_revenue_usd/NULLIF(spend_usd,0),3) AS attributed_roas
FROM channel_totals ORDER BY cac_usd;
