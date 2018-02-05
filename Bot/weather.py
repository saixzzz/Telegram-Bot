import requests

def get_weather():
    url = 'https://api.darksky.net/forecast/36a7973cd96ac98dc0fa71dfa9ecb308/49.8398093,23.9935223'
    respons = requests.get(url).json()
    temperature = respons['currently']['temperature']
    celsius = (temperature - 32) / 1.8
    return ('Температура во Львове в данный момент составляет ' + '%.2f' % celsius) + ' градусов цельсия'

print(get_weather())