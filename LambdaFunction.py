# sum of 2 variables

# Lambda function: it's an 1 liner function

# def sum(a,b):
#     return a+b

# sum = lambda a,b : a+b

# print(sum(10,20))

# x = lambda num : num**2

# print(x(9))

# filter
# listA = [80, 85, 79, 93, 77, 67, 69, 99]

# listB = list(filter(lambda a: a>=80, listA))

# print(listB)

# listNumber = [1,2,3,4,5,6,7,8,9,10]

# listB = list(filter(lambda a: a%2 == 1, listNumber))

# print(listB)

# map

listMarks = [50, 60, 70, 75, 80, 95, 92]

listNewMarks = list(map(lambda mark: mark+5, listMarks))
# listNewMarks = list(map(lambda mark: mark+5, list(filter(lambda m: m <=95, listMarks))))

print(listNewMarks)
