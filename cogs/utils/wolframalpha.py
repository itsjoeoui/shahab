import random
from os.path import join, dirname, os
import requests
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)
TOKEN = os.getenv('WOLFRAM_TOKEN')

serviceurls = {
    'simple': 'http://api.wolframalpha.com/v1/simple?',
    'short': 'http://api.wolframalpha.com/v1/result?'
}

quickreplies = (
    "Wtf is this shit??",
    "Bruh you're kidding me lmao",
    "Give me a joint instead of this shit",
    "I'm depressed",
    "Lol kill yourself",
    "I can't solve this lmao",
    "Aight I'm out"
)

def get_full_result(keyword):
    r = requests.get(serviceurls['simple'], params={'appid': TOKEN, 'i': keyword})
    with open('cache/wolfram_result.jpg', 'wb+') as handler:
        handler.write(r.content)

def get_short_result(keyword):
    r = requests.get(serviceurls['short'], params={'appid': TOKEN, 'i': keyword})
    if r.text == "Wolfram|Alpha did not understand your input":
        return random.choice(quickreplies)
    return r.text
