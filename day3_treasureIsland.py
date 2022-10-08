print('''         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
########################################      
''')
print('Welcome to treasure island...')
q_one = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()
if q_one == 'left':
    q_two = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if q_two == 'wait':
        q_three = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if q_three == 'yellow':
            print("Congratulations - you have won the treasure! :)")
        elif q_three == 'blue':
            print("Sorry but you were eaten by beats. GAME OVER!")
        elif q_three == 'red':
            print("Sorry but you were burnt alive. GAME OVER!")
        else:
            print("There isn't a door with that colour. GAME OVER")
    else:
        print("Sorry but you were attacked by trout. GAME OVER!")
else:
    print("Sorry but you fell into a hole. GAME OVER!")