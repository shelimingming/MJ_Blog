import requests
import json


def get(url):
    res = requests.get(url)
    if res:
        resJson = json.loads(res.text)
        return resJson
    return None


def post(url, body):
    res = requests.post(url, json=body)
    print("post res:" + res.text)
    if res:
        resJson = json.loads(res.text)
        return resJson
    return None
