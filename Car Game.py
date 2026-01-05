command = ""
started = False

while True:
    command = input("> ").upper()
    if command == "START":
        if started == True:
            print("Car is already started dude")
        else:
            started = True
            print("Car Started...")
    elif command == "STOP":
        if not started == True:
            print("Car is already stopped dude")
        else:
            started = False
            print("Car Stopped...")
    elif command == "HELP":
        print("""
1.Start - to start the car
2.Stop -  to stop the car
3.Quit - to quit the game
              """)
    elif command == "QUIT":
        print("Game Stopped")    
        break
    else:
        print("I dont understand")



# command = ""

# while command != "QUIT":
#     command = input("> ").upper()
#     if command == "START":
#         print("Car Started...")
#     elif command == "STOP":
#         print("Car Stopped...")
#     elif command == "HELP":
#         print("""
# 1.Start - to start the car
# 2.Stop -  to stop the car
# 3.Quit - to quit the game
#               """)
#     else:
#         print("I dont understand")
# else:
#     print("Game Stopped")
    


