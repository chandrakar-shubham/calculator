from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_age():
    if request.method == 'POST':
        birth_date = request.form['birth_date']
        current_date = request.form['current_date']
        
        # Convert the input strings to datetime objects
        birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
        current_date = datetime.strptime(current_date, '%Y-%m-%d')
        
        # Calculate the age
        age = current_date - birth_date
        
        # Extract years, months, weeks, days, and minutes
        years = age.days // 365
        remaining_days = age.days % 365
        months = remaining_days // 30
        remaining_days %= 30
        weeks = remaining_days // 7
        days = remaining_days % 7
        minutes = age.total_seconds() / 60
        
        return render_template('age_calculator.html', age=f"{years} years, {months} months, {weeks} weeks, {days} days, {minutes:.2f} minutes")

    return render_template('age_calculator.html', age=None)

if __name__ == '__main__':
    app.run(debug=True)