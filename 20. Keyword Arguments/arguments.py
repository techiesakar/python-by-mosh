def greet_user(fname, lname):  # fname and lname are the first and second parameters
    print(f"Hi! {fname} {lname}")
    print("Welcome to Australia")


greet_user(lname="Aryal", fname="Samir")  # This is keyword arguments


def calc_cost(total, shipping, discount):
    print(f"The total cost is {total}")
    print(f"The total shippings are {shipping}")
    print(f"The total discount is {discount}")


calc_cost(
    total=50, shipping=5, discount=0.1
)  # Calculating the total cost of the ordered items
