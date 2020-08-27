name = "Nick"
age = 30
height = 5.9

# Print Variables----------
print(name)
print(age)
print(height)

# Print Variable's Type----------
print(type(name))
print(type(age))
print(type(height))

# Examples to add multiple String variables----------
name1 = "Tech"
name2 = "Vives"

"""
This is inside of a multi line comments
So, here we make 2 string variable
now we will add them inside the print() statement
"""

print(name1+name2)
print(name1, name2)

# we can also add extra data with variables inside the print() statement.

print(name1 + " is my life")
print(name1, 56*2) # here we use commas because Plus will give us errors.
print(name1 + "nology" , "is everywhere")

# Examples to add multiple Numeric variables----------
num1 = 50
num2 = 10.5

"""
So, here we make 1 int variable (Integer) and one float variable.
now we will add them inside the print() statement
"""
print(num1, num2)
print(num1+num2)

# we can also multiply, subtract, divide these variable's data(number).
print(num1-num2)
print(num1*num2)
print(num1/num2)

# we can also add extra data with variables inside the print() statement.
print(num1+80-20)
print(num2*2 + 4)

#Type Casting Of Variables----------
# Three Different Types of variables
str_var = "Hello"
int_var = 45
float_var = 20.2

print(str(int_var)+str_var)

"""
In general, If we try to add any integer or float with any String, than it gives us error. But here it will not give us error, because here we convert the int_var into a string using str().
"""

print("\n") # we write this escape for get a gap between two lines

str_var2 = "58"

print(int(str_var2) + float_var)

"""
Normally, we can't add any str with float, but here we typecast the str_var2 into a integer using int(). So, it will not gives us any error.
"""

# Take Inputs And Store in Variables----------
print("Please write something and press Enter")
user_input = input()
"""
This is the code to take inputs from user("input()") and store it in a variable.
"""
print("you inputted =", user_input )

# Example of Taking Inputs And Store them in Variables and Print them----------
inpu1 = input("What is your name\n:-")
"""
We can add any string, inside the input's bracket to print it. And I write "\n" to get a new line where we can enter the input. If we don't add "\n" than we need to enter the input alongside with the written string and it looks very bad. If wan't to see it, than you can try it (without "\n").
"""

print("Hii", inpu1, "You are amazing!!")