# API

# Application Programming Interface
# How Software can communicate with one another

import requests
import json

#
# post_code_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
#
# print(post_code_req) # <Response [200]>
#
# print(post_code_req.status_code)  # 200
#
# print(post_code_req.headers) # http readers returned
# print(post_code_req.content) # raw content
# print(post_code_req.json()) # json content
# print(type(post_code_req.json())) # <class 'dict'>
#
# Now we will ask for specific details/ We do this by now importing JSON

json_body = json.dumps({"postcodes": ["PR8 5DB", "M45 6GN", "EX165BL"]})

headers = {"Content-Type" : "application/json"}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

print(post_multi_req.json())
