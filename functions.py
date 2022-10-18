''' Functions with positional arguments '''


# def wise(weight, height):
#     character = (height ** 2)/weight
#     return character
#     print(character)


# w = int(input("What is your Weight: "))
# h = int(input("What is your Height: "))
# my_character = wise(w, h)


''' Functions with keyword arguments '''


def bmi(weight=80, height=6):
    return(height ** 2)/weight


var1 = bmi()
print(var1)


''' Functions with variable arguments '''
