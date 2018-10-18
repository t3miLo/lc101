from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc


# app configuration

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mys3cr3tk3y'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:Jeremiah@localhost:3306/build-a-blog'


# database
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(25))
    title = db.Column(db.String(25), nullable=False)
    body = db.Column(db.String(225), nullable=False)

    def __init__(self, author, title, body):
        self.author = author
        self.title = title
        self.body = body


@app.route('/', methods=['GET', 'POST'])
@app.route('/blog', methods=['GET', 'POST'])
def index():

    posts = reversed(Blog.query.all())
    print(posts)

    if request.method == 'POST':
        return redirect(url_for('newPost'))

    return render_template('index.html', posts=posts)


@app.route('/newpost', methods=['GET', 'POST'])
def newPost():

    if request.method == 'POST':
        author = request.form['author']
        title = request.form['title']
        body = request.form['body']

        if len(title) == 0 or len(body) == 0:
            flash("You can't leave the title or body empty", "error")
        elif len(author) == 0:
            author = 'Anonymous'
            new_post = Blog(author, title, body)
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            new_post = Blog(author, title, body)
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('newpost.html')


if __name__ == '__main__':
    app.run()
