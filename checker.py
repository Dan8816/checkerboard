from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('checkers.html', num1 = 4, num2 = 4)

@app.route('/<Exx>/<Why>')

def xy(Exx,Why):
    Int1=int(Exx)/2
    Int2=int(Why)/2
    return render_template('checkers.html', num1 = int(Int1), num2 = int(Int2))


app.run(debug=True)