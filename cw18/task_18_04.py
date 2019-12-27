# Создать сайт. При запросе на домашнюю страницу отображается текущая дата.

from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return "Hello world!"


@app.route('/')
def time():
    date = str(datetime.now().date())
    return date


if __name__ == '__main__':
    app.run()
