a = 6
b = 9

print(a, b)


# 1. Swapping Without Using Third Variable

a, b = b, a
print(a, b)


# 2. Swapping Using Third ( Temp ) Variable

temp = a
a = b
b = temp

print(a,b)
