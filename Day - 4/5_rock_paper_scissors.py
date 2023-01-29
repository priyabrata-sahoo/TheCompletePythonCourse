rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [rock, paper, scissors]
option_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(options[option_choose])

import random

print("Computer chose:")
random_number = random.randint(0, 2)
print(options[random_number])

if option_choose >= 3 or option_choose < 0: 
  print("You typed an invalid number, you lose!") 
elif option_choose == 0 and random_number == 2:
  print("You win!")
elif random_number == 0 and option_choose == 2:
  print("You lose")
elif random_number > option_choose:
  print("You lose")
elif option_choose > random_number:
  print("You win!")
elif random_number == option_choose:
  print("It's a draw")



