#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_market.py
@Time    :   2022/10/24 19:58:55
@Author  :   Next Finance Tech
@License :   (C)Copyright 2022 Next Finance Tech
"""

import os
import time
import unittest

import dotenv

from pymessari.market import MarketAPI


class TestMarketAPI(unittest.TestCase):
    def setUp(self) -> None:
        dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
        dotenv.load_dotenv(dotenv_path=dotenv_path)
        api_key = os.environ.get("API_KEY")

        self.api = MarketAPI(api_key=api_key)
        time.sleep(1)

    def test_get_all_markets(self) -> None:
        response = self.api.get_all_markets()

        self.assertEqual(response["status_code"], 200)

    def test_get_market_timeseries(self) -> None:
        market_key = "binance-btc-usdt"
        metric_id = "price"
        response = self.api.get_market_timeseries(market_key=market_key, metric_id=metric_id)

        self.assertEqual(response["status_code"], 200)


if __name__ == "__main__":
    unittest.main()
