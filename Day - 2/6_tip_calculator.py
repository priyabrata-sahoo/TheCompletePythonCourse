print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill?"))

tip_percentage = tip / 100
tip_amount = bill * tip_percentage
bill_with_tip = bill + tip_amount
pay_amount = round((bill_with_tip / num_people), 2)

print(f"Each person should pay: {pay_amount}")