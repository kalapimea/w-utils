from scripts.helpers.classes_gen import *

def classes(command):
    if command[1] == "help":
        print("""help> use 'class list' to list all classes,
              if nothing shows up, use 'class generate default' to generate default configuration of classes to classes.json
              or 'class generate custom' for a customied generation
              or 'class generate reset' to empty out classes.json (you do not need to reset before the other commands)
              
              use 'class info <class> <info>' to see information about class.
              
              <class> takes any of the classes seen in  'class list' as input
              <info> takes one of the following to show about <class>:
                teacher        shows name of teacher
                room           shows room number of class""")
    
    elif command[1] == "list":
        with open("data/classes.json", "r") as f:
            data = json.load(f)
        
        for subject in data:
            print(subject["class_name"])
    
    elif command[1] == "generate":
        if len(command) > 2:
            if command[2] == "default":
                generate_classes()
            elif command[2] == "custom":
                generate_classes_custom()
            elif command[2] == "empty":
                reset_configuration()  

    elif command[1] == "info":
        filter_class = command[2]
        info = command[3]

        with open("data/classes.json", "r") as f:
            subjects = json.load(f)

            for subject in subjects:
                if subject["class_name"] == filter_class:
                    if info == "teacher":
                        print(f"Teacher of {subject["class_name"]} is {subject["class_teacher"]}")
                    elif info == "room":
                        print(f"Room number of {subject["class_name"]} is {subject["class_room_number"]}")
                    else:
                        print("invalid info flag of {info}")
                    
                    break
            else:
                print(f"No such class '{filter_class}' found")