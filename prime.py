num = 11
if num > 2 :
    for i in range(3, num, 2):
        if num % 2 == 0:
            print("Not Prime")
            break
        elif num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")