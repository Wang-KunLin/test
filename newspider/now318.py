#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url("https://www.baidu.com/robot.txt")
rp.read()
print(rp.can_fetch("*", "https://www.baidu.com/s?word=python&tn=50000021_hao_pg&ie=utf-8&sc=UWd1pgw-pA7EnHc1FMfqnHRdnW6LPHbzrjfkPBuW5y99U1Dznzu9m1YkPj6snjfdPjRd&ssl_sample=s_108&srcqid=2940283942648705041&H123Tmp=nu"))
