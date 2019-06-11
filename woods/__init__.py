from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/woodsking'

db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('woods/home.html')


@app.route('/about_us')
def about_us():
    return render_template('woods/about_us.html')


@app.route('/contact_us')
def contact_us():
    return render_template('woods/contact_us.html')


@app.route('/our_products')
def our_products():
    return render_template('woods/our_products.html')