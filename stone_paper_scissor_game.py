

import random

rock = ('''     _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) ''')

paper = ('''     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________) ''')

scissor = ('''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) ''')

print("welcome to the stone paper scissor game\n")

userchoice = int(input("enter 1 for rock , 2 for paper , 3 for scissor\n"))
if userchoice == 1:
    print(rock)
elif userchoice == 2:
    print(paper)
else:
    print(scissor)

compchoice = random.randint(1, 3)
if compchoice == 1:
    print(rock)
elif compchoice == 2:
    print(paper)
else:
    print(scissor)

if userchoice == 1:
    if compchoice == 2:
        print("you lose!")
    elif compchoice == 3:
        print("you win!")
    else:
        print("its a draw :0")
elif userchoice == 2:
    if compchoice == 3:
        print("you lose!")
    elif compchoice == 1:
        print("you win!")
    else:
        print("its a draw :0")
else:
    if compchoice == 1:
        print("you lose!")
    elif compchoice == 2:
        print("you win!")
    else:
        print("its a draw :0")

print("\n thank you for playing !!")
