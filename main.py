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

# Write your code below this line 👇

import random

images = [rock, paper, scissors]



user_input = int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors?\n"))
print(images[user_input])


print("Computer chose:")
computer_input = random.randint(0, 2)
print(images[computer_input])



if user_input == 0 and computer_input == 2:
    print("You win!")
elif user_input == 1 and computer_input == 0:
    print("You win!")
elif user_input == 2 and computer_input == 1:
    print("You win!")
elif user_input == 2 and computer_input == 0:
    print("You lose!")
elif user_input == 1 and computer_input == 2:
    print("You lose!")
elif user_input == 0 and computer_input == 1:
    print("You lose!")
elif user_input == computer_input:
    print("Draw!")
