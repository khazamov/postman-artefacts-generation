import requests
import subprocess
import logging
import json
import pdb 
from requests.auth import HTTPBasicAuth
import os
from os import path
import sys

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


VERSIONS_FOR_UPDATE=['preview']
UPDATE_URL = 'https://api.getpostman.com/collections/12547236-cb03ba15-66d1-4d68-b9aa-f07b2b06a653'
API_KEY = os.getenv('POSTMAN_MANAGEMENT')


##

# if !path.exists('postman_2021-07.json'):
# 	sys.exit("Collection file does not exist.")

with open('postman_2021-07.json', encoding="utf-8") as f:
    read_collection_data = f.read()


header = {
	'Content-Type': 'application/json',
	'X-API-Key': API_KEY
}


_auth = HTTPBasicAuth('X-API-Key', API_KEY)

collection_wrapper = {}
read_collection_data_json = json.loads(read_collection_data)

collection_wrapper['collection'] = read_collection_data_json
JSON_collection_wrapper = json.dumps(collection_wrapper)


#pdb.set_trace()





response=requests.put(UPDATE_URL, headers=header, data=JSON_collection_wrapper)



print(response.json())
#print(response.reason)
# print(response.request.url)
# print(response.request.body)
# print(response.request.headers)

# print(response.body)


f.close()



