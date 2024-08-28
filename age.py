from datetime import datetime

birth = int(input("Enter Your Birth Date Year = "))

month = int(input("Enter Your Birth Date Month = "))

current_year = datetime.now().year

current_month = datetime.now().month

monthh = current_month - month

year = current_year - birth

total_months = (year) * 12 + (monthh)

if total_months > 1:
    print("Given Month Is Invalid!")

if year > 1:
    print("Given Year Is Invalid!")

else:
    print(f"You Are {year} Years Old And {total_months} Months Old. ")

