# -*- coding: utf-8 -*-

import requests
import json


def play(src):
    url = 'http://audigo.local/audio/v1/play/block'
    d = json.dumps({"src": src})
    requests.post(url, data=d, timeout=0.1)

