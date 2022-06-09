from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/store')
def store():
    return render_template('store.html')

@app.route('/newarrival')
def newarrival():
    return render_template('newarrival.html')

@app.route('/sale')
def sale():
    return render_template('sale.html')

if __name__ == '__main__':
   app.run()