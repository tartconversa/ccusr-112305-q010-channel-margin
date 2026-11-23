"""校验可供分析的资料关系。"""

import unittest

from scripts.inspect_sources import read_table


class SourceContractTest(unittest.TestCase):
    def test_source_observations_and_references(self):
        plans = {row["plan"] for row in read_table("plans")}
        sales = {row["sale"]:row for row in read_table("sales")}
        self.assertTrue(all(row["plan"] is None or row["plan"] in plans for row in sales.values()))
        self.assertGreaterEqual(len({row["week"] for row in sales.values()}), 12)
        self.assertTrue(any(row["plan"] is None for row in sales.values()))
        self.assertTrue(all(row["sale"] in sales for row in read_table("adjustments")))
        self.assertTrue(any(row["recognized_week"] > sales[row["sale"]]["week"] and
                            row["category"] == "跨渠道换货" for row in read_table("adjustments")))
        agreement = next(row for row in read_table("agreements") if row["campaign"] == "XMAS")
        asks = [row for row in read_table("decisions") if row["campaign"] == "XMAS" and row["action"] == "退出"]
        self.assertTrue(set(agreement["sales_hold"]) <= set(sales))
        self.assertLess(len(agreement["optional_stop"]) - len(asks), agreement["min_active"])

    def test_channel_handover_inputs(self):
        sources = [read_table(name) for name in ['entitlements', 'assumption_changes', 'redemption_events', 'sales']]
        self.assertTrue(all(x["sale"] in {s["sale"] for s in sources[3]} for x in sources[0]))
        self.assertEqual({x["approved"] for x in sources[1]},{"接受","待接管","部分接受","拒绝"})
        matching=[x for x in sources[2] if x["serial"]=="SER-01"]
        self.assertEqual({x["site"] for x in matching},{"雪场","网店"})
        self.assertEqual({x["kind"] for x in matching},{"自提记账","重复扫描"})

