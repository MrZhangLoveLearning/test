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
		infos = main.parse_electric_info(content)
		return jsonify(infos)

if __name__=='__main__':
	app.run()