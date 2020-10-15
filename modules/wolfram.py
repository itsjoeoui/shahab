import requests
from os.path import join, dirname, os
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)
TOKEN = os.getenv('WOLFRAM_TOKEN')

serviceurl = "http://api.wolframalpha.com/v1/simple?"

def get_full_result(keyword):
    r = requests.get(serviceurl, params = {'appid': TOKEN, 'i': keyword})
    with open('cache/wolfram_result.jpg', 'wb+') as handler:
        handler.write(r.content)
