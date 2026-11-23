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
