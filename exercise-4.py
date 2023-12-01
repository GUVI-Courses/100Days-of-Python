'''1. Write a program to validate a person can vote or not
*take the age as input from the user
if age is less than 18 print he cannot vote
if age is greater than 18 print he can vote
if age is greater than 90 print please stay at home
if age is 18 than  print please make the voter id '''

age=int(input("Enter your age:\n"))

if(age<18):
    print("You Cannot Vote")

elif(age>18 and age<=90):
    print("You can vote")

elif(age>90):
    print("please stay at home")

elif(age==18):
    print("please make the voter id")
else:
    pass