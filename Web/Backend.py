from flask import Flask, send_file, jsonify
from intake import avgCurr
from intake import calculate_slope_and_intercept,calculate_concentration

app = Flask(__name__)
@app.route('/')
def hello_world():
    return send_file('home.html')

@app.route('/avg_current')
def avg_current():
    return send_file('avg_curr.html')

@app.route('/index')
def index():
    return send_file('index.html')

@app.route('/concentration')
def get_concentration():
    concentration = calculate_concentration('./Book1.xlsx', 'conc', 'current') 

    return 

@app.route('/intake')
def intake_route():
    return str(avgCurr)

@app.route('/slope_intercept')
def slope_intercept():
    slope, intercept = calculate_slope_and_intercept('./Book1.xlsx', 'conc', 'current')
    return jsonify({'slope': slope, 'intercept': intercept})


if __name__ == '__main__':
    app.run(debug=True)


