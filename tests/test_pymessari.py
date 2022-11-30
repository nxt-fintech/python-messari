#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_pymessari.py
@Time    :   2022/10/24 19:59:30
@Author  :   Next Finance Tech
@License :   (C)Copyright 2022 Next Finance Tech
"""

import os
import unittest

import dotenv

from pymessari.asset import AssetAPI
from pymessari.market import MarketAPI
from pymessari.news import NewsAPI
from pymessari.protocol import ProtocolAPI
from pymessari.pymessari import MessariAPI
from pymessari.timeseries import TimeseriesAPI


class TestAPI(unittest.TestCase):
    def setUp(self) -> None:
        dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
        dotenv.load_dotenv(dotenv_path=dotenv_path)
        api_key = os.environ.get("API_KEY")

        self.api = MessariAPI(api_key=api_key)

    def test_asset(self) -> None:
        self.assertIsInstance(self.api.asset(), AssetAPI)

    def test_market(self) -> None:
        self.assertIsInstance(self.api.market(), MarketAPI)

    def test_news(self) -> None:
        self.assertIsInstance(self.api.news(), NewsAPI)

    def test_protocol(self) -> None:
        self.assertIsInstance(self.api.protocol(), ProtocolAPI)

    def test_timeseries(self) -> None:
        self.assertIsInstance(self.api.timeseries(), TimeseriesAPI)
