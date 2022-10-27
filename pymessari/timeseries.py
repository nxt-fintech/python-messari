#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   timeseries.py
@Time    :   2022/10/24 20:00:45
@Author  :   Next Finance Tech
@License :   (C)Copyright 2022 Next Finance Tech
"""

import requests

from .base import BaseAPI


class TimeseriesAPI(BaseAPI):
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

    def list_asset_timeseries_metric_ids(self, **params):
        endpoint = "/api/v1/assets/metrics"

        return self.request(endpoint, params=params)

    def get_asset_timeseries(self, asset_key, metric_id, **params):
        endpoint = f"/api/v1/assets/{asset_key}/metrics/{metric_id}/time-series"

        return self.request(endpoint, params=params)

    def get_market_timeseries(self, market_key, metric_id, **params):
        endpoint = f"/api/v1/markets/{market_key}/metrics/{metric_id}/time-series"

        return self.request(endpoint, params=params)
