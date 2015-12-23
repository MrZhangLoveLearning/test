# -*- coding: utf-8 -*-
"""Login and simulate choose a class"""

import requests
from requests import Session
from requests.exceptions import RequestException

TIME_OUT = 2.0
LOGIN_HOST = (['http://218.64.56.18/%s',
	'http://218.64.56.18:8080/%s',
	'http://218.64.56.18:8081/%s'])
WRONG_USENAME = "密码错误"
CONECTION_ERROR = "登录失败！"

def login(username, passwd):
	"""Login 

	>>> login('6102114007', '152017')  # doctest: +ELLIPSIS
	<requests.sessions.Session object at 0x...>


	"""
	sesion = Session()
	data = {}
	data['USERNAME'] = username
	data['PASSWORD'] = passwd
	data['useDogCode'] = ''
	data['RANDOMCODE'] = ''
	data['x'] = 22
	data['y'] = 9
	ip = LOGIN_HOST [int(username)%3]
	# print ip
	try:
		res = sesion.post(ip % (''), data=data, timeout=TIME_OUT)
		res = sesion.post(ip % ('Logon.do?method=logonBySSO'),
			data={}, timeout=TIME_OUT)
		if res.ok:
			return sesion
		else:
			return WRONG_USENAME
	except RequestException as error:
		return CONECTION_ERROR

def rob_class(sesion, url):
	try:
		res = sesion.get(url, timeout=TIME_OUT)
		return res.content
	except RequestException as error:
		return CONECTION_ERROR		

def rob(username, passwd, url):
	st1 = login(username, passwd)
	if st1 == WRONG_USENAME:
		return WRONG_USENAME
	if st1 == CONECTION_ERROR:
		return CONECTION_ERROR
	st2 = rob_class(st1, url)
	return st2


if __name__ == '__main__':
	import doctest
	doctest.testmod()



		








