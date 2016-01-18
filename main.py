# -*- coding: utf-8 -*-
"""Login and simulate choose a class"""

import requests
from requests import Session
from requests.exceptions import RequestException

TIME_OUT = 5.0
# LOGIN_HOST = (['http://218.64.56.18/%s',
# 	'http://218.64.56.18:8080/%s',
# 	'http://218.64.56.18:8081/%s'])
LOGIN_HOST = (['http://218.64.56.18:80/%s',
	'http://218.64.56.18:80/%s',
	'http://218.64.56.18:80/%s'])
WRONG_USENAME = "密码错误"
CONECTION_ERROR = "连接超时！请稍后再试"

def login(username, passwd, url=None):
	"""Login 

	>>> login('6102114000', '000000')  # doctest: +ELLIPSIS
	<requests.sessions.Session object at 0x...>


	"""
	sesion = Session()
	data = {}
	data['USERNAME'] = username
	data['PASSWORD'] = passwd
	data['useDogCode'] = ''
	data['x'] = 37
	data['y'] = 8
	ip = LOGIN_HOST [int(username)%3]
	try:
		res = sesion.post(ip % ('Logon.do?method=logon'), data=data, timeout=TIME_OUT)
		res = sesion.post(ip % ('Logon.do?method=logonBySSO'), timeout=TIME_OUT)
		if res.ok:
			return sesion
		else:
			return WRONG_USENAME
	except RequestException as error:
		return CONECTION_ERROR

def rob_class(sesion, url):
	"""rob_class

	

	"""
	try:


		res = sesion.get(url, timeout=TIME_OUT)
		return res.content
	except RequestException as error:
		return CONECTION_ERROR		

def rob(username, passwd, url):
	"""rob

	>>> rob('6102114007', '152017', "xkglAction.do?method=xsxk&xnxq01id=2015-2016-2&jx0502id=2130902BC92B4FECAE3544969A5B24D9&type=1&jx0504id=201520162024524&xf=2&kch=T5520Z0014&zxs=32&jx02kczid=null&zzdxklbname=1&szkcfl=25&kcsx=2&kcsj=&kczc=&kcid=DE9D64E3D1C17618E040007F01001C1D") 

	"""
	ip = LOGIN_HOST [int(username)%3] % url
	print ip
	st1 = login(username, passwd)
	if st1 == WRONG_USENAME:
		return WRONG_USENAME
	if st1 == CONECTION_ERROR:
		return CONECTION_ERROR
	st2 = rob_class(st1, ip)
	print st2
	return st2


if __name__ == '__main__':
	import doctest
	doctest.testmod()



		








