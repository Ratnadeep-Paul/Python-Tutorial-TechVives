# Print Type Of Set
a_set = set()
print(type(a_set))

# We can store a list using two methods.
# 1.Method -- Directly write the list-
a_set = set(["C++", "PHP", "Python", "HTML"])

# 2.Method -- Make a list variable and insert the variable-
ls = ["C++", "PHP", "Python", "HTML"]
b_set = set(ls)

print(a_set, "And",  b_set)

# Try To Add Same Multiple Value
lang = set(["PHP", "Python", "PHP"])
# Here we write "PHP" 2 Times but it will Print only 1 time.
print(lang)


# Add() Function Of Set
lang = set(["PHP", "Python", "Java"])
lang.add("C++")
print(lang)

# Intersection() Of Set
lang = set(["PHP", "Python", "Java"])
snake = set(["Viper", "Anaconda", "Python"])
intsct = snake.intersection(lang)
print(intsct)

# Symmetric_difference() Function Of Set
lang = set(["PHP", "Python", "Java"])
snake = set(["Viper", "Anaconda", "Python"])
sym_differ = snake.symmetric_difference(lang)
print(sym_differ)

# Union() Function Of Set
lang = set(["PHP", "Python", "Java"])
snake = set(["Viper", "Anaconda", "Python"])
a = snake.union(lang)
print(a)
