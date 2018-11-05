# -*- coding: utf-8 -*-

import grequests
import json

def play(src):
    url = 'http://audigo.local/audio/v1/play/block'
    d = json.dumps({"src": src})
    req = grequests.post(url, data=d, timeout=0.1)
    grequests.map([req])

