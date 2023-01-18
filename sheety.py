import requests as req
import os
END_POINT = "https://api.sheety.co/e634a57692dcc2c2a245e9c85c0b3389/workoutApp/workouts"
MY_TOKEN = os.environ.get("SHEETY_TOKEN")

def add_row(data: dict) -> int:
    """format of data = {
                "date": "21/07/2022",
                "time": "15:00:00",
                "exercise": "Running",
                "duration": 22,
                "calories": 130,

            }"""
    parameters = {
        "workout": data,
    }
    header={"Authorization": f"Bearer {MY_TOKEN}"}
    # import json
    res = req.post(url=END_POINT, json=parameters, headers=header)
    res.raise_for_status()
    data = res.json()
    return res.status_code
if __name__ == "__maine__":
    print(add_row({
                "date": "21/07/2022",
                "time": "15:00:00",
                "exercise": "Running",
                "duration": 22,
                "calories": 130,

            }))
