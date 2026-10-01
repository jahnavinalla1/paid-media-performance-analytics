import math
import sqlite3
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import run
lift=budget=reporting=run

class PipelineTests(unittest.TestCase):
    def connect(self,project):
        source=sqlite3.connect(ROOT/'outputs/analysis.sqlite')
        db=sqlite3.connect(':memory:');source.backup(db);source.close()
        db.row_factory=sqlite3.Row
        self.addCleanup(db.close)
        return db

    def test_weighted_cac_and_reconciliation(self):
        db=self.connect('01-paid-media-performance')
        rows=db.execute((ROOT/'analysis.sql').read_text()).fetchall()
        total=db.execute('SELECT SUM(spend_usd),SUM(new_members) FROM campaign_daily').fetchone()
        self.assertAlmostEqual(sum(r['spend_usd'] for r in rows),total[0],places=6)
        self.assertEqual(sum(r['new_members'] for r in rows),total[1])
        for r in rows:self.assertAlmostEqual(r['cac_usd'],r['spend_usd']/r['new_members'],delta=.0051)

    def test_zero_conversions_is_null(self):
        db=self.connect('01-paid-media-performance')
        db.execute("UPDATE campaign_daily SET new_members=0 WHERE channel='Display'")
        result=db.execute((ROOT/'analysis.sql').read_text()).fetchall()
        self.assertIsNone(next(r for r in result if r['channel']=='Display')['cac_usd'])

if __name__=='__main__':unittest.main()
