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
        except requests.RequestException as e:
            raise e

        return BaseAPI.process_response(response)

    @staticmethod
    def process_response(response):
        result = {"status_code": response.status_code}
        if len(response.content) > 0:
            result["body"] = response.json()

        return result
