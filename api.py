# -*- coding: utf-8 -*-

from flask import Flask, abort, jsonify, request
from functools import wraps
from flask import make_response
import sys
import main
app = Flask(__name__)
app.debug=True
app.secret_key='api'

def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        # rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Content-Type'] = 'text/html;charset=utf-8'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst
    return wrapper_fun




@app.route('/api/post', methods=['GET', 'POST'])
@allow_cross_domain
def post_info():
    if request.method == 'GET':
        abort(404)
    else:
        try:
            username = request.form.get('USERNAME')
            passwd = request.form.get('PASSWORD')
            url = request.form.get('URL')
            if username and passwd and url:
                content = main.rob(username, passwd, url)
                if content:
                    return content
            else:
                return "不能为空"

        except IndexError as in_error:
            return 'wrong username'

        

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8585)