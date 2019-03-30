#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from requests import Session, Request
import re


url = "https://www.baidu.com"
headers = {"User-Agent": '''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
 Chrome/72.0.3626.121 Safari/537.36'''}
sx = Session()
rp = Request('POST', url, headers)
pr = sx.prepare_request(rp)
pse = sx.send(pr)
print(pse.text)

