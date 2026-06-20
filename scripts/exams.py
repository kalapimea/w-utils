import json
from scripts.helpers.dates import *


def exams(command):
    if command[1] == "help":
        print("""exam add <class> <yyyy-mm-dd> <hh:mm>""")
    
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
                "exam_time": exam_time
            }
            
            exams.append(exam_entry)

            with open("data/exams.json", "w") as f:
                json.dump(exams, f, indent=4)