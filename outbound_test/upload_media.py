import requests
import json

url = "https://iqwhatsapp.airtel.in:443/gateway/airtel-xchange/basic/whatsapp-manager/v1/session/media"

payload={
    'type': 'IMAGE',
    'businessId': 'Hackathon_918904587734'
}

files=[
  ('file',('test_01.jpeg',open('C:/projects/AirtelIQ/sample_media/test_01.jpeg','rb'),'image/jpeg'))
]
headers = {
  'Content-Type': 'application/json',
  'Accept':'*/*',
  'Authorization': 'Basic QUlSVEVMX0RJR19MeEk4VFVLOGVLZnRCa3lQdWlmTDoxeipMVTZLTjxrenNMPytiVzM2',
  'Connection':'keep-alive'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response)
