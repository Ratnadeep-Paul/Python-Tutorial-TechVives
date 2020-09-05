# Import Section
import random

# Printing Section
print("Welcome To The Guess The Number Game")
print("This Is A Terminal Game. Here You Have To Find The Correct Number")
print("You Have 10 Chances To Find The Correct Number Between 1-50")

# Variable Section
a = 1
b = 9
number = random.randint(1, 50)

# Loop Section For Main Function
while a<11:
    a = a + 1
    user_input = input("Enter Your Guessed Number\n:-|")
    if user_input.isnumeric()==True:
        input_num = int(user_input)
        if input_num==number:
            print("Congratulations!! You Win This Game")
            break
        else:
            if input_num>number:
                print("Oops!! You Entered Greater Number. Try Again With A Lesser Number")
            else:
                print("Oops!! You Entered Lesser Number. Try Again With A Greater Number")

            print("You Have", b, "Chances Left!!")
            b = b-1
            if b == -1:
                print("Game Over!!! You Lose The Game.. Can You Try This Again??")
                break
    else:
        print("You Enter Something Wrong (Alphabetic Input Are Not Supported).. Please Try Again")

# Exiting----
input("\nPress Enter To Exit")
exit()