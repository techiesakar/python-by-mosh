weight = int(input("Weight: \t"))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
elif unit.upper()=="P":
    converted = weight / 0.45
    print(f"You're {converted} pounds")
else:
    print("Please enter the correct Unit")

