import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

headers = {'Content-type': 'application/json', 'Authorization':'Bearer $openai_api_key'}
url = "https://api.openai.com/v1/images/generations"
prompt = 'While traveling through a dense forest, you stumble upon an ancient, overgrown path veering off from the main trail. Do you dare to explore its mysteries?'

data = {'prompt': prompt, 'n':1, 'size': "1024x1024", 'response_format': 'url'}
response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.json())
