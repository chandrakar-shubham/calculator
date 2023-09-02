from datetime import datetime

def calculate_age(birth_date, current_date):
    # Convert input strings to datetime objects
    birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
    current_date = datetime.strptime(current_date, '%Y-%m-%d')
    
    # Calculate age
    age = current_date - birth_date
    
    # Extract years, months, and days
    years = age.days // 365
    remaining_days = age.days % 365
    months = remaining_days // 30
    days = remaining_days % 30
    
    # Calculate weeks, hours, minutes, and seconds
    weeks = age.days // 7
    hours = age.seconds // 3600
    minutes = (age.seconds % 3600) // 60
    seconds = age.seconds % 60
    
    # Create formatted strings for different units
    age_years_months_days = f"{years} years {months} months {days} days"
    age_months_days = f"{years * 12 + months} months {days} days"
    age_weeks_days = f"{weeks} weeks {days} days"
    age_days = f"{age.days} days"
    age_hours = f"{age.days * 24 + hours} hours"
    age_minutes = f"{age.days * 24 * 60 + hours * 60 + minutes} minutes"
    age_seconds = f"{age.days * 24 * 3600 + age.seconds} seconds"
    
    return {
        'years_months_days': age_years_months_days,
        'months_days': age_months_days,
        'weeks_days': age_weeks_days,
        'days': age_days,
        'hours': age_hours,
        'minutes': age_minutes,
        'seconds': age_seconds
    }