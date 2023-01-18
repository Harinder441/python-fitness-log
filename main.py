from nutrition_api import get_calories_data
from sheety import add_row
import datetime as dt

user = input("Which exercise you did today? ")
exercises = get_calories_data(query=user)
# print(exercises)
date_time = dt.datetime.now()
cur_date = date_time.strftime("%d/%m/%Y")
cur_time = date_time.strftime("%H:%M:%S")
# print(cur_date, type(cur_time))
for exercise in exercises:
    user_data = {
        "date": cur_date,
        "time": cur_time,
        "exercise": exercise['name'],
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"],
    }
    add_row(data=user_data)
