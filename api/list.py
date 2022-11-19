import requests
import json
from deep_translator import GoogleTranslator

url = "https://iqwhatsapp.airtel.in:443/gateway/airtel-xchange/basic/whatsapp-manager/v1/session/send/interactive/list"


def sendList(receiver, langId, text, heading, tag, title, description):
    if langId != 'en':
        text = GoogleTranslator(source="en", target=langId).translate(text)
        heading = GoogleTranslator(source="en", target=langId).translate(heading)
        
        for x in title:
            title[0] = GoogleTranslator(source="en", target=langId).translate(title[0]) + '(' + tag[0] +')'
            if description != None:
                description[0] = GoogleTranslator(source="en", target=langId).translate(description[0])
    options = []     
    for i in range(0, len(tag)):
        if description != None:
            options.append({
                        "tag": tag[i],
                        "title": title[i],
                        "description": description[i]
                    })
        else:
            options.append({
                        "tag": tag[i],
                        "title": title[i]
                    })
            
        
    payload = json.dumps({
        "sessionId": "31e965f1-5f31-45b0-b522-918af89bcf69",
        "to": receiver,
        "from": "918904587734",
        "message": {
            "text": text
        },
        "list": {
            "heading": heading,
            "options": options
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic QUlSVEVMX0RJR19MeEk4VFVLOGVLZnRCa3lQdWlmTDoxeipMVTZLTjxrenNMPytiVzM2'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)