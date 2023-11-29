'''
1. Write a python program to initialize      variables & print its data types.

2. Do Type Conversion for  a) int to string  b) string to int c) bool to string d) string to bool
'''
'''
# 1.
name="Anees"
role="Programmer"
salary=50000
print(name,role,salary)
print(type(name),type(role),type(salary))
'''

# 2.

mynum="100"
print(mynum)
print(type(mynum))

mynum=int(mynum)
print(mynum)
print(type(mynum))


# name="Anees"
# name=int(name)
# print(name)
print("\n")
phonenumber=7854968745896
print(type(phonenumber))
phonenumber=str(phonenumber)
print(type(phonenumber))

print("\n")

mybool=True
print(type(mybool))
mybool=str(mybool)
print(type(mybool))
print("\n")


mybool="True"
print(type(mybool))
mybool=bool(mybool)
print(type(mybool))