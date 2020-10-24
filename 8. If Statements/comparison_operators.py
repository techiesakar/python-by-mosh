# If temperature is greater than 30
#    It's a hot day
# Otherwise if temp less than 10
# It's a cold day
# Otherwise
#   It's neither hot nor cold

temp = input("Enter the temperature: \t")
if float(temp) > 30:
    print("It's a hot day today")
elif float(temp) < 10:
    print("It's a cold day")
else:
    print("It's neither cold nor hot ")
