[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Build Status](https://github.com/pre-commit/action/workflows/deploy/badge.svg)](https://github.com/pre-commit/action/actions)

# pymessari

python api client for [messari](https://messari.io/).

[Official API Document](https://messari.io/api/docs).

## Install

```bash
pip install pymessari
```

## Quick start

```python
from pymessari import API
api = MessariAPI(api_key=<API_KEY>)

asset_client = api.asset()
market_client = api.market()
news_client = api.news()
protocol_client = api.protocol()
timeseries_client = api.timeseries()
```
