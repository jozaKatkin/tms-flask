# Создать шаблон с формой Имя, фамилия, возраст.
# Передать данные на вью дописать эти данные в файл


from flask import Flask, request

app = Flask(__name__)


@app.route('/write_data', methods=['POST'])
def write_data():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form["age"]
        with open('test.txt', 'w') as f:
            f.write(f'{first_name} - {last_name} - {age}\n')
    return 'Saved'


if __name__ == '__main__':
    app.run()
