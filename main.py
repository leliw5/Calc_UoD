from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main_page() -> 'html':
    return render_template('index.html', the_title='Kalkulator wynagrodzeń UoD')


@app.route('/results', methods=['POST'])
def results():
    return request.form['salary'] + '  ' + request.form['cost_income']


if __name__ == '__main__':
    app.run(debug=True)