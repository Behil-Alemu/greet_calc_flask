# Put your app in here.
from unittest import result
from operations import add, sub, div, mult
from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def adding():
    """Add a plus b"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(add(a,b))

@app.route('/sub')
def subtracting():
    """subtract a minus b"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(sub(a,b))

@app.route('/mult')
def multiplying():
    """Multiply a times b"""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(mult(a,b))

@app.route('/div')
def dividing():
    """Divide a by b"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(div(a,b))


oper = {
    'add': add,
    'sub': sub,
    'div': div,
    'mult': mult
}

# @app.route('/math/<operation>')
# def do_math(operation):
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     num = (a,b)
#     result = map(oper[operation], num)
#     return str(result)


@app.route('/math/<operation>')
def do_math(operation):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = oper[operation](a,b)
    return str(result)

# why can I not return a number 

