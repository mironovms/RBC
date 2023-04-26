import requests
import json


date = '2022-01-21'
key = 'DEMO_KEY'
r = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={date}&api_key={key}")
data = json.loads(r.content)
id_2_photo = data['photos'][1]['id']
print(id_2_photo)