from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flasktest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text())
    date = db.Column(db.DateTime, default = datetime.datetime.now)
    def __init__(self, title,body):
        self.title = title
        self.body = body

class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'body', 'date' )

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)

@app.route("/get", methods = ['GET'])
def get_articles():
    return jsonify({
        "Howdy!":"World"
    })

@app.route("/add", methods = ['POST'])
def add_article():
    title = request.json['title']
    body = request.json['body']


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