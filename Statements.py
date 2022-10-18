#If-else conditional statement
# var1 = 18
# age = int(input("How old are you?"))
#
# if age >= var1:
#     print(f"\nYou are an adult")
# else:
#     print(f"\nYou are a child")

#If,else-if,else conditional statemant
grade = input("What was your grade: ")

if grade.upper == "A":
    print(f'Your grade is {5.0}\nYou are a Genius')
elif grade.upper == "B":
    print(f'Your grade is {4.0}\nYou are Good, but you can do better')
elif grade.upper == "C":
    print(f'Your grade is {3.0}\nYou are close to being a Failure. You need to sit up.')
elif grade.upper == "D":
    print(f'Your grade is {2.0}\nSmall tin remain for you to fail ohhhh!!! Wise up')
else:
    print(f"Your grade is {0.0}\nYou Failed")