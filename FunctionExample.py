# Using functions, we can write reusable code

# def printNumbers(number):
#     for i in range(number):
#         print(i)

# def printNumbers(start, stop):
#     for i in range(start, stop):
#         print(i)

#printNumbers(4, 12)

# a = 10
# b = 20

# print("Hi")

# printNumbers(51, 61)


# 1. Function define
# 2. Function call
# 3. Function body/suite

# Types of arguments in functions
# 1. Required argument

# def greetings(name):
#     print("Hello",name)

# greetings("Sangita")
# greetings()

# 2. default argument

# def vote(name, age=16):
#     print(name,age)
#     if age>18:
#         print("You are allowed to vote")
#     else:
#         print("You are not allowed to vote")

# vote("Jayesh", 26)

# vote("Sangita")

# 3. Keyword argument

# def sayDetails(firstname, lastname, age):
#     print("Your firstname: ",firstname)
#     print("Your lastname: ",lastname)
#     print("Your age: ",age)

# sayDetails("Jayesh", "Dhandha")

# sayDetails(lastname="Dhandha", firstname= "Jayesh", age=27)

# 4. Variable length argument

def friends(*names):
    print(names)

friends("Jayesh", "Sangita", "Kod Factory")
