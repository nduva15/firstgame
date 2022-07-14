import math
import random

print("Welcome to my new game!... ")

name = input("What is your name? ")
age = int(input("how old are you? "))
print("Hello, your name is", name, "and you are ", age, " years old")
health = 10
print("you start the game with 10 health")
if age >=18:
  print("You are old enough to play!... ")
  wants_to_play = input("Do you want to play a story game? ").lower()
  if wants_to_play == "yes":
    print("Lets play ")
    left_or_right = input("You are walking and you spot a village on your left and a forest on your right. Do you go left or right? (left/right) ")
    if left_or_right == "left":
      print("You are safer in a village than a forest.")
      ans = input("You see a lake, do you go around or across? (around/across) ")
      if ans == "around":
        print("You won ... ")
      else:
        print ("You lost 5 health ...")
        health -=5
    else:
      print ("You lost 5 health ")
      health -=5
  else:
    print("You wish to try another game? (yes/no) ")
    ans = input("Try another game ... ")
    if ans == "yes":
      print("Lets play a guessing game ...")
      guess = int(input("Guess any number (1/2) "))
      if guess == 1:
        print("You guessed correctly . You won ")
      else:
        print("You lost ")
    else:
     
        print("End game .... ")
else:
  print("Not old enough to play ")
