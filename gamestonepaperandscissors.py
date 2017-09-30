import random
r=["stone","paper","scissors"]
computer=r[random.randint(0,2)]
player=input("enter the choice");
if player==computer:
      print("draw")
elif player=="paper":
      if computer=="scissors":
          print("lose","computer has",computer)
      else:
          print("won","computer has",computer)
elif player=="stone":
      if computer=="paper":
          print("lose","computer has",computer)
      else:
          print("won","computer has",computer)
elif player=="scissors":
      if computer=="paper":
         print("lose","computer has",computer)
      else:
          print("won","computer has",computer)
