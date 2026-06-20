import json
from scripts.helpers.dates import *
from scripts.helpers.exam_update import *

def exams(command):
    if command[1] == "help":
        print("""exam add <class> <yyyy-mm-dd> <hh:mm>
              exam show [yyyy-mm-dd]
              exam update""")
    
    elif command[1] == "add":
        if len(command) >= 5:
            exam_class = command[2]
            exam_date = command[3]
            exam_time = command[4]
            

            
            with open("data/exams.json", "r") as f:
                exams = json.load(f)
            
            exam_entry = {
                "exam_class": exam_class,
                "exam_date": exam_date,
                "exam_time": exam_time,
                "exam_status": "undefined"
            }
            
            exams.append(exam_entry)

            with open("data/exams.json", "w") as f:
                json.dump(exams, f, indent=4)

    elif command[1] == "show":
        with open("data/exams.json", "r") as f:
            exams = json.load(f)

        if len(command) > 2:
            date_filter = command[2]

            for exam in exams:
                if exam["exam_date"] == date_filter:
                    print(f"{exam["exam_class"]} exam on {exam["exam_date"]} ({convert_to_weekday(exam["exam_date"])}) at {exam["exam_time"]}")
        else:
            for exam in exams:
                print(f"{exam["exam_class"]} on {exam["exam_date"]} ({convert_to_weekday(exam["exam_date"])}) at {exam["exam_time"]}")

    elif command[1] == "update":
        update_exams()