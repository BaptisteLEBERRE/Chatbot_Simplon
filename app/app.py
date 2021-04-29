from flask import Flask, render_template, url_for, request
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ChatbotApplication'

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5001, debug=True)