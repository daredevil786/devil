import random
r=["stone","paper","scissors"] #range
computer=r[random.randint(0,2)]
player=input("enter the choice");
if player==computer:
      print("draw")
elif player=="paper": #condition for paper outcome
      if computer=="scissors":
          print("lose","computer has",computer)
      else:
          print("won","computer has",computer)
elif player=="stone": #condition for stone outcome
      if computer=="paper":
          print("lose","computer has",computer)
      else:
          print("won","computer has",computer)
elif player=="scissors": #condition for scissors outcome
      if computer=="paper":
         print("lose","computer has",computer)
      else:
          print("won","computer has",computer)
