## Use Of Break Statement
# i = 0
# while (True):
# 	i = i+1
# 	print(i)
# 	if i==24:
# 		break

## Example of Break statement with "end="
# i = 0
# while (True):
# 	i = i+1
# 	print(i, end=" ")
# 	if i==24:
# 		break

## Use Of Continue in loops
# a = 0
# while True:
# 	a = a+1
# 	if a<5:
# 		continue
# 	print(a, end=" | ")
# 	if a==20:
# 		break

## Another Example Of Continue Statement
b = 0
while True:
	b = b+1
	if b<7:
		print("Continue =", b)
		continue

	print("Normal =", b, end=".. ")
	if b==23:
		break