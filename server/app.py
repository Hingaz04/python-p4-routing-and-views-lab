#!/usr/bin/env python3

from flask import Flask, render_template
from flask import Flask

app = Flask(__name__)


if __name__ == '__main__':
    app.run(port=5555, debug=True)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return f'<p>Printed String: {param}</p>'


@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join(str(i) for i in range(param + 1))
    return f'<p>Counting up to {param}:</p><pre>{numbers}</pre>'


def test_print_text(self):
    '''displays text of route in browser.'''
    response = app.test_client().get('/print/hello')
    assert 'hello' in response.data.decode()


@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return '<p>Error: Division by zero</p>'
    elif operation == '%':
        result = num1 % num2
    else:
        return '<p>Error: Invalid operation</p>'

    return f'<p>Result of {num1} {operation} {num2} is: {result}</p>'


if __name__ == '__main__':
    app.run(debug=True)
