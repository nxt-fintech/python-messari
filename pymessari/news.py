#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   news.py
@Time    :   2022/10/24 20:00:20
@Author  :   Next Finance Tech
@License :   (C)Copyright 2022 Next Finance Tech
"""
from .base import BaseAPI


class NewsAPI(BaseAPI):
    def get_all_news(self, **params):
        endpoint = "/api/v1/news"

        return self.request(endpoint, params=params)

    def get_news_for_asset(self, asset_key, **params):
        endpoint = f"/api/v1/news/{asset_key}"

        return self.request(endpoint, params=params)
