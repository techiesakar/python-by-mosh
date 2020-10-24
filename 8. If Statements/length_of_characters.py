# If name is less than 3 characters long
#   name must be at least 3 characters
# Otherwise if it's more than 50 characters long
#   name can be a maximum of 50 characters
# Otherwise
#   name looks good!

name = input("Enter the name of a person: \t")
if len(name) < 3:
    print("Name must be at least of 3 characters")
elif len(name) > 50:
    print("Name can't be have more than 50 characters")
else:
    print("Name looks Good!")

