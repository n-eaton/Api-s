import requests

response=requests.get(url = "http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data=response.json()
print(data)
longtitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']
iss_position=(longtitude,latitude)
print(iss_position)
# For a geographical location:
# https://www.latlong.net/Show-Latitude-Longitude.html