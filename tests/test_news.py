#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_news.py
@Time    :   2022/10/24 19:59:16
@Author  :   Next Finance Tech
@License :   (C)Copyright 2022 Next Finance Tech
"""

import os
import unittest

import dotenv

from pymessari.news import NewsAPI


class TestNewsAPI(unittest.TestCase):
    def setUp(self) -> None:
        dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
        dotenv.load_dotenv(dotenv_path=dotenv_path)
        api_key = os.environ.get("API_KEY")

        self.api = NewsAPI(api_key=api_key)

    def test_get_all_news(self) -> None:
        response = self.api.get_all_news()

        self.assertEqual(response["status_code"], 200)

    def test_get_news_for_asset(self) -> None:
        asset_key = "btc"
        response = self.api.get_news_for_asset(asset_key=asset_key)

        self.assertEqual(response["status_code"], 200)


if __name__ == "__main__":
    unittest.main()
