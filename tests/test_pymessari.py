#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_pymessari.py
@Time    :   2022/10/19 19:37:10
@Author  :   Next Finance Tech
@Version :   0.0.1
@License :   (C)Copyright 2022 Next Finance Tech
"""


import os
import unittest

import dotenv
from pymessari.pymessari import API


class TestAPI(unittest.TestCase):
    def setUp(self) -> None:
        dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
        dotenv.load_dotenv(dotenv_path=dotenv_path)
        api_key = os.environ.get("API_KEY")

        self.api = API(api_key=api_key)

    def test_get_total_revenue(self):
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2017-10-19T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_total_revenue(protocol_id=protocol_id, **params)

        self.assertEqual(response["status_code"], 200)

    def test_get_protocol_side_revenue(self):
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2017-10-19T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_protocol_side_revenue(protocol_id=protocol_id, **params)

        self.assertEqual(response["status_code"], 200)

    def test_get_supply_side_revenue(self):
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2017-10-19T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_supply_side_revenue(protocol_id=protocol_id, **params)

        self.assertEqual(response["status_code"], 200)

    def test_get_total_deposits_balance(self):
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2017-10-19T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_total_deposits_balance(protocol_id=protocol_id, **params)

        self.assertEqual(response["status_code"], 200)

    def test_get_num_deposits(self):
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2017-10-19T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_num_deposits(protocol_id=protocol_id, **params)

        self.assertEqual(response["status_code"], 200)

    def test_get_deposits(self):
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2017-10-19T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_deposits(protocol_id=protocol_id, **params)

        self.assertEqual(response["status_code"], 200)

    def test_get_total_borrows_balance(self):
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2017-10-19T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_total_borrows_balance(protocol_id=protocol_id, **params)

        self.assertEqual(response["status_code"], 200)

    def test_get_num_borrow(self):
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2017-10-19T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_num_borrow(protocol_id=protocol_id, **params)

        self.assertEqual(response["status_code"], 200)

    def test_get_borrows(self):
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2017-10-19T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_borrows(protocol_id=protocol_id, **params)

        self.assertEqual(response["status_code"], 200)

    def test_get_num_liquidates(self):
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2017-10-19T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_num_liquidates(protocol_id=protocol_id, **params)

        self.assertEqual(response["status_code"], 200)

    def test_get_liquidates(self):
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2017-10-19T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_liquidates(protocol_id=protocol_id, **params)

        self.assertEqual(response["status_code"], 200)

    def test_get_withdraws(self):
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2017-10-19T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_withdraws(protocol_id=protocol_id, **params)

        self.assertEqual(response["status_code"], 200)

    def test_get_num_withdraws(self):
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2017-10-19T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_num_withdraws(protocol_id=protocol_id, **params)

        self.assertEqual(response["status_code"], 200)

    def test_get_total_value_locked(self):
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2017-10-19T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_total_value_locked(protocol_id=protocol_id, **params)

        self.assertEqual(response["status_code"], 200)


if __name__ == "__main__":
    unittest.main()
