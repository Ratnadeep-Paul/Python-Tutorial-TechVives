mystr = "Hi, This Is Ratnadeep"

print(mystr[0])
# Name of the Variable[Which Number Character We Want]

print("\n")
# For A Gap

print(mystr[0])
print(mystr[1])
print(mystr[4])
print(mystr[5])
print(mystr[6])
print(mystr[7])

print(len(mystr))
# len(Name of the variable)

print(mystr[0:9])
# Default = VariableName[0:length] In this case default = mystr[0:21]

numstr = "0123456789"
print(numstr[0:5])
print(numstr[2:9])
print(numstr[1:84])
""" 
Here we enter a number which is greater than the actual length of the string
but this will not give us any error. It  just print the maximum character the string has 
"""

# To Gap 1 Character--
print( numstr[0:10:2] )
# Default Value = 0:<length of string>:1 But Is this case the default = 0:10:1

# To Gap 2 Character--
print(numstr[0:10:3])

# You can also use the potion slicing in this--
print(numstr[2:9:2])

# We will also get the same output, if we write like this--
print(numstr[::2], numstr[0::2], numstr[:10:2])

astr = "This Is TechVives"

print(astr[0:-1])
print(astr[0:-2])
print(astr[2:-5])

str = "This is TechVives"

a = str.count("i")
print(a)

# Default = find("Name Of The Words or Character, You Want To Find")
b = str.find("Vives")
print(b)

# Default Value = Replace("words or character you want to change", "With the word you want to change")
c = str.replace("Tech", "Knowledge")
print(c)

e = str.upper()
print(e)

f = str.title()
print(f)