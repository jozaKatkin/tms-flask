# Создать сайт. При запросе по урлу /my_word/[word],
# в случае если длина слова четна - выводит строку содержащую все
# нечетные элементы строки(abcde -> ace). В ином случае просто выводит слово.

from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/even_word/<even_word>')
def even(even_word):
    return even_word[::2]


@app.route('/odd_word/<odd_word>')
def odd(odd_word):
    return odd_word


@app.route('/my_word/<word>')
def check_word(word):
    if not len(word) % 2:
        return redirect(url_for('even', even_word=word))
    else:
        return redirect(url_for('odd', odd_word=word))


if __name__ == '__main__':
    app.run()
