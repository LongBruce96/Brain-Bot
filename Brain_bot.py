from flask import Flask, render_template, url_for

app = Flask(__name__, static_url_path='/static')


@app.route('/homepage', methods=['GET', 'POST'])
def home_page():
    return render_template('home-page.html')

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    return render_template('cart.html')

@app.route('/createaccount', methods=['GET', 'POST'])
def create_account():
    return render_template('create-account.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/prdt1', methods=['GET', 'POST'])
def prdt1():
    return render_template('prdt1.html')

if __name__ == '__main__':
  app.run(host = '127.0.0.1', port=8000, debug=True)
 