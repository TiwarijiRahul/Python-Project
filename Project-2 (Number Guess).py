
#Guess the Number.#
import random
target = random.randint(1,100)

while True:
    user_num = input("Guess the num or Quit: ")
    if (user_num == "Quit"):
        print("----GAME Quit----")
        break
    user_num = int(user_num)

    if user_num == target:
        print("Correct",target)
        break
    if user_num>target:
        print("Take a small num")
    
    else:
        print("Target num is Big")

print("Game Over")