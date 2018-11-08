# -*- coding: utf-8 -*-

import requests
import json


def play(src):
    url = 'http://audigo.local/audio/v1/play/block'
    d = json.dumps({"src": src})
    try:
        requests.post(url, data=d, timeout=0.1)
    except:
        import traceback
        traceback.print_exc()

