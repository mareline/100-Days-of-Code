bill = float(input("What was the total bill?"))
percentage = int(input("What total percentage do you want to tip? 10, 12, or 15?"))
people = int(input("How many people are splitting the bill?"))

tip_percentage = percentage / 100 + 1
total_bill = bill * tip_percentage
split = total_bill / people
total_amount = round(split, 2)
print(f"Each person should pay {total_amount}.")