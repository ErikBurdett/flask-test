from flask import Flask


app = Flask(__name__)

@app.route("/")
def homepage():
    return "Hello Universe. Hello, Heroku. Howdy."

@app.route("/helloworld")
def helloworld():
    return {
        'Hello':'World'
    }
if __name__== '__main__':
    app.run(debug=True)