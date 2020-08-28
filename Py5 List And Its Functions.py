# To make a list, we just need to do---

list_language = ["Python", "HTML", "Java", "C++", "JavaScript"]
print(list_language)

list2 = ["Snapdragon", 854.99,]
print(list2)


# Slicing Methods---

list_language = ["Python", "HTML", "Java", "C++", "JavaScript"]

print(list_language[1])
print(list_language[0:2])

list3 = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]

print(list3[0::2])  # we can also write this like = [::2], [0:10:2], [:10:2]
print(list3[2:9:3])


# List Functions---

# Built-In Methods
foods = ["Pizza", "Chips", "Ice-cream", "Chicken"]
foods[3] = "Egg"
print(foods)

# Append Function
foods.append("Doughnut")
print(foods)


# Extend Function
fruits = ["Orange", "Banana", "Mango", "Apple"]
foods.extend(fruits)
print(foods)

# Pop Function
foods.pop(1)
# Numbering start from 0
print(foods)

# Insert Function
foods.insert(2, "Egg")
print(foods)

# Remove Function
foods.remove("Chips")
print(foods)

# Sort Function
nums = [74, 7, 5, 9, 45, 99]
strnums = ["88", "55", "11", "33", "44"]

foods.sort()
nums.sort()
strnums.sort()

print("Foods are" ,foods)
print("Numbers are", nums)
print(strnums)

# Reverse Function
nums.sort()
nums.reverse()
print(nums)


## Tuples---
tup = (4, 6, 8, 9)
# This is a tuple.

print(tup)
# we need to print it to get any output

# Error Shows-
# tup = (4, 6, 8, 9)
#
# tup[1]= 10
# print(tup)
