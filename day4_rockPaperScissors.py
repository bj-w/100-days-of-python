import random

# ASCII ART
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

# pick choices
user = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
computer = random.randint(0, 2)

# put ascii into a list for easy printing
images = [rock, paper, scissors]

# print user's choice
print(images[user])

# print computer's choice
print(images[computer])

# decide winner 
win = "You win!"
lose = "You lose!"
draw = "It's a draw"

if user == 0:
    if computer == 1:
        print(f"{lose}")
    elif computer == 2:
        print(f"{win}")
    else:
        print(f"{draw}")
elif user == 1:
    if computer == 0:
        print(f"{win}")
    elif computer == 2:
        print(f"{lose}")
    else:
        print(f"{draw}")
elif user == 2:
    if computer == 0:
        print(f"{lose}")
    if computer == 1:
        print(f"{win}")
    else:
        print(f"{draw}")
else:
    print(f"Unable to play :(")
