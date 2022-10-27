#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   asset.py
@Time    :   2022/10/24 19:59:56
@Author  :   Next Finance Tech
@License :   (C)Copyright 2022 Next Finance Tech
"""

import requests

from .base import BaseAPI


class AssetAPI(BaseAPI):
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

    def get_all_assets(self, **params):
        # TODO: with-metrics and with-profiles parameters
        endpoint = "/api/v2/assets"

        return self.request(endpoint, params=params)

    def get_asset(self, asset_key, **params):
        endpoint = f"/api/v1/assets/{asset_key}"

        return self.request(endpoint, params=params)

    def get_asset_profile(self, asset_key, **params):
        endpoint = f"/api/v2/assets/{asset_key}/profile"

        return self.request(endpoint, params=params)

    def get_asset_metrics(self, asset_key, **params):
        endpoint = f"/api/v1/assets/{asset_key}/metrics"

        return self.request(endpoint, params=params)

    def get_asset_market_data(self, asset_key, **params):
        endpoint = f"/api/v1/assets/{asset_key}/metrics/market-data"

        return self.request(endpoint, params=params)

    def list_asset_timeseries_metric_ids(self, **params):
        endpoint = "/api/v1/assets/metrics"

        return self.request(endpoint, params=params)

    def get_asset_timeseries(self, asset_key, metric_id, **params):
        endpoint = f"/api/v1/assets/{asset_key}/metrics/{metric_id}/time-series"

        return self.request(endpoint, params=params)
