#Task 1
m = int(input("Enter mark: "))
if m >= 35:
    print("Passed")
else:
    print("failed")



#Task 2

a = int(input("Enter age: "))
if a >=18:
    print("Eligible to vote")
else:
    print("Not eligible")



#Task 3

bill = int(input("enter bill: "))
if bill > 5000:
    print("Final amount: ",bill - (bill*10/100))
else:
    print("Final amount: ", bill)
    

#Task 4

u = str(input("Enter username: "))
p = str(input("Enter password: "))
if u == "kishan" and p == "01234":
    print("Verified")
else:
    print("Invalid")


    
#Task 5

g = int(input("Enter grade : "))
if g>=90 and g<=100:
    print("Grade : A")
elif g>=75 and g<=89:
    print("Grade : B")
elif g>=50 and g<=74:
    print("Grade : C")
else:
    print("Fail")


#Task 6

a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))
op = str(input("Enter operator: "))

if op == '+':
    print("Addition: ", a + b)
elif op == '-':
    print("Subtraction: ", a - b)
elif op == '*':
    print("Multiplication: ", a * b)
elif op == '/':
    print("Division: ", a / b)
else:
    print("Invalid operator")


#Task 7

u = int(input("Enter Units: "))
if u >= 0 and u <=100:
    print("Total cost : ₹", u * 2);
elif u >= 101 and u <=200:
    print("Total cost : ₹", u * 3);
else:
    print("Total cost : ₹", u * 5);


#Task 8

a = int(input("Enter age: "))
if a < 5 and a>0:
    print("Free tickets")
elif a>=5 and a<=12:
    print("Ticket fare : ₹50")
else:
    print("Ticket fare : ₹100")


#Task 9

s = int(input("Enter salary: "))
if s > 30000:
    c = int(input("Enter credit: "))
    if c > 700:
        print("Loan Approved")
    else:
        print("Not enough credits")
else:
    print("Loan Rejected")


#Task 10

a = int(input("Enter score : "))
if a>=60:
    ent = int(input("Enter entrance exam score: "))
    if ent > 70:
        print("Eligible for college admission")
    else:
        print("Rejected, Not enough marks in extrance exam")
else:
    print("Academics marks does not meet the criteria")



#Task 11

p = int(input("Enter degree percentage : "))
if p >= 65:
    a = int(input("Enter aptitude Score: "))
    if a >= 75:
        print("Eligible in company")
    else:
        print("Sorry not eligible because of low aptitude score")
else:
    print("Not eligibe")



#Task 12

sc = int(input("Enter score : "))
if sc >= 80:
    a = int(input("Enter attendance percentage: "))
    if a >= 75:
        print("Eligible for scholarship")
    else:
        print("Oops Not eligible.. Low attendance")
else:
    print("Not eligible")
    

#Task 13

total = 20000
a = int(input("Enter amount to withdraw: "))
if a <=total:
    pin = str(input("Enter pin: "))
    if pin == "1402":
        print("Success!!")
    else:
        print("Wrong pin")
else:
    print("Insufficient balance")


#Task 14

u = str(input("Enter Username: "))
if u == "kishan":
    print("username correct")
    p = str(input("Enter password: "))
    if p == "10453":
        print("correct password")
        otp = int(input("Enter otp : "))
        if otp == 1234:
            print("Success")
        else:
            print("Wrong otp")
    else:
        print("Oops!!! Wrong password")
else:
    print("Sorry Username invalid!!!!")



#Task 15

d = str(input("Enter whether doctor is available or not(Yes/No) : "))
if d == "Yes" or d == "yes":
    print("Yes doctor is available")
    s = str(input("Enter whether appoinments slots are avalilabe or not(Yes/No) : "))
    if s == "Yes" or s == "yes":
        print("Yes slots are available")
    else:
        print("Slots are not avalilable")
else:
    print("Sorry!!! no Doctor available for this moment")



#Task 16

isreg = str(input("Enter whether student is registerd or not(Yes/No) : "))
if isreg == "Yes" or isreg == "yes":
    print("Yes student is registered")
    ispaid = str(input("Enter whether student paid fees or not(Yes/No) : "))
    if ispaid == "yes" or ispaid == "Yes":
        print("Yes student paid fees")
    else:
        print("No student did not pay fees")
else:
    print("Student did not even register for course")




#Task 17

e = int(input("Enter year of experience : "))
if e >=3:
    r = int(input("Enter rating : "))
    if r>=8:
        print("Eligible for bonus")
    else:
        print("No eligible for bonus because of rating")
else:
    print("Not eligible")


#Task 18    

total = 5000
isAvail = str(input("Is Hall ticket available(Yes/No): "))
if isAvail == "yes" or isAvail == "Yes" :
    print("Hall ticket is available")
    fees = int(input("Enter fees paid: "))
    if total - fees == 0:
        print("Total fees Paid... Eligible for exam")
    else:
        print("Remaining fees have to be paid is Rs.", total-fees)
else:
    print("Sorry hall ticket is not available")
    



#Task 19


isRoom = str(input("Enter whether student is selected or not(Yes/No) : "))
if isRoom == "Yes" or isRoom == "yes":
    print("Yes student is selected for room")
    isavail = str(input("Enter whether student paid fees or not(Yes/No) : "))
    if isavail == "yes" or isavail == "Yes":
        print("Yes!!! Rooms are available")
    else:
        print("OOps:( Rooms are not available")
else:
    print("Student is not selected for hostel allotment")



#Task 20

cat = str(input("Are you premium member or not (Yes/No): "))
amount = int(input("Enter amount: "))
if cat == "yes" or cat == "Yes":
    if amount > 5000:
        print("Final Discounted amount for premium member : Rs.",amount-amount*20/100)
    else:
        print("No discount... Price : Rs.", amount)
elif cat == "no" or cat == "No":
    if amount > 5000:
        print("Final Discounted amount for non-premium member : Rs.",amount-amount*10/100)
    else:
        print("No discount... Price : Rs.", amount)
else:
    print("Invalid")
