# How To Use If Else Conditionals
a = 45
b = 12

if a>b:
	print("a Is Greater Than b")

else:
	print("a Is Less Than b")

# User Input If else--
print("Enter The Name Of Your favorite Programming Language.. (First Letter Must Be Capital)")
uin = input(":-")

if uin=="Python":
	# Double Equal (==) is Important. Single Equal (=) will give error.
	print("Woow, You Are Awesome!!")

else:
	print("Nice..")

# Use Of Elif In If Else Conditionals
print("Enter The Name Of Your favorite Programming Language.. (First Letter Must Be Capital)")
uin = input(":-")

if uin=="Python":
	# Double Equal (==) is Important. Single Equal (=) will give error.
	print("Woow, You Are Awesome!!")

elif uin=="Java":
	print("It's Amazing")

elif uin=="PHP":
	print("It's Good")

else:
	print("Nice..")


# Advanced If-Else Statement using a string method.
print("Enter The Name Of Your favorite Programming Language.. (First Letter Must Be Capital And Other Word Must Be In Lowercase)")
uin = input(":-")
checking = uin.capitalize()

if checking==uin:

	if uin=="Python":
            # Double Equal (==) is Important. Single Equal (=) will give error.
            print("Woow, You Are Awesome!!")

	elif uin=="Java":
            print("It's Amazing")

	elif uin=="C++":
            print("It's Good")

	else:
            print("Nice..")

else:
	print("You Enter A Letter-case Case Word, Please Enter A Capitalized Word")

