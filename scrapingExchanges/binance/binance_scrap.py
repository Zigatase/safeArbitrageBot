import requests
from scrapingExchanges.binance.binanceConfig import url, headers, paramsAllPay, paramsTinkoffNew, paramsRosBankNew


# --- All Pay ---
def binance_all():
    response = requests.post(url=url, headers=headers, json=paramsAllPay).json()

    for i in response['data']:
        print(f"Class: {i['adv']['classify']}")
        print(f"Token: {i['adv']['asset']}")
        print(f"Fiat: {i['adv']['fiatUnit']}")
        print(f"Price: {i['adv']['price']} {i['adv']['fiatUnit']}")
        print(f"Available: {i['adv']['dynamicMaxSingleTransQuantity']} {i['adv']['asset']}")
        print(f"Min Limit: {i['adv']['minSingleTransAmount']} {i['adv']['fiatUnit']}")
        print(f"Max Limit: {i['adv']['dynamicMaxSingleTransAmount']} {i['adv']['fiatUnit']}")
        print(f"Order: {float(i['advertiser']['monthFinishRate']) * 100} % \n\n")

# --- Tinkoff ---
def binance_tf():
    response = requests.post(url=url, headers=headers, json=paramsTinkoffNew).json()

    for i in response['data']:
        print(f"Class: {i['adv']['classify']}")
        print(f"Token: {i['adv']['asset']}")
        print(f"Fiat: {i['adv']['fiatUnit']}")
        print(f"Price: {i['adv']['price']} {i['adv']['fiatUnit']}")
        print(f"Available: {i['adv']['dynamicMaxSingleTransQuantity']} {i['adv']['asset']}")
        print(f"Min Limit: {i['adv']['minSingleTransAmount']} {i['adv']['fiatUnit']}")
        print(f"Max Limit: {i['adv']['dynamicMaxSingleTransAmount']} {i['adv']['fiatUnit']}")
        print(f"Order: {float(i['advertiser']['monthFinishRate']) * 100} % \n\n")


# --- RosBank (SberBank)
def binance_ros():
    response = requests.post(url=url, headers=headers, json=paramsRosBankNew).json()

    for i in response['data']:
        print(f"Class: {i['adv']['classify']}")
        print(f"Token: {i['adv']['asset']}")
        print(f"Fiat: {i['adv']['fiatUnit']}")
        print(f"Price: {i['adv']['price']} {i['adv']['fiatUnit']}")
        print(f"Available: {i['adv']['dynamicMaxSingleTransQuantity']} {i['adv']['asset']}")
        print(f"Min Limit: {i['adv']['minSingleTransAmount']} {i['adv']['fiatUnit']}")
        print(f"Max Limit: {i['adv']['dynamicMaxSingleTransAmount']} {i['adv']['fiatUnit']}")
        print(f"Order: {float(i['advertiser']['monthFinishRate']) * 100} % \n\n")


def main():
    binance_all()


if __name__ == '__main__':
    main()