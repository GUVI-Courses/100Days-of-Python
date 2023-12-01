mystr="welcome to day-2 Session on Python"
# print(mystr)
# mystr='''
# i am good boy
# i am an coder

# '''

# print(mystr)
# print(type(mystr))

# inbuilt method
print("Uppercase",mystr.upper())
print("Lowercase",mystr.lower())
print("index",mystr.index('day'))
print("capitalize",mystr.capitalize())
print("count",mystr.count('o'))
print("count",mystr.count('Python'))
print("find",mystr.find('o'))
print("find",mystr.find('123'))
print("startswith",mystr.startswith("Welcome"))
print("endswith",mystr.endswith("Python"))
print("length",len(mystr))
print(mystr.isalpha())
print(mystr.isalnum())
print(mystr.replace("Python","Python Programming"))
data=mystr.split()
print(data)