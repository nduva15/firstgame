print("Welcome to my game! ")
name = input("What is your name? ")
age = int(input("What is your age? "))
print("Your name is", name, "and you are", age, "years old")
health = 10


if age >=18:
  print("You are old enough to play")
  
        
  wants_to_play = input("Do you want to play? ").lower()
  if wants_to_play == "yes":
    
    print("Lets play... ")
    right_or_left = input("Do you want to go ... left or right(left/right)? ")
    
    if right_or_left == "left":
      
      print("you are correct ... ")
      ans = input("nice, you got to a river, do you swim around or across? ")
      if ans == "across":
        
        print("you went across and lost 5 health ")
        health -=5
        ans = input("you notice a hospital and a house. where do you go to recover?(hospital/house ")
        if ans == "house":
          print("You lost 5 health ... ")
          health -=5
              
        else:
          print("You won! ")
        
      elif ans == "around":
       print("You went around and reached the other side ")
      else:
        print("you failed")
    else:
        print("Goodbye! ")
else:
 print("Not old enough to play ")
  
