from Prime import Prime

print ("Which number you want to test is prime or not")
num = int(input())
p1 = Prime(num)
print ("%d is prime?"% num)
print (p1.isPrime())
