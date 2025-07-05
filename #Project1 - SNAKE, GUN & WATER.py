#Project1 - SNAKE, GUN & WATER

import random
def game ():

    snake = 1
    water = -1
    Gun = 0
    print("Choose from 1, -1, 0")
    computer =random.choice([1,0,-1])
    
    you = int(input("enter num: "))
    print("Comp val: ",computer)
    print("You val: ",you)
    if(computer == you):
        print("Draw")
    else:
        if(computer ==1 and you == 0):
            print("You win")
        elif(computer == 1 and you == -1):
            print("You loose")
        elif(computer == -1 and you ==1):
            print("you win")
        elif(computer == -1 and you== 0):
            print("you loose")
        elif(computer==0 and you==1):
            print("You win")
        elif(computer== 0 and you == -1):
            print("you loose")

        else:
            print("something went wrong")
    

game()

        
