from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import math

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///palindromes.db'
db = SQLAlchemy(app)

class Palindromes(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    palindrome = db.Column(db.Integer, nullable=False)
    cycles = db.Column(db.Integer)



def rev(num):
    return int(num != 0) and ((num % 10) * \
             (10**int(math.log(num, 10))) + \
                          rev(num // 10))

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('/index.html')




if __name__ == "__main__":
    app.run(debug=True)
# TODO: change debug mode
