import random

ans = random.randint(1,9)
tries = 0
guess = 0

while guess != ans and tries<3:
  guess = int(input("Guess a number between 1 and 9, you get 3 tries:  "))
  tries = tries+1
  triesleft = 3-tries
  if guess != ans and tries<3:
    print("Try again! You have %s tries left!" % triesleft)
  elif guess != ans:
    print("Sorry! You're out of tries!")
  else:
    print("You got it!")


