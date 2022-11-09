#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_timeseries.py
@Time    :   2022/10/24 19:59:45
@Author  :   Next Finance Tech
@License :   (C)Copyright 2022 Next Finance Tech
"""

import os
import time
import unittest

import dotenv

from pymessari.timeseries import TimeseriesAPI


class TestTimeseriesAPI(unittest.TestCase):
    def setUp(self) -> None:
        dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
        dotenv.load_dotenv(dotenv_path=dotenv_path)
        api_key = os.environ.get("API_KEY")

        self.api = TimeseriesAPI(api_key=api_key)
        time.sleep(1)

    def test_list_asset_timeseries_metric_ids(self) -> None:
        response = self.api.list_asset_timeseries_metric_ids()

        self.assertEqual(response["status_code"], 200)

    def test_get_asset_timeseries(self) -> None:
        asset_key = "bitcoin"
        metrci_id = "price"
        response = self.api.get_asset_timeseries(asset_key=asset_key, metric_id=metrci_id)

        self.assertEqual(response["status_code"], 200)

    def test_get_market_timeseries(self) -> None:
        market_key = "binance-btc-usdt"
        metric_id = "price"
        response = self.api.get_market_timeseries(market_key=market_key, metric_id=metric_id)

        self.assertEqual(response["status_code"], 200)


if __name__ == "__main__":
    unittest.main()
