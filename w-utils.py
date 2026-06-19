from scripts.grades import *
from scripts.classes import *    


#Main loop
print("W-utils> Welcome to W-utils. \nType 'help' for a list of commands and '<command> help' for help with a command")
running = True
while running:
    command = input("W-utils> ").lower()
    parts = command.split()

    
    #todo: add help command
    if parts[0] == "exit":
        running = False
    elif parts[0] == "grade":
        grade(parts)
    elif parts[0] == "class":
        classes(parts)