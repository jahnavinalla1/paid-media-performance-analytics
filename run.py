"""Campaign diagnostics. Run with Python 3.10+; no third-party dependencies."""
import random
import sys
from datetime import date, timedelta
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import database, export_query, query, report, table, write_csv

ROOT = Path(__file__).resolve().parent


def generate(seed=41):
    rng = random.Random(seed)
    rows = []
    specs = [('Search','Google Ads',.036,.075,1.8), ('Social','Meta Ads',.018,.038,1.1),
             ('Display','Display Network',.007,.019,.8), ('Affiliate','Partner Network',.025,.065,1.5)]
    for day in range(60):
        for channel, platform, ctr, cvr, cpc in specs:
            for geo in ['US','UK','CA']:
                for audience in ['Prospecting','Retargeting']:
                    impressions = rng.randint(3500,11000)
                    fatigue = .70 if channel == 'Social' and day >= 30 and audience == 'Prospecting' else 1
                    clicks = int(impressions * ctr * fatigue * rng.uniform(.85,1.15))
                    members = sum(rng.random() < cvr*(1.35 if audience=='Retargeting' else 1) for _ in range(clicks))
                    spend = round(clicks*cpc*rng.uniform(.9,1.2)/fatigue,2)
                    rows.append(dict(date=str(date(2026,8,1)+timedelta(days=day)),campaign_id=f'{channel}-{geo}-{audience}',
                                     channel=channel,platform=platform,geography=geo,audience=audience,
                                     impressions=impressions,clicks=clicks,spend_usd=spend,new_members=members,
                                     net_revenue_usd=round(members*144*.95,2)))
    return rows


def main():
    rows = generate()
    write_csv(ROOT/'data/campaign_daily.csv',rows)
    db = database(ROOT/'outputs/analysis.sqlite',{'campaign_daily':rows})
    channels=export_query(db,ROOT/'analysis.sql',ROOT/'outputs/channel_performance.csv')
    segments=export_query(db,ROOT/'segments.sql',ROOT/'outputs/segment_performance.csv')
    weekly=query(db,"SELECT strftime('%Y-%W',date) AS week, channel, SUM(spend_usd) AS spend_usd, SUM(new_members) AS new_members, ROUND(SUM(spend_usd)/NULLIF(SUM(new_members),0),2) AS cac_usd FROM campaign_daily GROUP BY 1,2")
    write_csv(ROOT/'outputs/weekly_performance.csv',weekly)
    spend=sum(r['spend_usd'] for r in rows); members=sum(r['new_members'] for r in rows)
    fatigue=[r for r in segments if r['channel']=='Social' and r['audience']=='Prospecting' and r['period']=='last_30_days']
    change=sum(r['cac_usd']/r['previous_period_cac_usd']-1 for r in fatigue)/len(fatigue)
    findings=[f"{channels[0]['channel']} has the lowest observed attributed CAC (${channels[0]['cac_usd']:.2f}); evaluate a small budget test after checking incrementality and audience overlap.",
              f"Social prospecting CAC increased by {change:.1%} on average across the three geography cuts between the two 30-day periods. Investigate creative fatigue and auction costs; this is a descriptive signal, not a causal diagnosis.",
              'Review the channel summary alongside audience cuts. Retargeting serves already interested users, so lower attributed CAC does not establish incremental growth.']
    report(ROOT,'Paid Media Performance & Acquisition',{'Media spend':f'${spend:,.0f}','New members':f'{members:,}','Blended media CAC':f'${spend/members:.2f}','Campaign-day rows':len(rows)},
           [table('Channel performance',channels,'channel','cac_usd'),table('Audience and geography',segments,'channel','cac_usd'),table('Weekly trend',weekly,'week','cac_usd')],findings,
           'Synthetic 60-day simulation. Members use an exclusive last-click attribution assignment; platforms are labels, not live integrations. Revenue is assumed first-term net receipts (144 USD less 5% refunds), not lifetime value or profit. All spend is pre-normalized to USD; media CAC excludes salaries and agency fees. Full conversion windows are assumed mature. The fatigue pattern is deliberately seeded.')
    db.close()


if __name__=='__main__': main()
