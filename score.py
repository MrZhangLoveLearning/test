# -*- coding: utf-8 -*-
# @Date    : 2016-01-16 11:46:10
# @Author  : Zhang Lun (2529450174@qq.com)
# @Link    : https://github.com/MrZhangLoveLearning

import requests
import main

def get_score(username, passwd):
	session = main.login(username, passwd)
	url = 'http://218.64.56.18/xszqcjglAction.do?method=queryxscj'
	res = session.post(url, data={'kksj':'2015-2016-1'})
	return res.content
