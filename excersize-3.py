'''
1) Write Python program to evaluatea)Arithmetic Operators, prompt the user for two numerical values and perform addition, subtraction, multiplication, division, and modulo operations on them.
b) Comparison Operators, prompt the user for two numerical values and perform comparisons like greater than, less than, equal to, etc.
c) Logical Operators, prompt the user for two boolean values and perform logical AND, OR, and NOT operations.
d) Assignment Operators, demonstrate the use of various assignment operators on a single variable.
'''

# a)
print("Arthematic opeartion")
num1=int(input("Enter the number 1\n"))
num2=int(input("Enter the number 2\n"))
print("Addition :", num1+num2)
print("Substraction :", num1-num2)
print("Division :", num1/num2)
print("Modulo :", num1%num2)
print("Exponential :", num1**num2)

# b)comparison
print("\nComparision operation")
print(num1<num2)
print(num1>num2)
print(num1>=num2)
print(num1<=num2)
print(num1==num2)
print(num1!=num2)

# c)logical Operation
print("\Logical operation")
print(num1<num2  and num2>num1)
print(num1>num2 and num2<=22)
print(num1>=num2 and False)
print(num1<=num2 or num1>num2)
print(num1==num2 or True)

# d) assignment

num1+=num2
print(num1)
num1-=num2
print(num1)
num1/=num2
print(num1)
num1%=num2
num1**=num2
print(num1)