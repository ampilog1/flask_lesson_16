from flask import Flask, render_template, request
from Flask_parser import parce

app = Flask(__name__)


@app.get("/")
def index():
    main_data = {'https://v-a-c.org/ges2'}
    return render_template('index.html', main_data=main_data)


@app.get("/contacts/")
def contacts():
    developer_name = 'Demon'
    # context = {'name': developer_name}
    return render_template('contacts.html', name=developer_name)


@app.get('/results/')
def result():
    data = parce()
    return render_template('results.html', data=data)


@app.get('/run/')
def run_get():
    main_data = {'https://v-a-c.org/ges2'}
    return render_template('form.html', text=main_data)


@app.post('/run/')
def run_post():
    text = request.form['input_text']
    with open('main.txt', 'a') as f:
        f.write(f'{text}\n')
    return render_template('results.html', text=text)


if __name__ == '__main__':
    app.run(debug=True)
