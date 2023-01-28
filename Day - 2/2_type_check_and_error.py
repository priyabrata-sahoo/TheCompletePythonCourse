# type checking
# it’ll print type as int.
num_char = len( input("What is your name?\n") )
print( type(num_char) )

# it’ll print type as str.
a = str(123)
print(type(a))

# it’ll print type as int.
a = int(123)
print(type(a))

# type error
# this error can be resolved by converting the integer to a string before concatenating it with the string.
num_char = len(input("What is your name?\n"))
print("Your name has " + num_char + " characters.")

# this program prompts the user to enter their name
# then calculates the number of characters in their name and displays the result in the form of "Your name has [number of characters] characters."
num_char = len(input("What is your name?\n"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")
