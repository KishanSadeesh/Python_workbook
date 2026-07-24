#Task 1

n=1
while n<=10:
    print(n)
    n+=1


#Task 2
n = 10
while n >=1:
    print(n)
    n-=1


#Task 3
n = 1
while n <=20:
    if n % 2 == 0:
        print(n)
    n+=1

#Task 4
n = 1
while n <=20:
    if n % 2 != 0:
        print(n)
    n+=1


#Task 5
n = 1
sum = 0
while n <=50:
    sum += n
    n+=1
print(sum)

#Task 6

n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(i,"x",n,"=",n*i)
    i+=1

#Task 7

n = int(input("Enter a number: "))
count = 0
while n!=0:
    n = n // 10
    count+=1
print(count)


#Task 8

n = int(input("Enter a number: "))
rev = 0
while n!=0:
    temp = n % 10
    rev = rev * 10 + temp
    n = n // 10
print(rev)

#Task 9

n = int(input("Enter a number: "))
a = n
rev = 0
while n>0:
    temp = n % 10
    rev = rev * 10 + temp
    n = n // 10
if rev == a:
    print(a," is a palindrome")
else:
    print(a," is not a palindrome")


#Task 10

n = int(input("Enter a number: "))
a = n
sum = 0
prod = 1
while n>0:
    temp = n % 10
    sum = sum + temp
    prod = prod * temp
    n = n // 10
if sum == prod:
    print(a," is a spy number")
else:
    print(a," is not a spy number")

#Task 11

n = int(input("Enter a number: "))
sum = 0
while n>0:
    temp = n % 10
    sum = sum + temp
    n = n // 10
print(sum)



#Task 12

n = int(input("Enter a number: "))
prod = 1
while n>0:
    temp = n % 10
    prod = prod * temp
    n = n // 10
print(prod)



#Task 13

n = int(input("Enter a number: "))
length = len(str(n))
a = n
arm = 0
while n>0:
    temp = n % 10
    arm = arm + temp ** length
    n = n // 10
if a == arm:
    print(a," is an armstrong number")
else:
    print(a," is not an armstrong number")


import sys

#Task 14

n = int(input("Enter a number: "))
max_val = 0
while n>0:
    temp = n % 10
    if max_val < temp:
        max_val = temp
    n = n // 10
print(max_val)

#Task 15

n = int(input("Enter a number: "))
min = sys.maxsize
while n>0:
    temp = n % 10
    if min > temp:
        min = temp
    n = n // 10
print(min)


#Task 16

n = int(input("Enter a number: "))
a,b = 0,1
while n>0:
    print(a,end=" ")
    c = a + b
    a = b
    b = c
    n-=1

#Task 17
n = int(input("Enter a number: "))
fact = 1
while n>0:
    fact = fact * n
    n-=1
print(fact)

