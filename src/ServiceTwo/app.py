import requests
import fast_json

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def A():
    url = "http://127.0.0.1:5000/otp/9884202442"
    return redirect(url)


@app.route('/home')
def user_form():
    return render_template('index.html', name='crediApp')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
