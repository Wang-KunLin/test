#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests

url = "https://baidu.com/robot.txt"
rp = requests.get(url)
html = rp.text
print(html)
