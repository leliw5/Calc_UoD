from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main_page() -> 'html':
    return render_template('index.html', the_title='Kalkulator wynagrodzeń UoD')


@app.route('/results', methods=['POST'])
def results():
    type_of_salary = request.form['type_of_salary']
    salary = float(request.form['salary'])
    cost = float(request.form['cost_income'])
    value_of_tax = 0.17
    if type_of_salary == 'net' and cost == 0.2:
        net = salary
        gross = net * 10 / 8.64
    elif type_of_salary == 'net' and cost == 0.5:
        net = salary
        gross = net * 10 / 9.15
    else:
        gross = salary
        net = gross * (1-cost) * value_of_tax

    tax = gross * cost * value_of_tax
    return str(round(gross)) + '  ' + str(round(tax)) + '  ' + str(round(net))


if __name__ == '__main__':
    app.run(debug=True)