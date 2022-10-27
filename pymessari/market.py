#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   market.py
@Time    :   2022/10/24 20:00:12
@Author  :   Next Finance Tech
@License :   (C)Copyright 2022 Next Finance Tech
"""

import requests

from .base import BaseAPI


class MarketAPI(BaseAPI):
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

    def get_all_markets(self, **params):
        endpoint = "/api/v1/markets"

        return self.request(endpoint, params=params)

    def get_market_timeseries(self, market_key, metric_id, **params):
        endpoint = f"/api/v1/markets/{market_key}/metrics/{metric_id}/time-series"

        return self.request(endpoint, params=params)
