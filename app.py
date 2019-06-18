from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e5686588c7eeb01d4283935cdb94b9ac'

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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'Logged in!', 'success')
        return redirect(url_for('index'))
    else:
        flash('Login unsuccesfull', 'danger')
    return render_template('login.html', title='Login', form=form)
