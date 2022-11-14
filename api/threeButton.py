import requests
import json

url = "https://iqwhatsapp.airtel.in:443/gateway/airtel-xchange/basic/whatsapp-manager/v1/session/send/interactive/buttons"

def sendThreeButton(receiver, text_, tag_, title_):
    payload = json.dumps({
        "sessionId": "5792547f57a44b358d3f1425dc163b7f",
        "to": receiver,
        "from": "918904587734",
        "message": {
            "text": text_
        },
        "buttons": [
            {
                "tag": tag_[0],
                "title": title_[0]
            },
            {
                "tag": tag_[1],
                "title": title_[1]
            },
            {
                "tag": tag_[2],
                "title": title_[2]
            },
        ]
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic QUlSVEVMX0RJR19MeEk4VFVLOGVLZnRCa3lQdWlmTDoxeipMVTZLTjxrenNMPytiVzM2'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

# 919820860959
