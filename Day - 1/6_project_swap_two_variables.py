# prompts the user to input two values, "a" and "b"
a = input("a: ")
b = input("b: ")

# creates a variable "c" which is assigned the value of "a"
c = a
# swaps the values of "a" and "b" by assigning the value of "b" to "a" and the value of "c"
a = b
b = c

# prints the new values of "a" and "b" to the user
print("a: " + a)
print("b: " + b)
