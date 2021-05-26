import requests, uuid, json, pandas as pd
df = pd.read_excel("HSEQ POC Translation.xlsx","Cases")
case_dsc = df.iloc[:,2]
text = []
for i in case_dsc:
    text.append({"text":i})

import requests, uuid, json

# Add your subscription key and endpoint
subscription_key = "e6a8ae6bde23484a824a01d387af20f9"
endpoint = "https://api.cognitive.microsofttranslator.com"

# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.
location = "westeurope"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'to': 'en'
}
constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = text[401:405]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

res = json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))
# print(res)
for i in range(len(body)):
    print(response[i]["translations"][0]["text"])

for i in range(401,415):
    print(text[i]["text"])