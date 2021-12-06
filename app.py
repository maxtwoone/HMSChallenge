from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import math
import Palindrome

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///palindromes.db'
db = SQLAlchemy(app)


class Palindromes(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    palindrome = db.Column(db.Integer, nullable=False)
    cycles = db.Column(db.Integer)


def rev(num):
    return int(num != 0) and ((num % 10) * \
                              (10 ** int(math.log(num, 10))) + \
                              rev(num // 10))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['number'].isdigit() and int(request.form['number']) <= 10_000:
            number = int(request.form['number'])
            palindrome = Palindrome.palindrome(number)[0]
            cycles = Palindrome.palindrome(number)[1]
            return render_template('/index.html', number=number, palindrome=palindrome, cycles=cycles)
        else:
            return 'Your number is not an integer between 1 and 10,000'

    return render_template('/index.html')


@app.route('/Database', methods=['GET', 'POST'])
def database():
    if request.method == 'POST':
        number = int(request.form['number2'])
        palindrome = int(request.form['palindrome2'])
        cycles = int(request.form['cycles2'])
        new_palindrome = Palindromes(number=number, palindrome=palindrome, cycles=cycles)
        try:
            db.session.add(new_palindrome)
            db.session.commit()
            return redirect('/Database')
        except:
            return 'There was an issue adding the palindrome to the database'
    else:
        palindromes = Palindromes.query.order_by(Palindromes.number).all()
        return render_template('database.html', palindromes=palindromes)


if __name__ == "__main__":
    app.run(debug=True)
# TODO: change debug mode
