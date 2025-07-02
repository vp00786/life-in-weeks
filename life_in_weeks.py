def life_in_weeks(x):
    r_years = 90 - x
    r_months = r_years * 12
    r_weeks = r_years * 52
    print(f"You have {r_weeks} weeks left.")

# Get age as integer
x = int(input("What is your current age? "))
life_in_weeks(x)
