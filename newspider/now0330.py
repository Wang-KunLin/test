#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
import re

url = "https://www.zhihu.com/explore"
header = {"User-Agent": '''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
 Chrome/72.0.3626.121 Safari/537.36'''}
rp = requests.get(url, header)
html = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
title = re.findall(html, rp.text)
print(title)

