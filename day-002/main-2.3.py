current_age = input("What is your current age?\n")
years_left = 90 - int(current_age)
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")