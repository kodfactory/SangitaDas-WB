# num = 2

#if num > 5 and num < 20 :
#    print("Number is between 5 and 20")
#    print("Some other code in if statement")

#print("Common code")

# if num > 10 :
#     print("Number is greater then 10")
# else:
#     print("Number is not greater then 10")

# Homework: take any number and print whether
# that number is odd or even

# 1,4,6,7,8,9,13,14
# odd : 1,7,9,13
# even: 4,6,8,14

# odd numbers % 2 then reminder will be 1
# even numbers % 2 then reminder will be 0

number = int(input("Enter the number: "))

print(type(number))

if number%2 == 0:
    print("Number is even")
else:
    print("Number is odd")

