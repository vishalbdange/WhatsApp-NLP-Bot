import requests
import json

url = "https://iqwhatsapp.airtel.in:443/gateway/airtel-xchange/basic/whatsapp-manager/v1/session/send/media"

payload = json.dumps({
  "sessionId": "31e965f1-5f31-45b0-b522-918af89bcf69",
  "to": "919960855675",
  "from": "918904587734",
  "mediaAttachment": {
    "type": "IMAGE",
    "id": "17fa040a-7c5f-4000-b261-df15f891504d"
  }
})
headers = {
  'Authorization': 'Basic QUlSVEVMX0RJR19MeEk4VFVLOGVLZnRCa3lQdWlmTDoxeipMVTZLTjxrenNMPytiVzM2',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
