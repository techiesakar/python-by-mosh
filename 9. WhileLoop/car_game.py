# Start to display " Car Started"
# Stop to display "Car Stopped"
# Help to show the available options
# Quit to quit the program

command = ""
started = False
while True:
    command = input("Enter any instructions:\t").lower()
    if command == "start":
        if started:
            print("The car is already started")
        else:
            started = True
            print("Car started...!")
    elif command == "stop":
        if not started:
            print("Car is already stopped...!")
        else:
            started = False
            print("Car is Stopped...!")
    elif command == "help":
        print(
            """
start - to start the car
Stop - to stop the car
quit - to quit
        """
        )
    elif command == "quit":
        print("The program is ended")
        break
    else:
        print("Sorry I don't understand")
