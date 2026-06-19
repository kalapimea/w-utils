import json

def generate_classes():

    classes = ["math", "chemistry", "history", "religion", "physics", "english", "swedish", "german", "finnish", "biology", "geography", "health-education"]

    classes.sort()

    subjects = []

    for subject in classes:
        class_name = subject
        class_teacher = "nobody"
        class_room_number = "A000"

        classes_dict = {
            "class_name": class_name,
            "class_teacher": class_teacher,
            "class_room_number": class_room_number
        }

        subjects.append(classes_dict)

    with open("data/classes.json", "w") as f:
        json.dump(subjects, f, indent=4)

    print("Succesfully configured classes.json!")

def generate_classes_custom():
    if input("do you want to use your own list of subjects instead of the predifined one (yes/no): ").lower == "yes":
        classes = ["math", "chemistry", "history", "religion", "physics", "english", "swedish", "german", "finnish", "biology", "geography", "health-education"]
    else:
        classes = []

        for i in range(int(input("how many classes do you have?: "))):
            classes.append(input(f"enter name of class number {i+1}: "))
    
    classes.sort()

    subjects = []
    for subject in classes:
        classes_dict = {
            "class_name": subject,
            "class_teacher": input("enter name of your {subject} teacher: "),
            "class_room_number": input("enter class room number of {subject}: ")
        }

        subjects.append(classes_dict)

    with open("data/classes.json", "w") as f:
        json.dump(subjects, f, indent=4)
    
    print("succesfully generated custom configuration to classes.json!")

def reset_configuration():
    subjects = []

    with open("data/classes.json", "w") as f:
        json.dump(subjects, f, indent=4)

if __name__ == "__main__":
    operation = int(input("""what do you want to do?
                          1. generate default configuration
                          2. generate custom configuration
                          3. generate empty confuguration
                          enter number of operation: """))
    
    if operation == 1:
        generate_classes()
        print("succesfully generated defaults")
    elif operation == 2:
        generate_classes_custom()
        print("succesfully generated custom")
    elif operation == 3:
        reset_configuration()
        print("succesfully generated empty")
    else:
        print("invalid operation")