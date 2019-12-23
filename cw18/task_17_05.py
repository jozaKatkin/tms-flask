# Создать сайт. При запросе по урлу /two_in/[number] возвращает 2 в степени number

from flask import Flask

app = Flask(__name__)


@app.route('/two_in/<int:number>')
def power(number):
    return f"{2 ** number}"


if __name__ == '__main__':
    app.run()
