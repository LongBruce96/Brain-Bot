from flask import Flask, render_template, url_for

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

if __name__ == '__main__':
  app.run(host = '127.0.0.1', port=8000, debug=True)
 