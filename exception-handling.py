
a = 5
b = 0

try:
    print("Resource Open")
    print(a / b)
except Exception as e:
    print("Error - ", e)
else:
    print("No Exception")
finally:
    print("Resource Closed")