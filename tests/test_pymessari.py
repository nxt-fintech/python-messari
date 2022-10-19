import unittest

from pymessari.pymessari import API


class TestAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.api = API(api_key="13acb1e8-0490-4576-a2cc-f5e51498a72e")

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


if __name__ == "__main__":
    unittest.main()
