import requests

def get_btc():
    url = 'https://yobit.net/api/2/btc_usd/ticker/'
    respons = requests.get(url).json()
    btc = respons['ticker']['sell']
    return ('Цена одного биткоина составляет: ' + str(btc) + ' USD')


print(get_btc())