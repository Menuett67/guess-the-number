import random
from art import logo
print(logo)
rand_number=random.randint(1,100)
def hard():
  print("You have 5 attempts remaining to guess the number.")
  should_continue=True
  attempts=5
  while should_continue:
    guess=int(input("Make a guess:"))
    if guess==rand_number:
      print(f"you got it.The answer was {guess}")
    else:
      if guess>rand_number:
        print("too high.")
      elif guess<rand_number:
        print("too low.")
      attempts-=1
    if attempts==0:
      should_continue=False
      print("You've run out of guesses, you lose.")
def easy():
  print("You have 10 attempts remaining to guess the number.")
  should_continue=True
  attempts=10
  while should_continue:
    guess=int(input("Make a guess:"))
    if guess==rand_number:
      print(f"you got it.The answer was {guess}")
    else:
      if guess>rand_number:
        print("too high.")
      elif guess<rand_number:
        print("too low.")
      attempts-=1
    if attempts==0:
      should_continue=False
      print("You've run out of guesses, you lose.")
print("Welcome to the Number Guessing Game !")
print("I'm thinking of a number between 1 and 100.")  
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty=="hard":
  hard()
elif difficulty=="easy":
  easy()
  
