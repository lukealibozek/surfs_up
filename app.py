from flask import Flask

app = Flask(__name__)
# You probably noticed the __name__ variable inside of the Flask() function. 
# Let's pause for a second and identify what's going on here.
# 
# This __name__ variable denotes the name of the current function. 
# You can use the __name__ variable to determine if your code is being run 
# from the command line or if it has been imported into another piece of code. 
# Variables with underscores before and after them are called magic methods in Python.

@app.route('/')
def hello_world():
    return 'Hello world'