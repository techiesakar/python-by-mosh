class Person:
    def __init__(self, name):  # double underscore init is method
        self.name = name  # self refers to current object. We are setting the name attribute of the current object
        # to the name argument pass to upper "init" method

    def talk(self):  # talk is Method
        print(f"Hi! I am {self.name}")


john = Person("John Smith")  # John is variable
john.talk()

bob = Person("Bob Smith")
bob.talk()  # Each object is different instance of a Person Class
