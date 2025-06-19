import requests
import time
import os

API_URL = 'https://api.telegram.org/bot'
API_CATS_URL = 'https://random.dog/woof.json'
BOT_TOKEN = os.getenv('TOKEN')
ERROR_TEXT = 'Картинка не появилась, увы :(('

offset = -2
counter = 0
cat_response: requests.Response
cat_link: str

while counter <= 100:
    print('attempt =', counter)
    response = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if response['result']:
        for result in response['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()['url']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')
    time.sleep(1)
    counter += 1