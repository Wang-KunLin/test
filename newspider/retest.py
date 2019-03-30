#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import re

with open('test.txt', 'r') as f:
    rd = f.read()
print(rd)
pat = re.compile(r'[a-zA-z]+://[^\s]*', re.S)
result = pat.findall(rd)
print(result)
