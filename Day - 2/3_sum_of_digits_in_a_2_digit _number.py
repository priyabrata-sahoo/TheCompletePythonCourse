# Once the user enters a number and hits enter, the program will store it as "two_digit_number"
two_digit_number = input("Type a two digit number: ")

#Get the first and second digits using subscripting then convert string to int.
first_digit = int(two_digit_number[0])
last_digit = int(two_digit_number[1])

#Add the two digits together
two_digit_number = first_digit + last_digit

print(two_digit_number)