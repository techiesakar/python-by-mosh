numbers = [2, 4, 3, 1, 7, 6, 8, 9]
numbers.append(20)  # It add item to the last of the list
print(numbers)

numbers.insert(0, 30)  # It insert the item to particular index placement
print(numbers)  # It remove the particular item

numbers.remove(2)
print(numbers)

numbers.pop()  # It remove the last item
print(numbers)

print(50 in numbers)  # This help to find the existence of item in the list
numbers.clear()  # This clear the list

print(numbers)

# *******************************Another Program************************************ #

another_number = [5, 4, 3, 5, 6, 7, 4, 3, 1]
print(another_number.count(5))  # This count the total number of particular item

another_number.sort()
print(another_number)

another_number.reverse()  # For desending order
print(another_number)

# *******************************Another Program************************************ #

number2 = another_number.copy()
print(number2)

