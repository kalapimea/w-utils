import json
from scripts.helpers.dates import *

exam_status = "undefined"

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