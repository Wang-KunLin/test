#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from requests import Request, Session

url = "https://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/72.0.3626.121 Safari/537.36"
}
s = Session()
re = Request('POST', url, headers)
pre = s.prepare_request(re)
r = s.send(pre)
print(r.text)
