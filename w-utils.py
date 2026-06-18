import json

def grade(command):
    if command[1] == "help":
        print("""help> grade add <class> <grade> <yyyy-mm-dd>
              
              Adds a new grade entry
              
              Arguments: 
              <class>       Subject name
              <grade>       Grade received from exam
              <yyyy-mm-dd>  Date of exam
              
              Notes: 
               - Arguments are order sensitive.
               - Class names may not contain spaces.
                 - See 'class list' for full list of class names.
               - Do not include quotation marks.
              
              
              help> grade show [--flag] [filter]
              
              Shows previously added grade entries
              
              Arguments: 
              [-flag] Takes one of 3 flags to specify the filter type: 
                --class OR -c for class
                --grade OR -g for grade
                --date OR -d for date
              [Filter] Will accept any single argument also seen in 'grade add'.

              Notes: 
               - Adding a filter is optional; empty 'grade show' with no filter will list all grade entries
               - Only use a single argument for filtering
               - Using more than one argument will ignore everything but the first argument after 'show'
               -Always use a flag when filtering to specify the filter type
               -Flags should always be added before the filter
              """)
    
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
            grades = json.load(f)    #loads grades.json onto grades
        
        grades.append(grade_entry)

        with open("data/grades.json", "w") as f:
            json.dump(grades, f, indent=4)   #writes updates grades onto grades.json. indent=4 for nicer formatting

    elif command[1] == "show":
        with open("data/grades.json", "r") as f:
            data = json.load(f)    #loads grades.json to data
        
        if len(command) > 2:    #checks lengs of command to avoid error for not having extra arguments
            
            
            if command[2] == "--class" or command[2] == "-c":
                filter = command[3]    #sets filter to the filter entered on the command

                for entry in data:
                    if entry["class_name"] == filter:
                        print(f"class: {entry["class_name"]} | grade:{entry["grade"]} | date: {entry["date"]} ")
            
            elif command[2] == "--grade" or command[2] == "-g":
                filter = command[3]

                for entry in data:
                    if entry["grade"] == filter:
                        print(f"class: {entry["class_name"]} | grade: {entry["grade"]} | date: {entry["date"]}")

            elif command[2] == "--date" or command[2] == "-d":
                filter = command[3]

                for entry in data:
                    if entry["date"] == filter:
                        print(f"class: {entry["class_name"]} | grade: {entry["grade"]} | date: {entry["date"]}")
            
            else:
                print(f"Invalid flag '{command[2]}'")
        
        
        else:
            for entry in data:
                print(f"class: {entry["class_name"]} | grade: {entry["grade"]} | date: {entry["date"]}")
                
    
def classes(command):
    if command[1] == "help":
        print(""" Help text goes Here""")
    
    elif command[1] == "list":
        with open("data/classes.json", "r") as f:
            data = json.load(f)
        
        for subject in data:
            print(subject["class_name"])






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