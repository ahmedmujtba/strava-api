import requests
import os
from dotenv import load_dotenv
load_dotenv()
access_token = os.environ['access_token']

def get_athlete():
    url = "https://www.strava.com/api/v3/athlete"
    headers = {
        'Authorization':f'Bearer {access_token}',
        #'Authorization':'WsJlsjL0OBEhvVCjO41GRt1IEJ2mRwJP1cKtybep',
        'Accept':'application/json'
    }
    print(headers)
    response = requests.get(url, headers=headers)
    
    # check if the response is successful
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return response.json()


apod_data = get_athlete()
print(apod_data)
