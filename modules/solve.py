import requests
from os.path import join, dirname, os
from dotenv import load_dotenv
from xml.dom import minidom
import random

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)
TOKEN = os.getenv('WOLFRAM_TOKEN')

serviceurl = "http://api.wolframalpha.com/v1/result?"

quickreply = [
    "Wtf is this shit??", 
    "Bruh you're kidding me lmao", 
    "Give me a joint instead of this shit", 
    "I'm depressed",
    "Lol kill yourself", 
    "I can't solve this lmao", 
    "Aight I'm out"
]

def get_short_result(keyword):
    r = requests.get(serviceurl, params = {'appid': TOKEN, 'i': keyword})
    if r.text == "Wolfram|Alpha did not understand your input":
        return random.choice(quickreply)    
    return(r.text)
    