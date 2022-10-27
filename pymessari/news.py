#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   news.py
@Time    :   2022/10/24 20:00:20
@Author  :   Next Finance Tech
@License :   (C)Copyright 2022 Next Finance Tech
"""

import requests

from .base import BaseAPI


class NewsAPI(BaseAPI):
    def request(self, endpoint, params=None):
        url = self.api_url + endpoint
        headers = {
            "Accept": "application/json",
            "x-messari-api-key": self.api_key,
        }

        try:
            with requests.Session() as s:
                s.headers.update(headers)
                response = s.get(url, params=params, timeout=self.timeout)
        except requests.RequestException as e:
            raise e

        return BaseAPI.process_response(response)

    def get_all_news(self, **params):
        endpoint = "/api/v1/news"

        return self.request(endpoint, params=params)

    def get_news_for_asset(self, asset_key, **params):
        endpoint = f"/api/v1/news/{asset_key}"

        return self.request(endpoint, params=params)
