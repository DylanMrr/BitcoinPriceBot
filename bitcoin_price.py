import requests

bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'


def get_price():
    response = requests.get(bitcoin_api_url).json()
    return (response[0]['price_usd'])
