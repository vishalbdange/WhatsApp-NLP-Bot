import requests
import json

url = "https://iqwhatsapp.airtel.in:443/gateway/airtel-xchange/basic/whatsapp-manager/v1/session/send/interactive/buttons"

def sendTwoButton(receiver, text, tag, title):
    payload = json.dumps({
        "sessionId": "5792547f57a44b358d3f1425dc163b7f",
        "to": receiver,
        "from": "918904587734",
        "message": {
            "text": text
        },
        "buttons": [
            {
                "tag": tag[0],
                "title": title[0]
            }, 
            {
                "tag": tag[1],
                "title": title[1]
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic QUlSVEVMX0RJR19MeEk4VFVLOGVLZnRCa3lQdWlmTDoxeipMVTZLTjxrenNMPytiVzM2'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

# 919820860959
