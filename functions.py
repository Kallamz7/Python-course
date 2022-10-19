''' Functions with positional arguments '''


# def wise(weight, height):
#     character = (height ** 2)/weight
#     return character


# w = int(input("What is your Weight: "))
# h = int(input("What is your Height: "))
# my_character = wise(w, h)
# print(character)


''' Functions with keyword arguments '''

#
# def bmi(weight=80, height=6):
#     return(height ** 2)/weight
#
#
# var1 = bmi()
# print(var1)


''' Functions with variable length positional arguments '''


# def result(grades, name, *args):
#     print(grades, name)
#
#
# result("wonder", 'me', 3, 4)

''' Functions with variable length keyword arguments'''


# def myFunc(**kwargs):
#     print(kwargs)
#     print(kwargs['name'])
#
#
# myFunc(age=5, sex="Male", level="uni", name="Peter")

func = lambda x: x ** 2

print(func(5))

