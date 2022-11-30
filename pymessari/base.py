#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   base.py
@Time    :   2022/10/24 20:00:04
@Author  :   Next Finance Tech
@License :   (C)Copyright 2022 Next Finance Tech
"""
import requests


class BaseAPI:
    def __init__(self, api_key, timeout=None):
        self.api_url = "https://data.messari.io"
        self.api_key = api_key
        self.timeout = timeout

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
                response.raise_for_status()
        except requests.RequestException as e:
            # TODO: handle exception
            raise e

        return response.json()
