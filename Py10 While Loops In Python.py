i = 0
while (i<45):
	print("HI", i, "TIMES")
	i = i+1


# Print  List Item
# Printing The Item In Reverse--
a = ["apple", "ball", "cat", "doll", "egg", "fish", "grapes","hen", "ice"]
while a:
	print(a.pop(-1))


# Another Way To Printing List Items--
a = ["apple", "ball", "cat", "doll", "egg", "fish", "grapes","hen", "ice"]
b = 0
while b<len(a):
	print(a[b])
	b = b+1


#Mini Project-- Table Printer
print("Enter The The Number, Which's Table You Want To Print")
num = int(input(":-"))

max = num*10
x = 0
y= 0
while (x<max+1):
	print(num,"*", y, "=",x)
	x = x+num
	y=y+1

input("Press Enter To Exit")
exit()