# coding:utf-8
from flask import Flask, abort, jsonify, request
import sys
import main
app = Flask(__name__)
app.debug=True
app.secret_key='api'

@app.route('/api/get/<username>', methods=['GET', 'POST'])
def get_info(username):
    if request.method == 'POST':
        abort(404)
    content = main.get_text(username)
    if not content:
        return 'login fail'
    else:
        try:
            infos = main.parse_electric_info(content)
            return jsonify(infos)
        except IndexError as in_error:
            return 'wrong username'


@app.route('/api/post', methods=['GET', 'POST'])
def post_info():
    if request.method == 'GET':
        abort(404)
    else:
        try:
            username = request.form.get('UserName')
            if username:
                content = main.get_text(username)
                if content:
                    infos = main.parse_electric_info(content)
                    return jsonify(infos)
            else:
                return 'wrong username'

        except IndexError as in_error:
            return 'wrong username'

        

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8000)