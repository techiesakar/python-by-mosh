course = "python for beginners"
print(len(course))  # Print the length of the string

print(course.upper())  # Make all letters Capital
print(course.title())  # Make the first letter capital of every words
print(course.capitalize())  # Make the only first letter capital of first word
print(course.lower())  # Lower all the character

print(course.find("p"))  # Find the index value, it is case sensitive
print(course.find("o"))
print(course.find("beginners"))
print(course.replace("beginners", "absolute beginners"))
print(course.replace("p", "P"))  # Replacing small p with the capital one

print(course)

print("python" in course)  # in Operator
