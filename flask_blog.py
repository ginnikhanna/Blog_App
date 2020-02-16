# import Flask class
from flask import Flask
# creating app variable to an instance of the Flask class __name__ is the name of the module
app = Flask(__name__)
# Creating routes. Routes are the addresses we type in the browser. It is a decroator.
@app.route("/")
@app.route("/home")
def home():

    '''Simply returninng a simple string'''

    return "<h1> Home Page </h1>"

@app.route('/about')
def about():
    return "<h1> About Page </h1>"

if __name__ == '__main__':
    app.run(debug = 'True')