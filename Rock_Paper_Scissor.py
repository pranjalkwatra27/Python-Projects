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
import random

moves = [scissors, paper, rock]

rat = int(input("2 for rock, 1 for paper, 0 for scissors: "))
if rat not in [0, 1, 2]:
    print("Wrong Input!")
else:
    print("You chose:", moves[rat])

    # Computer input
    comp = random.randint(0, 2)
    print("Computer chose:", moves[comp])

    # Winner logic
    if rat == comp:
        print("Tie!")
    elif (rat == 0 and comp == 1) or (rat == 1 and comp == 2) or (rat == 2 and comp == 0):
        print("You win!")
    else:
        print("Computer wins!")
