import json

def grade(command):
    if command[1] == "help":
        print("""help> grade add <class> <grade> <yyyy-mm-dd>
              
              Adds a new grade entry
              
              Arguments: 
              <class>       Subject name
              <grade>       Grade recieved from exam
              <yyyy-mm-dd>  Date of exam
              
              Notes: 
               - Arguments are order sensitive.
               - Class names may not contain spaces.
                 - See 'class list' for full list of class names.
               - Do not include quotation marks.""")
    
    elif command[1] == "add":
        class_name = command[2]
        grade = command[3]
        date = command[4]        
        
        grade_entry = {
            "class_name": class_name,
            "grade": grade,
            "date": date
        }

        with open("data/grades.json", "r") as f:
            grades = json.load(f)
        
        grades.append(grade_entry)

        with open("data/grades.json", "w") as f:
            json.dump(grades, f, indent=4)

#Main loop
print("W-utils> Welcome to W-utils. \nType 'help' for a list of commands and '<command> help' for help with a command")
running = True
while running:
    command = input("W-utils> ").lower()
    parts = command.split()

    
    #todo: add help command
    if parts[0] == "exit":
        running = False
        break
    elif parts[0] == "grade":
        grade(parts)