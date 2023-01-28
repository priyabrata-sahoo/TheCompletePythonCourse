height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height = int(height)
weight = float(weight)

# using multiplication & division
bmi = (weight / (height * height))

new_bmi = int(bmi)

print(new_bmi)