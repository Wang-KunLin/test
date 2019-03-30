#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import urllib.parse

url = "http://www.baidu.com/index.html;user?id=5#comment"
resu = urllib.parse.urlparse(url)
print(resu)
