#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   protocol.py
@Time    :   2022/10/24 20:00:29
@Author  :   Next Finance Tech
@License :   (C)Copyright 2022 Next Finance Tech
"""
from .base import BaseAPI


class ProtocolAPI(BaseAPI):
    @staticmethod
    def join_id(protocol_id, network_id):
        if network_id:
            protocol_id = f"{protocol_id}/networks/{network_id}"

        return protocol_id

    # revenue
    def get_total_revenue(self, protocol_id, network_id=None, **params):
        joined_ids = ProtocolAPI.join_id(protocol_id, network_id)
        endpoint = f"/api/v1/protocols/{joined_ids}/metrics/total-revenue-usd/time-series"

        return self.request(endpoint, params=params)

    def get_protocol_side_revenue(self, protocol_id, network_id=None, **params):
        joined_ids = ProtocolAPI.join_id(protocol_id, network_id)
        endpoint = f"/api/v1/protocols/{joined_ids}/metrics/protocol-side-revenue-usd/time-series"

        return self.request(endpoint, params=params)

    def get_supply_side_revenue(self, protocol_id, network_id=None, **params):
        joined_ids = ProtocolAPI.join_id(protocol_id, network_id)
        endpoint = f"/api/v1/protocols/{joined_ids}/metrics/supply-side-revenue-usd/time-series"

        return self.request(endpoint, params=params)

    # deposits
    def get_total_deposits_balance(self, protocol_id, network_id=None, **params):
        joined_ids = ProtocolAPI.join_id(protocol_id, network_id)
        endpoint = f"/api/v1/protocols/{joined_ids}/metrics/total-deposits-balance-usd/time-series"

        return self.request(endpoint, params=params)

    def get_num_deposits(self, protocol_id, network_id=None, **params):
        joined_ids = ProtocolAPI.join_id(protocol_id, network_id)
        endpoint = f"/api/v1/protocols/{joined_ids}/metrics/num-deposits/time-series"

        return self.request(endpoint, params=params)

    def get_deposits(self, protocol_id, network_id=None, **params):
        joined_ids = ProtocolAPI.join_id(protocol_id, network_id)
        endpoint = f"/api/v1/protocols/{joined_ids}/metrics/deposits-usd/time-series"

        return self.request(endpoint, params=params)

    # borrows
    def get_total_borrows_balance(self, protocol_id, network_id=None, **params):
        joined_ids = ProtocolAPI.join_id(protocol_id, network_id)
        endpoint = f"/api/v1/protocols/{joined_ids}/metrics/total-borrows-balance-usd/time-series"

        return self.request(endpoint, params=params)

    def get_num_borrows(self, protocol_id, network_id=None, **params):
        joined_ids = ProtocolAPI.join_id(protocol_id, network_id)
        endpoint = f"/api/v1/protocols/{joined_ids}/metrics/num-borrows/time-series"

        return self.request(endpoint, params=params)

    def get_borrows(self, protocol_id, network_id=None, **params):
        joined_ids = ProtocolAPI.join_id(protocol_id, network_id)
        endpoint = f"/api/v1/protocols/{joined_ids}/metrics/borrows-usd/time-series"

        return self.request(endpoint, params=params)

    # liquidates
    def get_num_liquidates(self, protocol_id, network_id=None, **params):
        joined_ids = ProtocolAPI.join_id(protocol_id, network_id)
        endpoint = f"/api/v1/protocols/{joined_ids}/metrics/num-liquidates/time-series"

        return self.request(endpoint, params=params)

    def get_liquidates(self, protocol_id, network_id=None, **params):
        joined_ids = ProtocolAPI.join_id(protocol_id, network_id)
        endpoint = f"/api/v1/protocols/{joined_ids}/metrics/liquidates-usd/time-series"

        return self.request(endpoint, params=params)

    # withdraws
    def get_withdraws(self, protocol_id, network_id=None, **params):
        joined_ids = ProtocolAPI.join_id(protocol_id, network_id)
        endpoint = f"/api/v1/protocols/{joined_ids}/metrics/withdraws-usd/time-series"

        return self.request(endpoint, params=params)

    def get_num_withdraws(self, protocol_id, network_id=None, **params):
        joined_ids = ProtocolAPI.join_id(protocol_id, network_id)
        endpoint = f"/api/v1/protocols/{joined_ids}/metrics/num-withdraws/time-series"

        return self.request(endpoint, params=params)

    # locked
    def get_total_value_locked(self, protocol_id, network_id=None, **params):
        joined_ids = ProtocolAPI.join_id(protocol_id, network_id)
        endpoint = f"/api/v1/protocols/{joined_ids}/metrics/total-value-locked-usd/time-series"

        return self.request(endpoint, params=params)

    # volume
    def get_volume(self, protocol_id, network_id=None, **params):
        joined_ids = ProtocolAPI.join_id(protocol_id, network_id)
        endpoint = f"/api/v1/protocols/{joined_ids}/metrics/volume-usd/time-series"

        return self.request(endpoint, params=params)

    # swap
    def get_num_swaps(self, protocol_id, network_id=None, **params):
        joined_ids = ProtocolAPI.join_id(protocol_id, network_id)
        endpoint = f"/api/v1/protocols/{joined_ids}/metrics/num-swaps/time-series"

        return self.request(endpoint, params=params)
