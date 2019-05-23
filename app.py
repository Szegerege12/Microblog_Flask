from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [

    {
        'author': ' Marek Sieńko',
        'title': 'Post testowy 1',
        'content': ' content content',
        'date': '21 maja 2019'
    },
    {
        'author': ' Kamil Lemiesz',
        'title': 'Post testowy 2',
        'content': ' content content',
        'date': '22 maja 2019'
    }
]


@app.route("/")
def index():
    return render_template('index.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')
