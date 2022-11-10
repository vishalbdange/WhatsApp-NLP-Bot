# import OS for environment variables
import json
import os

# import requests
import requests

GOOGLE_API_KEY='AIzaSyA-nlgpQYBXwZDK4bZ7kd6bpH_wCD6BBWQ'
AirtelIQ_url = "https://iqwhatsapp.airtel.in:443/gateway/airtel-xchange/basic/whatsapp-manager/v1/session/send/text"


def google_search():
    url='https://customsearch.googleapis.com/customsearch/v1'
    cx='21f70c2b29d284393'
    search_key = GOOGLE_API_KEY
    parameters = {
        "q" : "Neel dandiwala",
        "cx" : cx,
        'key' : search_key,
    }
    page=requests.request("GET",url,params=parameters)
    results = json.loads(page.text)
    # print(results['items'])
    top_4_searches =  [results['items'][3],results['items'][2],results['items'][1],results['items'][0]]

    payload = json.dumps({
          "sessionId": "5792547f57a44b358d3f1425dc163b7f",
          "to": "919960855675",
          "from": "918904587734",
          "message": {
            "text": "1. " +  top_4_searches[0]['snippet'] + '\n' +top_4_searches[0]['link'] + "\n\n 2. " +  top_4_searches[1]['snippet'] + '\n' +top_4_searches[1]['link'] + "\n\n 3. "  +  top_4_searches[2]['snippet'] + '\n' +top_4_searches[2]['link'] + "\n\n 4. "+  top_4_searches[3]['snippet'] + '\n' + top_4_searches[3]['link'] + "\n"
          }
        })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic QUlSVEVMX0RJR19MeEk4VFVLOGVLZnRCa3lQdWlmTDoxeipMVTZLTjxrenNMPytiVzM2'
    }

    response = requests.request("POST", AirtelIQ_url, headers=headers, data=payload)
    print(response.text)

google_search()