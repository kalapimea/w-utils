from datetime import datetime

def get_current_date():
       return datetime.now().date().isoformat()

def get_current_time():
        return datetime.now().strftime("%H:%M")

def get_current_weekday():
        return datetime.now().strftime("%A")

def convert_to_weekday(iso_date_str):
    iso_date = datetime.fromisoformat(iso_date_str)
    return iso_date.strftime("%A")