import http.client
import json


conn = http.client.HTTPSConnection("rickandmortyapi.com")


conn.request("GET", "/api/character")


res = conn.getresponse()


data = res.read()



data_json = json.loads(data.decode("utf-8"))



print(json.dumps(data_json, indent=4))  

