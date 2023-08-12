import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

def text_to_image(prompt: str):
   authorization = f"Bearer {openai_api_key}"
   headers = {'Content-type': 'application/json', 'Authorization': authorization}
   url = "https://api.openai.com/v1/images/generations"
   data = {'prompt': prompt, 'n':1, 'size': "1024x1024", 'response_format': 'url'}
   response = requests.post(url, data=json.dumps(data), headers=headers)
   return response.json()['data'][0]['url']


def main():
   prompt = 'While traveling through a dense forest, you stumble upon an ancient, overgrown path veering off from the main trail. Do you dare to explore its mysteries?'
   image_url = text_to_image(prompt)
   print(image_url)

if __name__ == '__main__':
    main()
