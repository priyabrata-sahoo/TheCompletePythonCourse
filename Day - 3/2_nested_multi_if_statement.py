print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age? "))
    if age < 12:
        bill = 5
        print(f"You have to pay {bill}$.")
    elif age <= 18:
        bill = 7
        print(f"You have to pay {bill}$.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print(f"You have to pay {bill}$.")

    want_photo = str(input("Do you want a photo taken? Y or N. "))
    if want_photo == "Y":
        bill += 3
        print(f"Your final bill is {bill}$.")
else:
    print("You can't ride the rollercoaster!")