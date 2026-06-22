import json
from scripts.helpers.dates import *
from scripts.helpers.exam_update import *

def exams(command):
    if command[1] == "help":
        print("""exam add <class> <yyyy-mm-dd> <hh:mm>
              exam show [--flag] [filter]
              exam update
              flags --status/-s --date/-d
              exam show past [--flag] [filter]""")
    
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
    
    elif command[1] == "show" and command[2] == "past":   #dont question it... i added this way after the other show so i couldent fit it there nicely
        with open("data/exams_past.json", "r") as f:
            exams_past = json.load(f)

        if len(command) >= 5:
            if command[3] == "--date" or command[3] == "-d":
                filter_date = command[4]
            elif command[3] == "--subject" or command[3] == "-s":
                filter_subject = command[4]
            else:
                filter_date = ""
                filter_subject = ""
            
            for exam in exams_past:
                if exam["exam_date"] == filter_date or exam["exam_class"] == filter_subject:
                    print(f"{exam["exam_class"]} exam was on {exam["exam_date"]}")
        for exam in exams_past:
            print(f"{exam["exam_class"]} exam was on {exam["exam_date"]}")
            
        
    
    elif command[1] == "show":
        with open("data/exams.json", "r") as f:
            exams = json.load(f)

        date_filter = ""
        status_filter = ""
        
        if len(command) >= 4:
            if command[2] == "--date" or command[2] == "-d":
                date_filter = command[3]
            elif command[2] == "--status" or "-s":
                status_filter = command[3]
           
            for exam in exams:
                if exam["exam_date"] == date_filter or exam["exam_status"] == status_filter:
                    print(f"{exam["exam_class"]} exam on {exam["exam_date"]} ({convert_to_weekday(exam["exam_date"])}) at {exam["exam_time"]}")
        else:
            for exam in exams:
                print(f"{exam["exam_class"]} on {exam["exam_date"]} ({convert_to_weekday(exam["exam_date"])}) at {exam["exam_time"]}")

    elif command[1] == "update":
        update_exams()