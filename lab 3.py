#Task1

n = str(input("Enter your name: "))
for i in range(1,6):
    print(n)


#Task2
print("Numbers from 1 to 20: ")
for i in range(1,21,1):
    print(i)

#Task3

print("Numbers from 20 to 1: ")
for i in range(20,0,-1):
    print(i)


#Task4
print("Even numbers from 1 to 50: ")
for i in range(1,51):
    if i % 2 == 0:
        print(i)
        
#Task5
print("Odd numbers from 1 to 50: ")
for i in range(1,51):
    if i % 2 != 0:
        print(i)  

#Task6

sum = 0
for i in range(1,11):
    sum += i
print(sum)


#Task7

n = int(input("Enter number:"))
for i in range(1,11,1):
    print(i," x ",n," = ", n*i)


#Task8

s = str(input("Enter name:"))
count = 0
for i in s:
    count += 1
print("Count of letters : ",count)



#Task9

word = str(input("Enter word : "))
for i in word:
    print(i)



#Task10

name = str(input("Enter name:"))
vowel = ['a','e','i','o','u']
count = 0
for c in name:
    if c in vowel:
        count += 1
print("Count of vowels: ",count)


#Task11

n = int(input("Enter number:"))
for i in range(n):
    for j in range(n):
        if i==j or i+j == n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()


#Task12

n = int(input("Enter value: "))
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()

''' ---------------------------------------- '''

s = "madam"
for i in s:
    for j in s:
        if i == j:
            print(j,end="")
        else:
            print(" ",end="")
    print()







