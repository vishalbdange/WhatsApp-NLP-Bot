import requests
import json
from deep_translator import GoogleTranslator

url = "https://iqwhatsapp.airtel.in:443/gateway/airtel-xchange/basic/whatsapp-manager/v1/session/send/text"

def sendText(receiver, langId, text):
    if langId != 'en':
        text = GoogleTranslator(source="en", target=langId).translate(text)
        
    payload = json.dumps({
        "sessionId": "5792547f57a44b358d3f1425dc163b7f",
        "to": receiver,
        "from": "918904587734",
        "message": {
            "text": text
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic QUlSVEVMX0RJR19MeEk4VFVLOGVLZnRCa3lQdWlmTDoxeipMVTZLTjxrenNMPytiVzM2'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

# 919820860959
