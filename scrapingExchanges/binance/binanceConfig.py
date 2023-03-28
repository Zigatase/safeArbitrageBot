__all__ = ["url", "headers", "paramsAllPay", "paramsTinkoffNew", "paramsRosBankNew"]

url = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"

headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}


# --- All Payments ---
paramsAllPay = {
  "proMerchantAds": False,
  "page": 1,
  "rows": 20,
  "payTypes": [],
  "countries": [],
  "publisherType": None,
  "asset": "USDT",
  "fiat": "RUB",
  "tradeType": "BUY"
}

# --- Tinkoff ---
paramsTinkoffNew = {
  "proMerchantAds": False,
  "page": 1,
  "rows": 20,
  "payTypes": ["TinkoffNew"],
  "countries": [],
  "publisherType": None,
  "asset": "USDT",
  "fiat": "RUB",
  "tradeType": "BUY"
}

# RosBank (Sber)
paramsRosBankNew = {
  "proMerchantAds": False,
  "page": 1,
  "rows": 20,
  "payTypes": ["RosBankNew"],
  "countries": [],
  "publisherType": None,
  "asset": "USDT",
  "fiat": "RUB",
  "tradeType": "BUY"
}