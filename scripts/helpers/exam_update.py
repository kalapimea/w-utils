import json
from scripts.helpers.dates import *




def update_exams():
    with open("data/exams.json", "r") as f:
        exams = json.load(f)
    
    exams_updated = []
    
    for exam in exams:
        days_to = days_between(get_current_date(), exam["exam_date"]) 
    
        if days_to < 0:
            exam_status = "expired"
        elif days_to == 0:
            exam_status = "today" 
        elif days_to <= 7:
            exam_status = "urgent"
        elif days_to < 20:
            exam_status = "upcoming"
        else:
            exam_status = "far away"

        exam_entry = {
           "exam_class": exam["exam_class"],
           "exam_date": exam["exam_date"],
           "exam_time": exam["exam_time"],
           "exam_status": exam_status
        }

        exams_updated.append(exam_entry)

    with open("data/exams.json", "w") as f:
        json.dump(exams_updated, f, indent=4)


    remove_expired()

def remove_expired():
    
    
    with open("data/exams.json", "r") as f:
        exams = json.load(f)
    with open("data/exams_past.json", "r") as f:
        exams_past = json.load(f)

    exams_updated = []

    for exam in exams:
        if exam["exam_status"] == "expired":
            exams_past.append(exam)
        else:
            exams_updated.append(exam)

    with open("data/exams.json", "w") as f:
        json.dump(exams_updated, f, indent=4)
    with open("data/exams_past.json", "w") as f:
        json.dump(exams_past, f, indent=4)




if __name__ == "__main__":
    update_exams()           