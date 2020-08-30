ls = ["Python", "Java", "C++", "PhP"]
print(ls[0], ls[1], ls[3])

for item in ls:
	print(item)

for i in range(100):
	print(i+1)

Advanced FOR LOOP
Fruits = ["Apple", "Banana", "Coconut", "Grapes", "Orange", "Mango", "Pear", "Guava", "Strawberry", "Dates"]
i = 1
for items in Fruits:
	print("S.No", i, items)
	i=i+2



#Mini Project
print("Enter the number, which's factorial you want to print")
a = int(input(":-"))
print("Enter the maximum number...")
b = int(input(":-"))

for fac in range(b+1):
	if fac % a == 0:
		if fac>1:
			print(fac)

print("For Exit, Press Enter")
input()
exit()