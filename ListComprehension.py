# letters = []  
# for letter in 'Python':
#     letters.append(letter)  
# print(letters)

# Above task can be achieve in single line using list comprehension

letters = [letter for letter in 'Python' if letter != 'o']

print(letters)


