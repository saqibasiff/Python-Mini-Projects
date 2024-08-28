from datetime import datetime

# Get the user's birth year and month
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month (1-12): "))

# Get the current date
current_date = datetime.now()

# Calculate total months
total_months = (current_date.year - birth_year) * 12 + (current_date.month - birth_month)

# Print the result
print(f"You are {total_months} months old.")