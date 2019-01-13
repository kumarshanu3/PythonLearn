print ("Give a number divisible by 3")
number = int(input())
for i in range(1,number+1):
    print()
    for j in range(1,i):
        print("*", end = " ")
    print("*", end = " ")
    for j in range(1,i):
        print("*", end = " ")
