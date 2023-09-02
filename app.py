# app.py

from flask import Flask, request, render_template
from age_calculator import calculate_age

app = Flask(__name__)

@app.route('/age_calculator', methods=['GET', 'POST'])
def age_calculator():
    if request.method == 'POST':
        birth_date = request.form['birth_date']
        current_date = request.form['current_date']
        
        # Call the calculate_age function to get age in various formats
        age_result = calculate_age(birth_date, current_date)
        
        return render_template('age_calculator_result.html', age_result=age_result)

    return render_template('age_calculator.html')

if __name__ == '__main__':
    app.run(debug=True)
