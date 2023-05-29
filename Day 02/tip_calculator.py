# TIP CALCULATOR
# print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? rs.")
total_bill = float(total_bill)
tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
tip_percent = float(tip_percent / 100)
split = input("How many people to split the bill?")
split = int(split)
tip = total_bill * tip_percent
total = total_bill + tip
bill_per_person = round(total / split, 2)
bill_per_person = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: rs.{bill_per_person}")
