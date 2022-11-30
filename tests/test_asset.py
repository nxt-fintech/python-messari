#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_asset.py
@Time    :   2022/10/24 19:58:37
@Author  :   Next Finance Tech
@License :   (C)Copyright 2022 Next Finance Tech
"""

import os
import time
import unittest

import dotenv

from pymessari.asset import AssetAPI


class TestAssetAPI(unittest.TestCase):
    def setUp(self) -> None:
        dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
        dotenv.load_dotenv(dotenv_path=dotenv_path)
        api_key = os.environ.get("API_KEY")

        self.api = AssetAPI(api_key=api_key)
        time.sleep(1)

    def test_get_all_assets(self) -> None:
        response = self.api.get_all_assets()

        self.assertIsInstance(response, dict)

    def test_get_asset(self) -> None:
        assert_key = "btc"
        response = self.api.get_asset(asset_key=assert_key)

        self.assertIsInstance(response, dict)

    def test_get_asset_profile(self) -> None:
        assert_key = "btc"
        response = self.api.get_asset_profile(asset_key=assert_key)

        self.assertIsInstance(response, dict)

    def test_get_asset_metrics(self) -> None:
        assert_key = "btc"
        response = self.api.get_asset_metrics(asset_key=assert_key)

        self.assertIsInstance(response, dict)

    def test_get_asset_market_data(self) -> None:
        assert_key = "btc"
        response = self.api.get_asset_market_data(asset_key=assert_key)

        self.assertIsInstance(response, dict)

    def test_list_asset_timeseries_metric_ids(self) -> None:
        response = self.api.list_asset_timeseries_metric_ids()

        self.assertIsInstance(response, dict)

    def test_get_asset_timeseries(self) -> None:
        assert_key = "btc"
        metric_id = "price"
        params = {
            "start": "2022-10-16T23:59:59.999Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_asset_timeseries(
            asset_key=assert_key, metric_id=metric_id, **params
        )

        self.assertIsInstance(response, dict)


if __name__ == "__main__":
    unittest.main()
