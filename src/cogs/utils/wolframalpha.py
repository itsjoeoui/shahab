import random
from os.path import join, dirname, os
import requests

TOKEN = os.getenv('WOLFRAM_TOKEN')

serviceurls = {
    'simple': 'http://api.wolframalpha.com/v1/simple?',
    'short': 'http://api.wolframalpha.com/v1/result?'
}

def get_full_result(keyword):
    r = requests.get(serviceurls['simple'], params={'appid': TOKEN, 'i': keyword})
    with open('cache/wolfram_result.jpg', 'wb+') as handler:
        handler.write(r.content)

def get_short_result(keyword):
    r = requests.get(serviceurls['short'], params={'appid': TOKEN, 'i': keyword})
    if r.text == "Wolfram|Alpha did not understand your input":
        return 'Sorry, I did not understand your input...'
    return r.text
