'''1) write a python program to evaluate below String
a) Add the string1 "Zen Classes" & string2 "GUVI"  and print the new string   
b) Find the length of the string and reverse it 
'''
'''
2) write a python program to evaluate below string 
mystr= "GUVI is an IIT-M & IIM-A incubated Ed-tech company“  
a) print "incubated " using positive slicing & negative slicing  
b) print "company" using negative slicing  
c) print "G n" using stepindex  
d) print "Gy"    using stepindex
'''

# 3) Take a inputs  from user and evaluate the expression. 
# a) Take the Students name. 
# b) Take the student english marks, maths, science, social, kannada & hindi 
# c) add the total marks  
# d) print average 
# e) add languages marks (english, kannada, hindi)and print average 
# f) add the core subjects (maths, science and social) and print average

# 1
'''
string1="Zen Classes"
string2=" Guvi"
string3=string1+string2
print(string3)
print("length is ",len(string3))
print("Reverse is ",string3[::-1])
'''

# 2
'''
mystr="GUVI is an IIT-M & IIM-A incubated Ed-tech company"
print(mystr[25:34])
print(mystr[-25:-16])
print(mystr[-7:])

print(mystr[::24])
print(mystr[0::49])
'''

# 3

studentName=input("enter the student Name \n")
english =int(input("Enter the english marks \n"))
maths=int(input("Enter the maths marks \n"))
science =int(input("Enter the  science marks \n"))
social=int(input("Enter the  social marks \n"))
kannada  =int(input("Enter the kannada marks \n"))
hindi=int(input("Enter the hindi marks \n"))

total=english+maths+science+social+kannada+hindi
avgmarks=total/6

languages=english+kannada+hindi
avglan=languages/3
core=maths+science+social
coreavg=core/3


print("Student Name is ",studentName)
print("Total marks is ",total)
print("\n")
print("Average marks is ",avgmarks)
print("Lanaguge Total marks is ",languages)
print("Lanaguge Average marks is ",avglan)
print("\n")
print("Core subjects Total marks is ",core)
print("Core Subject Average marks is ",coreavg)
