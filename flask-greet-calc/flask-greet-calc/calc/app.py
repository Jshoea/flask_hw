# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app= Flask(__name__)

@app.route("/add")
def do_add():
    """Add a and b"""

    a= int(request.args.get("a"))
    b= int(request.args.get("b"))
    result= a+b
    return str(result)

@app.route("/sub")
def do_sub():
    """Subtract a and b"""

    a= int(request.args.get("a"))
    b= int(request.args.get("b"))
    result= a-b
    return str(result)

@app.route("/mult")
def do_mult():
    """Multiply a and b"""

    a= int(request.args.get("a"))
    b= int(request.args.get("b"))
    result= a*b
    return str(result)

@app.route("/div")
def do_div():
    """Divide a and b"""

    a= int(request.args.get("a"))
    b= int(request.args.get("b"))
    result= a / b
    return str(result)

@app.route("/math/<oper>")
def do_math(oper):
    """Do Math operation of A & B"""

    a= int(request.args.get("a"))
    b = int(request.args.get("b"))
    result= operators[oper](a,b)

    return str(results)