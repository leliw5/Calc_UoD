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
        gross = float(round(salary * 10 / 8.64))
    elif type_of_salary == 'net' and cost == 0.5:
        gross = round(float(salary * 10 / 9.15))
    else:
        gross = salary
    tax = round(gross * (1-cost) * value_of_tax)
    net = gross - tax
    result_cost = round(gross * cost)
    result_base = round(gross * (1-cost))
    return render_template('results.html', the_title='Kalkulator wynagrodzeń UoD - Wynik',
                           the_net=net, pit=tax, the_gross=gross, the_cost=result_cost, the_base=result_base)


if __name__ == '__main__':
    app.run(debug=True)