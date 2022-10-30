from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def index():
    main_data = {
        'a': 'A',
        'b': 'B',
        'c': 'C'
    }
    context = {
        'name': 'Leo',
        'age': 99
    }
    return render_template('index.html', main_data=main_data, **context)


@app.get("/contacts/")
def contacts():
    developer_name = 'Demon'
    # context = {'name': developer_name}
    return render_template('contacts.html', name=developer_name)


@app.get('/result/')
def result():
    data = ['python', 'js', 'java', 'sql', 'lua']
    return render_template('result.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
