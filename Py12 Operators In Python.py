# # Operators In Python
# 1. Arithmetic Operator
# 2. Assignment Operators
# 3. Comparison Oparetors
# 4. Logical Oparetors
# 5. Membership Oparetors
# 6. Bitwise Oparetors

# ------------ 1. Arithmetic Oparetors ----------------- #
print("Aritmetic Oparetors")
print("9 + 3 is ", 9+3)
print("9 - 3 is ", 9-3)
print("9 * 3 is ", 9*3)
print("9 / 3 is ", 9/3)
print("10 // 3 is ", 10//3)
print("9 ** 3 is ", 9**3)
print("3 % 17 is ", 3%17)

# ------------ 2. Assignment Oparetors ----------------- #
print("Assignment Oparetors")
a = 10
a -= 5
print("a is =",a)

b = 20
b += 5
print("b is =",b)

c = 30
c /= 5
print("c is =",c)

d = 40
d *= 5
print("d is =",d)

f = 53
f //= 5
print("f is =",f)

g = 60
g **= 2
print("g is =",g)

h = 59
h %= 5
print("h is =",h)

i = 50
i &= 5
print("i is =",i)

j = 70
j |= 5
print("j is =",j)

k = 30
k ^= 5
print("k is =",k)

l = 53
l //= 5
print("l is =",l)

m = 60
m **= 2
print("m is =",m)

n = 60
n **= 2
print("n is =",n)


# ------------ 3. Comparison Operators ----------------- #
print("Comparison Operators")
x = 10
print(x==5)
print(x!=5)
print(x>5)
print(x<5)
print(x<=5)
print(x>=5)
# ------------ 4. Logical Operator ----------------- #
print("Logical Operators")
q = True
w = False
print(q or w)
print(q and w)
print(not(q or w))

q1 = 45==2
w1 = 24>5
print(not(q1 and w1))

print("Identitical Operators")
q2 = 50
w2 = 40

print(q2 is w2)
print(type(q2) is type(w2))
print(q2 is not w2)

# ------------ 5. Membership Operators ----------------- #
print("Membership Operators")
list_test = [2,56,48,63,5]
print(56 in list_test)
print(63 not in list_test)

# ------------ 6. Bitwise Operators ----------------- #
print("Bitwise Operators")
print(0 & 1)

input()
exit()