import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("WOLFRAM")

serviceurls = {
    "simple": "http://api.wolframalpha.com/v1/simple?",
    "short": "http://api.wolframalpha.com/v1/result?",
}


def get_full_result(keyword):
    r = requests.get(serviceurls["simple"],
                     params={
                         "appid": TOKEN,
                         "i": keyword
                     })
    filename = "cache/wolfram.jpg"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "wb") as handler:
        handler.write(r.content)


def get_short_result(keyword):
    r = requests.get(serviceurls["short"],
                     params={
                         "appid": TOKEN,
                         "i": keyword
                     })
    if r.text == "Wolfram|Alpha did not understand your input":
        return "Sorry, I did not understand your input..."
    return r.text
