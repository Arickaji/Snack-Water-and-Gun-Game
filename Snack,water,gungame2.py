import random
print("Welcome to the Snack,Water and Gun Game")
print("Press p for play")
play = input()
if play=='p':
    # this is a mode 1. is  single mode and 2. is double mode 
    print("Which mode you play: Press 1. single mode Press 2.Double Mode")
    mode = int(input())
    if mode==1:
        print("You enter the game mode 1")
        UserPoint = 0
        ComputerPoint = 0
        print("\nYou enter the game.")
        print("How many time you play and please remember you select the odd numbers:")
        time = int(input())
        for i in range(time):
           print("s for Snack,w for Water , and g for gun")
           choice = input().lower()

           if choice=='s':
              choice = "Snack"
           elif choice == 'w':
              choice = "Water"
           elif choice == 'g':
              choice =="Gun"
           else:
             print("Wrong input,please check your input")
             break    

           print(f"You choose:{choice}")
           lst = ["Snack","Water","Gun"]
           computer = random.choice(lst)
           print(f"computer choose :{computer}")
    
    # this is a condition about the match tie
    
           if choice=="Snack" and computer=="Snack":
              print("Math tie both 0 point")
    
           elif choice=="Water" and computer=="Water":
              print("Math tie both 0 point")
    
           elif choice=="Gun" and computer=="Gun":
              print("Math tie both 0 point")

    # this is a main condition     
    
       # this is a user win condition
    
           elif choice=="Snack" and computer=="Water":
             print("You Win,You get a 1 point.")
             UserPoint = UserPoint + 1
    
        
           elif choice=="Water" and computer=="Gun":
             print("You Win, You get a 1 point.")
             UserPoint = UserPoint + 1

    
           elif choice=="Gun" and computer=="Snack":
             print("You Win,You get a 1 point.")
             UserPoint = UserPoint + 1

       # this is a computer win condition
    
           elif choice=="Water" and computer=="Snack":
             print("Computer Win,computer get a 1 point.")
             ComputerPoint = ComputerPoint + 1
    
           elif choice=="Gun" and computer=="Water":
             print("Computer Win,computer get a 1 point.")
             ComputerPoint = ComputerPoint + 1

           elif choice=="Snack" and computer=="Gun":
             print("Computer Win,computer get a 1 point.")
             ComputerPoint = ComputerPoint + 1

        print(f"\nUser point : {UserPoint}")
        print(f"Computer point : {ComputerPoint}")   

    # this is a who win the match code 
        if UserPoint==ComputerPoint:
          print("Game Over,Both players are  Win")
        elif UserPoint>ComputerPoint:
          print("User Win the match.")
          print("Game Over")
        elif ComputerPoint>UserPoint:
          print("Computer Win the match.")
          print("Game Over") 

    # this is a mode 2 code 
    elif mode==2:
        user1Point = 0
        user2Point = 0
        print("Welcome to the Double Mode:")
        print("How many time you play game:")
        time1 = int(input())
        for i in range(time1):
            # this is a user 1 input
            print("User:1 chance")
            print("s for Snack , w for Water , g for Gun")
            user1 = input().lower()

            if  user1=='s':
              user1 = "Snack"
            elif user1 == 'w':
              user1 = "Water"
            elif user1 == 'g':
              user1 =="Gun"  
            else:
             print("Wrong input,please check your input\n")
             break   

            # this is a user 1 input
            print("User:2 chance")
            print("s for Snack, w for Water, g for Gun")
            user2 = input().lower()

            if user2=='s':
                user2="Snack"
            elif user2=='w':
                user2="Water"
            elif user2=='g':
                user2="Gun"
            else:
             print("Wrong input,please check your input\n")
             break      


            # this is a condition
            # this is a condition of win the user 1
            if user1==user2:
                print("Match Tie,Both are 0 point")
            elif user1=="Snack" and user2=="Water":
                print("User 1 Win")
                print("User 1 get the 1 point.")
                user1Point = user1Point + 1 
            elif user1=="Water" and user2=="Gun":
                print("User 1 Win")
                user1Point = user1Point + 1 
                print("User 1 get the 1 point.")

            elif user1=="Gun" and user2=="Snack":
                print("User 1 Win")
                print("User 1 get the 1 point.")   
                user1Point = user1Point + 1 

            # this is a condition of win the user 2
            
            elif user1=="Water" and user2=="Snack":
                print("User 2 Win")
                print("User 2 get the 1 point.") 
                user2Point = user2Point + 1

            elif user1=="Gun" and user2=="Water":
                print("User 2 Win")
                print("User 2 get the 1 point.")
                user2Point = user2Point + 1 
                 
            elif user1=="Snack" and user2=="Gun":
                print("User 2 Win")
                print("User 2 get the 1 point.")
                user2Point = user2Point + 1

        print(f"User:1 point {user1Point}")
        print(f"User:2 point {user2Point}")

        # this is a who win the match code 
        if user1Point==user2Point:
          print("Game Over,Both players are  Win")
        elif user1Point>user2Point:
          print("User 1 Win the match.")
          print("Game Over")
        elif user2Point>user1Point:
          print("Computer Win the match.")
          print("Game Over")


                 
# This is a quit the game 
print("Quit the game press q:")
Quit = input()
if Quit=='q':
    print("\nSee you Later,How many star you give for this game.")
    star =int(input())
    printstar = u"\u2605\t" * star
    print(printstar)
    print("\nThank you we hope you like this game.")

                               
    
