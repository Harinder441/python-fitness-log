import requests as req
GENDER = "male"
WEIGHT_KG = 60
HEIGHT_CM = 160
AGE = 24

API_ID = YOUR_ID
API_KEY = YOUR_API_KEY


def get_calories_data(query="i ran 2 km today") -> list:
    """will return a dictionary as {calories : ,'name':,duration:}"""
    calories_para = {
        "query": query,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE,
    }
    calories_header = {
        "x-app-id": API_ID,
        "x-app-key": API_KEY,

    }
    calories_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    # used data because of the int and float values
    res = req.post(url=calories_endpoint, data=calories_para, headers=calories_header)
    res.raise_for_status()
    data = res.json()
    # format_data = {'calories': data['exercises'][0]['nf_calories'], 'name': data['exercises'][0]['name'],
    #                'duration': data['exercises'][0]['duration_min']}
    return data['exercises']


if __name__ == "__main__":
    print(get_calories_data())
