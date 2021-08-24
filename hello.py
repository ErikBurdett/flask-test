from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Hello Universe"

if __name__== '__main__':
    app.run(debug=True)