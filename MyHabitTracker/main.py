import requests
from datetime import datetime 

# create user account
TOKEN = "heg78shudjd90a1"
USERNAME = "nimoh"
GRAPHID = "graph1"
PIXELA_ENDPOINTS = "https://pixe.la/v1/users"

# pixela_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# res = requests.post(url= PIXELA_ENDPOINTS, json=pixela_params)
# print(res.text)
# create a graph
graph_endpoints = f"{PIXELA_ENDPOINTS}/{USERNAME}/graphs"

# graph_params = {
#     "id": GRAPHID,
#     "name": "leg workout",
#     "unit": "kilograms",
#     "type": "int",
#     "color": "ajisai"
# }

# headers ={
#     "X-USER-TOKEN": TOKEN
# }
# res = requests.post(url = graph_endpoints, json = graph_params, headers= headers)
# print(res.text)
pixel_creation_endpoint = f"{graph_endpoints}/{GRAPHID}" 

today = datetime.now()
DATE = today.strftime("%Y%m%d")
# graph_config = {
#     "date": DATE,
#     "quantity": input("How much weight did you lift today? ")
    
# }

headers ={
    "X-USER-TOKEN": TOKEN
}

# res = requests.post(url= pixel_creation_endpoint, json= graph_config, headers= headers)
# print(res.text)
# PUT
pixel_update_endpoint = f"{pixel_creation_endpoint}/{DATE}" 

graph_update = {
    "quantity": "1"
}
# res = requests.put(url= pixel_update_endpoint, json= graph_update, headers= headers)
# print(res.text)

# DELETE
res = requests.delete(url= pixel_update_endpoint, headers= headers)
print(res.text)