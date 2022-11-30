#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   pymessari.py
@Time    :   2022/10/19 14:50:19
@Author  :   Next Finance Tech
@License :   (C)Copyright 2022 Next Finance Tech
"""
from .asset import AssetAPI
from .market import MarketAPI
from .news import NewsAPI
from .protocol import ProtocolAPI
from .timeseries import TimeseriesAPI


class MessariAPI:
    def __init__(self, api_key, timeout=None):
        self.api_key = api_key
        self.timeout = timeout

    def asset(self):
        return self.singleton("_asset", AssetAPI)

    def market(self):
        return self.singleton("_matket", MarketAPI)

    def news(self):
        return self.singleton("_news", NewsAPI)

    def protocol(self):
        return self.singleton("_protocol", ProtocolAPI)

    def timeseries(self):
        return self.singleton("_timeseries", TimeseriesAPI)

    def singleton(self, attribute_name, cls):
        if hasattr(self, attribute_name):
            instance = getattr(self, attribute_name)
            return instance

        instance = cls(self.api_key, self.timeout)
        setattr(self, attribute_name, instance)
        return instance
