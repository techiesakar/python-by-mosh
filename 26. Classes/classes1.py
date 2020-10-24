class Computer:  # Attributes = Variables, Behaviour = Method (function)
    def config(self):
        print("i5, 8 GB, 500GB")


com1 = Computer()  # This means Com1 is an Object of Computer
com2 = Computer()
Computer.config(com1)
Computer.config(com2)  # calling config for Com2

com1.config()  # We are using the object self to call the function
com2.config()  # It means we are calling the config
