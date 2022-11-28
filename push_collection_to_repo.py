import requests
import subprocess
import logging
import json
import pdb 
from requests.auth import HTTPBasicAuth

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


VERSIONS_FOR_UPDATE=['preview']
UPDATE_URL = 'https://api.getpostman.com/collections/12547236-cb03ba15-66d1-4d68-b9aa-f07b2b06a653'
API_KEY = 'PMAK-636d33b8b11a1127f78b6af5-753d32c2da46d48fccb1c94c891941a97b'


# p = subprocess.Popen("openapi2postmanv2 -s 2021-07___oas.json  -o postman_2021-07.json -p -O folderStrategy=Tags,requestParametersResolution=Schema,responseParametersResolution=Schema,optimizeConversion=false,stackLimit=50", stdout=subprocess.PIPE, shell=True)


# with open('postman_2021-07.json', encoding="utf-8") as f:
#     read_collection_data = f.read()



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



