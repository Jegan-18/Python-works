# Reading Data

f = open("MyData", 'r')
# print(f.read())
print(f.readline(), end="")
print(f.readline(), end="")
print(f.readline(), end="")
"""
"""
f = open("MyData", 'r')
# Writing Data
f1 = open("MyData1", "a")
for data in f:
    f1.write(data)


f = open('IMG.png', 'rb')

f1 = open("PIC.jpg", 'wb')

for i in f:
    f1.write(i)