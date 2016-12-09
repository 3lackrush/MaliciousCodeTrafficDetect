#!/usr/bin/env python
#coding:utf-8

import requests

proxies = {
    "http":"socks5://127.0.0.1:1080",
    "https":"socks5://127.0.0.1:1080"
}

r = requests.get("http://www.google.com",proxies=proxies,timeout=5)

print("HTTP STATUS CODE:"+str(r.status_code))

