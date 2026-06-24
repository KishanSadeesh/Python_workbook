'''
#Task1

C = float(input("Enter Celcius: "))
F = (C * 1.8) + 32
print("Fahrenheit: ", F)

#Task 2


P = int(input("Enter Principal amount : "))
N = int(input("No of years: "))
R = float(input("Rate of Interest : "))

SI = (P * R * N)/ 100
print("Simple Interest : ", SI)

#Task 3

n = int(input("Enter Number: "))

print("Square value : ", n**2)
print("cube value : ", n**3)

#Task 4

duration = float(input("Enter hours as decimal : "))
print("Hours : ", int(duration))
print("Minutes : ", int((duration - int(duration))*60))


#Task 5

a = int(input("Enter Subject A marks : "))
b = int(input("Enter Subject B marks : "))
c = int(input("Enter Subject C marks : "))
total = a+b+c
print("total sum of marks : ", total)
print("average score : ", total/3)

#Task 6

num = int(input("Enter three digit number : "))
print("First digit: ",num//100)
num = num % 100
print("Second digit: ", num//10)
num = num % 10
print("Third digit: ", num)


#Task 7

a = int(input("Enter a value : "))
b = int(input("Enter b value : "))

a = a ^ b
b = a ^ b
a = a ^ b
print("a value : ", a)
print("b value : ", b)


#Task 8

amount = int(input("Enter amount: "))
num500 = amount // 500
remain = amount - (num500 * 500)
num100 = remain // 100
print("No of 500s : ", num500)
print("no of 100s : ", num100)


#Task 9

n = int(input("Enter total days : "))
weeks = n // 7
left = n - (weeks * 7)
print("No of weeks : ", weeks)
print("No of days left: ", left)



#Task 10

n = int(input("Enter two digit number : ")) #45
rev = (n % 10) * 10    #rev = 50
n = n //10             #n = 4
rev += n               #rev = 54
print("Reverse numbers : ",rev)

'''









