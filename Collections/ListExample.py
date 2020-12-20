# 1. List
# 2. Set
# 3. Tuple 
# 4. Dictionary

# Syntax: [elem1, elem2, elem3]
listA = ["SangitA", "jaya", "Amita", "Nikita"]

listB = ["Pooja", "Aditi"]

# print(listA + listB)

# listC = [1, 10, "Hi", "Hello", 5.5, 0]

# print(listC[-1])

# print(listC[3])

# for i in listA:
#     if i.lower() == "sangita":
#         print("Name exist")
# else:
#     print("Name exist")

# if "Jayas" not in listA:
#     print("Name not exist")
# else:
#     print("Name exist")


# print(listA[1:3])
# print(listA[2:])
# print(listA[-1])

# listC = listA + listB

# print(listA + listB)

# print(listB * 2)

# adding a new element in a list
# remove element from list
# Join 2 lists
# split 
# repeat a element in list

# print(listA)

# listA.append("Mrunali")

# listA.remove("Jaya")

# print(listA)

listD = [1, 10, "Hi", "Hello", 5.5, 0, 'A', 'B']

# List iteration can be done using for loop
# for i in listD:
#     print(i)

# print("Length of my list: ",len(listD))

# i = 0 
# while i < len(listD):
#     print(listD[i])
#     i += 1

listNo = [1,2,2,2,3,3,3,3,4,4,5,5,6,6,7,7,77,8,8,9,9,9,0,0,0,9,88,8]

listNew = []

# Hint: Create new empty list and try to use iteration
for i in listNo:
    if i not in listNew:
        listNew.append(i)

print(listNew)


# listC = list(listNo)





