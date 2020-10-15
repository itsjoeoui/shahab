import requests
from os.path import join, dirname, os
from dotenv import load_dotenv
from xml.dom import minidom

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)
TOKEN = os.getenv('WOLFRAM_TOKEN')

serviceurl = "http://api.wolframalpha.com/v1/result?"

def get_short_result(keyword):
    r = requests.get(serviceurl, params = {'appid': TOKEN, 'i': keyword})
    return(r.text)
