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

if __name__ == "__main__":
    generate_classes()