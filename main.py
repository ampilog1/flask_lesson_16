from flask import Flask, render_template, request

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


@app.get('/results/')
def result():
    data = ['python', 'js', 'java', 'sql', 'lua']
    return render_template('results.html', data=data)


@app.get('/run/')
def run_get():
    with open('main.txt', 'r') as f:
        text = f.read()
    return render_template('form.html', text=text)


@app.post('/run/')
def run_post():
    text = request.form['input_text']
    with open('main.txt', 'a') as f:
        f.write(f'{text}\n')
    return render_template('results.html', text=text)


if __name__ == '__main__':
    app.run(debug=True)
