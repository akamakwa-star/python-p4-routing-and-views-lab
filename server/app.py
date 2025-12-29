#!/usr/bin/env python3

from flask import Flask, Response

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<text>')
def print_text(text):
    print(text)
    return text


@app.route('/count/<int:n>')
def count(n):
    lines = '\n'.join(str(i) for i in range(n)) + ('\n' if n > 0 else '')
    return Response(lines, mimetype='text/plain')


@app.route('/math/<int:x>/<op>/<int:y>')
def math(x, op, y):
    if op == '+':
        result = x + y
    elif op == '-':
        result = x - y
    elif op == '*':
        result = x * y
    elif op == 'div':
        result = x / y
    elif op == '%':
        result = x % y
    else:
        return Response('Invalid operation', status=400)
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
