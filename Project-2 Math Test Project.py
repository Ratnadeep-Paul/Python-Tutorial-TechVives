# Import Section
import random

# Variable Section
score = 0

# Introduction Section
print("Welcome To The Math Test")
print("Here We Will Ask You 10 Random equations, And you need to enter the correct Answer")
print("After Competing All 10 Questions, We Will Give You The Mark You Earned (Between 0 to 10).. ")

# First Question--
a = random.randint(4, 100)
b = random.randint(4, 100)
print("Your First Question Is--")
print(a, "+", b, "=??")
user_input = int(input(":-|"))

if user_input==a+b:
    print("Your Answer Is Correct....")
    score= score+1
else:
    print("Oops!! You Are Wrong....")
    print("The Correct Answer Is ==", a+b)

# Second Question--
a = random.randint(4, 150)
b = random.randint(a, 150)
print("Your Second Question Is--")
print(b, "-", a, "=??")
user_input = int(input(":-|"))

if user_input==b-a:
    print("Your Answer Is Correct....")
    score= score+1
else:
    print("Oops!! You Are Wrong....")
    print("The Correct Answer Is ==", b-a)


# Third Question--
a = random.randint(4, 400)
b = random.randint(a, 400)
print("Your Third Question Is--")
print(b, "-", a, "=??")
user_input = int(input(":-|"))

if user_input==b-a:
    print("Your Answer Is Correct....")
    score= score+1
else:
    print("Oops!! You Are Wrong....")
    print("The Correct Answer Is ==", b-a)

# Fourth Question--
a = random.randint(4, 400)
b = random.randint(4, 400)
print("Your Fourth Question Is--")
print(a, "+", b, "=??")
user_input = int(input(":-|"))

if user_input==a+b:
    print("Your Answer Is Correct....")
    score= score+1
else:
    print("Oops!! You Are Wrong....")
    print("The Correct Answer Is ==", a+b)


# Fifth Question--
a = random.randint(4, 200)
b = random.randint(4, 40)
print("Your Fifth Question Is--")
print(a, "*", b, "=??")
user_input = int(input(":-|"))

if user_input==a*b:
    print("Your Answer Is Correct....")
    score= score+1
else:
    print("Oops!! You Are Wrong....")
    print("The Correct Answer Is ==", a*b)


# Sixth Question--
a = random.randint(4, 600)
b = random.randint(a, 600)
print("Your Sixth Question Is--")
print(b, "-", a, "=??")
user_input = int(input(":-|"))

if user_input==b-a:
    print("Your Answer Is Correct....")
    score= score+1
else:
    print("Oops!! You Are Wrong....")
    print("The Correct Answer Is ==", b-a)

# Seventh Question--
a = random.randint(4, 400)
b = random.randint(4, 50)
print("Your Seventh Question Is--")
print(a, "*", b, "=??")
user_input = int(input(":-|"))

if user_input==a*b:
    print("Your Answer Is Correct....")
    score= score+1
else:
    print("Oops!! You Are Wrong....")
    print("The Correct Answer Is ==", a*b)


# Eighth Question--
a = random.randint(4, 600)
b = random.randint(4, 600)
print("Your Eighth Question Is--")
print(a, "+", b, "=??")
user_input = int(input(":-|"))

if user_input==a+b:
    print("Your Answer Is Correct....")
    score= score+1
else:
    print("Oops!! You Are Wrong....")
    print("The Correct Answer Is ==", a+b)

# Ninth Question--
a = random.randint(4, 800)
b = random.randint(4, 800)
print("Your Ninth Question Is--")
print(a, "+", b, "=??")
user_input = int(input(":-|"))

if user_input==a+b:
    print("Your Answer Is Correct....")
    score= score+1
else:
    print("Oops!! You Are Wrong....")
    print("The Correct Answer Is ==", a+b)

# Last Question--
a = random.randint(4, 100)
b = random.randint(4, 99)
print("Your Last Question Is--")
print(a, "*", b, "=??")
user_input = int(input(":-|"))

if user_input==a*b:
    print("Your Answer Is Correct....")
    score= score+1
else:
    print("Oops!! You Are Wrong....")
    print("The Correct Answer Is ==", a*b)

# Final Score Release
print("All Questions Are Completed")
if score==10:
    print("Congratulations, You Got 10 Out Of 10")
else:
    print("Well Try..  You got", score, "Points, out of 10")

# Exiting..
input("Please Press ENTER to Exit")
exit()
