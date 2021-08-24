from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/get", methods = ['GET'])
def get_articles():
    return jsonify({
        "Howdy!":"World"
    })

@app.route("/homepage")
def homepage():
    return "Hello Universe. Hello, Heroku. Howdy."

@app.route("/helloworld")
def helloworld():
    return {
        'Hello':'World'
    }

if __name__== '__main__':
    app.run(debug=True)