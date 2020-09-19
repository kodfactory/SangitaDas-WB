# Take the marks of student as input

# If marks are greater then 80 then print Grade A
# If marks are between 60 and 80 print Grade B
# If marks are between 35 and 60 print Grade C
# If marks are less then 35 then Fail

marks = int(input("Enter the marks: "))

# if marks >= 80:
#     print("Grade A")
# elif marks < 80 and marks >= 60:
#     print("Grade B")
# elif marks < 60 and marks >= 35:
#     print("Grade C")
# else:
#     print("Oh Oh... You are fail...")

if marks >= 80:
    print("Grade A")
elif 60 <= marks < 80:
    print("Grade B")
elif 35 <= marks < 60:
    print("Grade C")
else:
    print("Oh Oh... You are fail...")
