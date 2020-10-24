customer = {"name": "John Smith", "age": 30, "is_verified": True}
print(customer["name"])
print(customer.get("birthdate", "Jan 1 1998"))

customer["name"] = "Jack Smith"
customer["birthdate"] = "Jan 1 1999"
print(customer["name"])
print(customer.get("birthdate"))

