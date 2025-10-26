import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0 }
reverseDict = {1: "snake", -1: "water", 0: "gun"}

you = youDict[youstr]

print(f"You Chose{reverseDict[you]}\ncomputer chose{reverseDict[computer]}")

if(computer == you):
    print("It,s a draw")
else:
    '''
    if(computer == -1 and you == 1): (computer - you) = -2
        print("You Win")

    elif(computer == -1 and you ==0): (computer - you) = -1
         print("You lose!") 

    elif(computer == 1 and you == -1): (computer - you) = 2
         print("You lose")

    elif(computer ==1 and you ==0): (computer - you) = 1
         print("You Win")

    elif(computer == 1 and you ==-1): (computer - you) = 1
         print("You lose!")

    elif(computer ==1 and you ==0): (computer - you) = -1
        print("You Win")
        
    The below logic is writte on the basis of teh value of computer - you
    '''
    if((computer - you)== -1 or (computer - you) == 2):
        print("You lose")
    else:
        print("You Win") 

   