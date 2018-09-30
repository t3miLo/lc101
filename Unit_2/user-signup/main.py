from flask import Flask, render_template, url_for
from form import SignUpForm


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Jeremiah1010'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SignUpForm()
    if form.validate_on_submit():
        name = form.username.data
        return 'You are now registered! Welcome %s' % (name)
    return render_template('index.html', form=form)


app.run()
