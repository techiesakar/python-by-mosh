numbers = [1, 2, 3, 2, 1, 2, 3, 2, 4, 5, 4, 5, 6, 7, 55, 6, 7, 6, 8, 7, 8, 7, 8]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

# This is very clear logic.
# If the numbers are not in uniques, then append will simply add the list in numbers to the uniques
# By doing this we get unique list item without any duplicates
