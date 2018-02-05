import requests
from python.MyPython.Задания.Bot import weather, bitcoin
from time import sleep
import json

token = '443380377:AAEBXdl6AQygW12r1qby9fMcS5Dg2c8i9Zk'
#https://api.telegram.org/bot443380377:AAEBXdl6AQygW12r1qby9fMcS5Dg2c8i9Zk/sendmessage?chat_id=263183896&text=Hello

URL = 'https://api.telegram.org/bot' + token + '/'


def get_updates():
    url = URL + 'getupdates'
    response = requests.get(url)
    return response.json()


def get_message():
    data = get_updates()

    last_object = data['result'][-1]
    current_update_id = last_object['update_id']

    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id

      #                          бида  -164201925       макс #-225446429
        chat_id = -225446429  #263183896  #last_object['message']['chat']['id'],

        message_text = last_object['message']['text']
        message = {
            'chat_id': chat_id,
            'text': message_text
        }
        return message
    return None


def send_message(chat_id, text):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def main():
    d = get_updates()
    with open('updates.json', mode='w') as file:
        json.dump(d, file, indent=2, ensure_ascii=True)
        while True:
            answer = get_message()

            if answer is not None:

                chat_id = answer['chat_id']

                text = answer['text']

                if text == '/101':
                    send_message(chat_id, text='Привет, кожанные ублюдки')
                continue

                if text == '/погода':
                    send_message(chat_id, weather.get_weather())

                if text == '/btc':
                    send_message(chat_id, bitcoin.get_btc())

                else:
                    sleep(2)


main()
if __name__ == '__name__':
    main()
