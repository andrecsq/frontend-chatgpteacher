import requests
import json

url = "http://localhost:8000/correction"

payload = json.dumps({
  "sentence_to_translate": "Que horas são?",
  "translation_attempt": "What time is?"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
