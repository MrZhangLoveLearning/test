# coding:utf-8
from flask import Flask,session,redirect,escape,request,abort,jsonify
import sys
import main
app = Flask(__name__)
app.debug=True
app.secret_key='api'
@app.route('/api/<username>')
def get_info(username):
	content = main.get_text(username)
	if not content:
		# abort(404)
		return 'login fail'
	else:
		try:
			infos = main.parse_electric_info(content)
			return jsonify(infos)
		except IndexError as in_error:
			return 'wrong username'

		

if __name__=='__main__':
	app.run(host='0.0.0.0', port=8000)