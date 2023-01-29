number = int(input("Which number do you want to check? "))
num_check = number % 2

if num_check == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")