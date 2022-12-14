#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_protocol.py
@Time    :   2022/10/19 19:37:10
@Author  :   Next Finance Tech
@License :   (C)Copyright 2022 Next Finance Tech
"""


import os
import time
import unittest

import dotenv

from pymessari.pymessari import ProtocolAPI


class TestProtocolAPI(unittest.TestCase):
    def setUp(self) -> None:
        dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
        dotenv.load_dotenv(dotenv_path=dotenv_path)
        api_key = os.environ.get("API_KEY")

        self.api = ProtocolAPI(api_key=api_key)
        time.sleep(1)

    def test_get_total_revenue(self) -> None:
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_total_revenue(protocol_id=protocol_id, **params)

        self.assertIsInstance(response, dict)

    def test_get_total_revenue_with_network_id(self) -> None:
        protocol_id = "c0af3604-6141-4577-87c9-0b13e8fdaf4a"
        network_id = "383aabb9-285c-4813-aa76-6987091b93a6"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_total_revenue(
            protocol_id=protocol_id, network_id=network_id, **params
        )

        self.assertIsInstance(response, dict)

    def test_get_protocol_side_revenue(self) -> None:
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_protocol_side_revenue(protocol_id=protocol_id, **params)

        self.assertIsInstance(response, dict)

    def test_get_protocol_side_revenue_with_network_id(self) -> None:
        protocol_id = "c0af3604-6141-4577-87c9-0b13e8fdaf4a"
        network_id = "383aabb9-285c-4813-aa76-6987091b93a6"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_protocol_side_revenue(
            protocol_id=protocol_id, network_id=network_id, **params
        )

        self.assertIsInstance(response, dict)

    def test_get_supply_side_revenue(self) -> None:
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_supply_side_revenue(protocol_id=protocol_id, **params)

        self.assertIsInstance(response, dict)

    def test_get_supply_side_revenue_with_network_id(self) -> None:
        protocol_id = "c0af3604-6141-4577-87c9-0b13e8fdaf4a"
        network_id = "383aabb9-285c-4813-aa76-6987091b93a6"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_supply_side_revenue(
            protocol_id=protocol_id, network_id=network_id, **params
        )

        self.assertIsInstance(response, dict)

    def test_get_total_deposits_balance(self) -> None:
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_total_deposits_balance(protocol_id=protocol_id, **params)

        self.assertIsInstance(response, dict)

    def test_get_total_deposits_balance_with_network_id(self) -> None:
        protocol_id = "c0af3604-6141-4577-87c9-0b13e8fdaf4a"
        network_id = "383aabb9-285c-4813-aa76-6987091b93a6"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_total_deposits_balance(
            protocol_id=protocol_id, network_id=network_id, **params
        )

        self.assertIsInstance(response, dict)

    def test_get_num_deposits(self) -> None:
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_num_deposits(protocol_id=protocol_id, **params)

        self.assertIsInstance(response, dict)

    def test_get_num_deposits_with_network_id(self) -> None:
        protocol_id = "c0af3604-6141-4577-87c9-0b13e8fdaf4a"
        network_id = "383aabb9-285c-4813-aa76-6987091b93a6"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_num_deposits(
            protocol_id=protocol_id, network_id=network_id, **params
        )

        self.assertIsInstance(response, dict)

    def test_get_deposits(self) -> None:
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_deposits(protocol_id=protocol_id, **params)

        self.assertIsInstance(response, dict)

    def test_get_deposits_with_network_id(self) -> None:
        protocol_id = "c0af3604-6141-4577-87c9-0b13e8fdaf4a"
        network_id = "383aabb9-285c-4813-aa76-6987091b93a6"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_deposits(protocol_id=protocol_id, network_id=network_id, **params)

        self.assertIsInstance(response, dict)

    def test_get_total_borrows_balance(self) -> None:
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_total_borrows_balance(protocol_id=protocol_id, **params)

        self.assertIsInstance(response, dict)

    def test_get_total_borrows_balance_with_network_id(self) -> None:
        protocol_id = "c0af3604-6141-4577-87c9-0b13e8fdaf4a"
        network_id = "383aabb9-285c-4813-aa76-6987091b93a6"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_total_borrows_balance(
            protocol_id=protocol_id, network_id=network_id, **params
        )

        self.assertIsInstance(response, dict)

    def test_s(self) -> None:
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_num_borrows(protocol_id=protocol_id, **params)

        self.assertIsInstance(response, dict)

    def test_get_num_borrows_with_network_id(self) -> None:
        protocol_id = "c0af3604-6141-4577-87c9-0b13e8fdaf4a"
        network_id = "383aabb9-285c-4813-aa76-6987091b93a6"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_num_borrows(
            protocol_id=protocol_id, network_id=network_id, **params
        )

        self.assertIsInstance(response, dict)

    def test_get_borrows(self) -> None:
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_borrows(protocol_id=protocol_id, **params)

        self.assertIsInstance(response, dict)

    def test_get_borrows_with_network_id(self) -> None:
        protocol_id = "c0af3604-6141-4577-87c9-0b13e8fdaf4a"
        network_id = "383aabb9-285c-4813-aa76-6987091b93a6"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_borrows(protocol_id=protocol_id, network_id=network_id, **params)

        self.assertIsInstance(response, dict)

    def test_get_num_liquidates(self) -> None:
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_num_liquidates(protocol_id=protocol_id, **params)

        self.assertIsInstance(response, dict)

    def test_get_num_liquidates_with_network_id(self) -> None:
        protocol_id = "c0af3604-6141-4577-87c9-0b13e8fdaf4a"
        network_id = "383aabb9-285c-4813-aa76-6987091b93a6"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_num_liquidates(
            protocol_id=protocol_id, network_id=network_id, **params
        )

        self.assertIsInstance(response, dict)

    def test_get_liquidates(self) -> None:
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_liquidates(protocol_id=protocol_id, **params)

        self.assertIsInstance(response, dict)

    def test_get_liquidates_with_network_id(self) -> None:
        protocol_id = "c0af3604-6141-4577-87c9-0b13e8fdaf4a"
        network_id = "383aabb9-285c-4813-aa76-6987091b93a6"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_liquidates(protocol_id=protocol_id, network_id=network_id, **params)

        self.assertIsInstance(response, dict)

    def test_get_withdraws(self) -> None:
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_withdraws(protocol_id=protocol_id, **params)

        self.assertIsInstance(response, dict)

    def test_get_withdraws_with_network_id(self) -> None:
        protocol_id = "c0af3604-6141-4577-87c9-0b13e8fdaf4a"
        network_id = "383aabb9-285c-4813-aa76-6987091b93a6"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_withdraws(protocol_id=protocol_id, network_id=network_id, **params)

        self.assertIsInstance(response, dict)

    def test_get_num_withdraws(self) -> None:
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_num_withdraws(protocol_id=protocol_id, **params)

        self.assertIsInstance(response, dict)

    def test_get_num_withdraws_with_network_id(self) -> None:
        protocol_id = "c0af3604-6141-4577-87c9-0b13e8fdaf4a"
        network_id = "383aabb9-285c-4813-aa76-6987091b93a6"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_num_withdraws(
            protocol_id=protocol_id, network_id=network_id, **params
        )

        self.assertIsInstance(response, dict)

    def test_get_total_value_locked(self) -> None:
        protocol_id = "accec09e-1e9f-4b54-849e-fa7c91a10f89"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_total_value_locked(protocol_id=protocol_id, **params)

        self.assertIsInstance(response, dict)

    def test_get_total_value_locked_with_network_id(self) -> None:
        protocol_id = "c0af3604-6141-4577-87c9-0b13e8fdaf4a"
        network_id = "383aabb9-285c-4813-aa76-6987091b93a6"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_total_value_locked(
            protocol_id=protocol_id, network_id=network_id, **params
        )

        self.assertIsInstance(response, dict)

    def test_get_volume(self) -> None:
        protocol_id = "c0af3604-6141-4577-87c9-0b13e8fdaf4a"
        network_id = "383aabb9-285c-4813-aa76-6987091b93a6"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_volume(protocol_id=protocol_id, network_id=network_id, **params)

        self.assertIsInstance(response, dict)

    def test_get_num_swaps(self) -> None:
        protocol_id = "c0af3604-6141-4577-87c9-0b13e8fdaf4a"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_num_swaps(protocol_id=protocol_id, **params)

        self.assertIsInstance(response, dict)

    def test_get_num_swaps_with_network_id(self) -> None:
        protocol_id = "c0af3604-6141-4577-87c9-0b13e8fdaf4a"
        network_id = "383aabb9-285c-4813-aa76-6987091b93a6"
        params = {
            "beg": "2022-10-16T00:00:00.000Z",
            "end": "2022-10-17T23:59:59.999Z",
            "interval": "1d",
        }
        response = self.api.get_num_swaps(protocol_id=protocol_id, network_id=network_id, **params)

        self.assertIsInstance(response, dict)


if __name__ == "__main__":
    unittest.main()
