# By using nested loop

numbers = [5, 2, 5, 2, 2]
for X_count in numbers:
    output = ''
    for count in range(X_count):
        output = output + 'X'
    print(output)
