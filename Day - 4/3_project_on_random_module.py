# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# Import the random module here
import random
total_input_num = (len(names))

random_choice = random.randint(1, total_input_num - 1)

person_who_pay = names[random_choice]

print(f"{person_who_pay} is going to buy the meal today!")