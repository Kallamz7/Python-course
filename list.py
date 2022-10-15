# Creating a list
Weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]

print(Weekdays)

# Length of a string
print(f'length of var1: {len(Weekdays)}')

# Indexing strings
print(Weekdays[-4:-1])

# Adding a list to another list
Weekends = ["saturday", "sundays"]

Weekdays.extend(Weekends)

print(Weekdays)

# Removing elements from a list
Weekdays.remove("wednesday")

print(Weekdays)

Weekdays.pop()

print(Weekdays)

del Weekdays[4]

print(Weekdays)



