import requests
import json

url = "https://iqwhatsapp.airtel.in:443/gateway/airtel-xchange/basic/whatsapp-manager/v1/session/send/interactive/list"


def sendList():
    payload = json.dumps({
        "sessionId": "31e965f1-5f31-45b0-b522-918af89bcf69",
        "to": "919820860959",
        "from": "918904587734",
        "message": {
            "text": "Multiple stores are available at this pin code. Select one of the below to start your grocery shopping."
        },
        "list": {
            "heading": "Select Store",
            "options": [
                {
                    "tag": "store1",
                    "title": "Store 1",
                    "description": "Ambience Mall, Gurugram"
                },
                {
                    "tag": "store2",
                    "title": "Store 2",
                    "description": "Cyber Hub, Gurugram"
                }
            ]
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic QUlSVEVMX0RJR19MeEk4VFVLOGVLZnRCa3lQdWlmTDoxeipMVTZLTjxrenNMPytiVzM2'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
