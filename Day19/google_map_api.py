import requests

api_key = "AIzaSyA8VRK8GqobS2yWJHn4Aj7-VDnqei_H82g"
url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
params = {
    'key' : api_key,
    'radius' : '1000',
    'location' : '33.590,130.401',
    'type':'restaurant'
}

response = requests.get(url,params=params)
result = response.json()
print(result['results'][0])