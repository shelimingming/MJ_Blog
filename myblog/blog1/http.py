import requests
import json
def get(url):
    res = requests.get(url)
    if res:
        resJson = json.loads(res.text)
        return resJson
    return None
